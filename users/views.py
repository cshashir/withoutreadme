from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime
from django.utils import timezone
from django.contrib import messages
from django.db import IntegrityError
from django.http import Http404, HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, DetailView
from django.conf import settings
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import *
from blog.models import *
from .models import *
from partshala.urls import *
from blog.urls import *

# User = settings.AUTH_USER_MODEL


def register_fellow(request):
    if request.method == 'POST':
        form = FellowRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_fellow = True
            user.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You can Log in')
            return redirect('login')
    else:
        form = FellowRegisterForm()
    return render(request, 'users/register-fellow.html', {'form': form})


def register_associate(request):
    if request.method == 'POST':
        form = AssociateRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_associate = True
            user.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You can Log in')
            return redirect('login')
    else:
        form = AssociateRegisterForm()
    return render(request, 'users/register-associate.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is None:
                messages.warning(request, f'Please enter correct username and password. Sign up if you are new to Partshala')
                return redirect('login')
            elif user.is_fellow:
                login(request, user)
                return redirect('profile_fellow')
            else:
                login(request, user)
                return redirect('profile_associate')
    else:
        form = UserLoginForm()

    context = {
        'form': form,
    }
    return render(request, 'users/login.html', context)


@login_required(login_url=reverse_lazy('login'))
def profile_fellow(request):
    if request.method == 'POST':
        u_form = FellowUpdateForm(request.POST, instance=request.user.profilefellow)
        p_form = FellowPicUpdateForm(request.POST, request.FILES, instance=request.user.profilefellow)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile_fellow')
    else:
        u_form = FellowUpdateForm(instance=request.user.profilefellow)
        p_form = FellowPicUpdateForm(instance=request.user.profilefellow)

    logged_in_fellow_posts = Post.objects.filter(fellow=request.user).order_by('-post_date')

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'logged_in_fellow_posts': logged_in_fellow_posts
    }
    return render(request, 'users/profile_fellow.html', context)


@login_required(login_url=reverse_lazy('login'))
def profile_associate(request):
    if request.method == 'POST':
        u_form = AssociateUpdateForm(request.POST, instance=request.user.profileassociate)
        p_form = AssociatePicUpdateForm(request.POST, request.FILES, instance=request.user.profileassociate)
        d_form = SSCResultForm(request.POST, request.FILES, instance=request.user.profileassociate)
        e_form = HSCResultForm(request.POST, request.FILES, instance=request.user.profileassociate)
        dl_form = DLCopyForm(request.POST, request.FILES, instance=request.user.profileassociate)
        if u_form.is_valid() and p_form.is_valid() and d_form.is_valid():
            u_form.save()
            p_form.save()
            d_form.save()
            e_form.save()
            dl_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile_associate')
    else:
        u_form = AssociateUpdateForm(instance=request.user.profileassociate)
        p_form = AssociatePicUpdateForm(instance=request.user.profileassociate)
        d_form = SSCResultForm(instance=request.user.profileassociate)
        e_form = HSCResultForm(request.POST, request.FILES, instance=request.user.profileassociate)
        dl_form = DLCopyForm(request.POST, request.FILES, instance=request.user.profileassociate)
    # logged_in_associate_applications = Post.objects.filter(associate=request.user).order_by('-date')

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'd_form': d_form,
        'e_form': e_form,
        'dl_form': dl_form,
        # 'logged_in_associate_applications': logged_in_associate_applications
    }
    return render(request, 'users/profile_associate.html', context)


class ApplyJobView(CreateView):
    model = Application
    form_class = ApplyJobForm
    slug_field = 'post_id'
    slug_url_kwarg = 'post_id'

    @method_decorator(login_required(login_url=reverse_lazy('login')))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self.request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            messages.info(self.request, 'Successfully applied for the job!')
            return self.form_valid(form)
        else:
            return HttpResponseRedirect(reverse_lazy('blog-home'))

    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'id': self.kwargs['post_id']})

    def form_valid(self, form):
        # check if user already applied
        associate = Application.objects.filter(associate_id=self.request.user.id, post_id=self.kwargs['post_id'])
        if associate:
            messages.info(self.request, 'You already applied for this job')
            return HttpResponseRedirect(self.get_success_url())
        # save applicant
        form.instance.associate = self.request.user
        form.save()
        return super().form_valid(form)


@login_required(login_url=reverse_lazy('login'))
def hire_associate(request, application_id=None):
    # try:
    associate = Application.objects.get(id=application_id)
    associate.is_hired = True
    associate.save()
    messages.success(request, f'Hiring Successfully. Associate will be notified. Thank you!')
    # except IntegrityError as e:
    #     print(e.message)
    #     return HttpResponseRedirect(reverse_lazy('profile_fellow'))
    # return HttpResponseRedirect(reverse_lazy('profile_fellow'))
    return redirect('hire_associate_detail', application_id=application_id)



@login_required(login_url=reverse_lazy('login'))
def reject_associate(request, application_id=None):
    # try:
    associate = Application.objects.get(id=application_id)
    associate.rejected = True
    associate.save()
    messages.success(request, f'Associate will be notified. Thank you!')
    # except IntegrityError as e:
    #     print(e.message)
    #     return HttpResponseRedirect(reverse_lazy('profile_fellow'))
    # return HttpResponseRedirect(reverse_lazy('profile_fellow'))
    return redirect('hire_associate_detail', application_id=application_id)


class ApplicantPerJobView(ListView):
    model = Application
    template_name = 'users/post_applications.html'
    context_object_name = 'applications'
    paginate_by = 3

    @method_decorator(login_required(login_url=reverse_lazy('login')))
    # @method_decorator(user_is_fellow)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self.request, *args, **kwargs)

    def get_queryset(self):
        return Application.objects.filter(post_id=self.kwargs['post_id']).order_by('id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = Post.objects.get(id=self.kwargs['post_id'])
        return context


@login_required(login_url=reverse_lazy('login'))
def filled(request, post_id=None):
    try:
        post = Post.objects.get(fellow_id=request.user.id, id=post_id)
        post.filled = True
        post.save()
    except IntegrityError as e:
        print(e.message)
        return HttpResponseRedirect(reverse_lazy('profile_fellow'))
    return HttpResponseRedirect(reverse_lazy('profile_fellow'))


@login_required(login_url=reverse_lazy('login'))
def recall(request, application_id=None):
    associate = Application.objects.get(id=application_id)
    associate.recall = True
    associate.save()
    messages.success(request, f'Noted. Associate would be notified. Thank you!')
    return redirect('hire_associate_detail', application_id=application_id)

class ApplicantDetailView(DetailView):
    model = Application
    template_name = 'users/hire_associate_detail.html'
    pk_url_kwarg = 'application_id'

    def get_object(self, queryset=None):
        obj = super(ApplicantDetailView, self).get_object(queryset=queryset)
        if obj is None:
            raise Http404("Associate doesn't exists")
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        application = Application.objects.get(id=self.kwargs['application_id'])
        context['application'] = application
        context['rating'] = application.associate.profileassociate.associate_avg_rating

        now = datetime.now()
        if application.post.start_date <= now.date() and application.post.end_date >= now.date() :
            context['job_started'] = True
        elif application.post.end_date < now.date() :
            context['job_completed'] = True
        return context


class AssociateApplicationListView(ListView):
    model = Application
    template_name = 'users/associate_dashboard.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'applications'
    # paginate_by = 3

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self.request, *args, **kwargs)

    def get_queryset(self):
        # return Applicants.objects.filter(user=self.request.user)
        # associate = get_object_or_404(User, username=self.kwargs.get('username'))
        return Application.objects.filter(associate=self.request.user).order_by('-created_at')


class FellowApplicationListView(ListView):
    model = Post
    template_name = 'users/fellow_dashboard.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'logged_in_fellow_posts'
    # paginate_by = 3

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self.request, *args, **kwargs)

    def get_queryset(self):
        # return Applicants.objects.filter(user=self.request.user)
        # associate = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(fellow=self.request.user).order_by('-post_date')





@login_required(login_url=reverse_lazy('login'))
def associate_rating(request, application_id=None):
    if request.method == 'POST':
        form = AssociateRateForm(request.POST)
        if form.is_valid():
            application = Application.objects.get(id=application_id)
            application.associate_rating = form.cleaned_data['associate_rating']
            application.associate_comment = form.cleaned_data['associate_comment']
            application.associate_is_rated = True
            application.save()

            total_applications = Application.objects.count()
            associate = application.associate
            j = 0
            avg = 0
            i_d = 0
            for i in range(total_applications):
                i_d+=1
                application = Application.objects.get(id=i_d)
                if application.associate == associate and application.associate_is_rated == True:
                    avg+=application.associate_rating
                    j+=1
            application = Application.objects.get(id=application_id)
            application.associate.profileassociate.associate_avg_rating = avg/j
            application.associate.profileassociate.save()

            messages.success(request, f'Your review has been submitted. Thank you!')
            return redirect('hire_associate_detail', application_id=application_id)
        else:
            form = AssociateRateForm(request.POST)
    return redirect('hire_associate_detail', application_id=application_id)



class ApplicationDetailView(DetailView):
    model = Application
    template_name = 'users/application_detail.html'
    context_object_name = 'application'
    pk_url_kwarg = 'application_id'

    def get_object(self, queryset=None):
        obj = super(ApplicationDetailView, self).get_object(queryset=queryset)
        if obj is None:
            raise Http404("Application doesn't exist")
        return obj

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            # raise error
            raise Http404("Application doesn't exist")
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        objec = Application.objects.get(id=self.kwargs['application_id'])
        context['reviewer'] = Application.objects.filter(id=self.kwargs['application_id'])
        context['rating'] = objec.post.fellow.profilefellow.fellow_avg_rating

        now = datetime.now()
        if objec.post.end_date < now.date() :
            context['job_done'] = True

        return context


@login_required(login_url=reverse_lazy('login'))
def fellow_rating(request, application_id=None):
    if request.method == 'POST':
        form = FellowRateForm(request.POST)
        if form.is_valid():
            application = Application.objects.get(id=application_id)
            application.fellow_rating = form.cleaned_data['fellow_rating']
            application.fellow_comment = form.cleaned_data['fellow_comment']
            application.fellow_is_rated = True
            application.save()

            total_applications = Application.objects.count()
            fellow = application.post.fellow
            j = 0
            avg = 0
            i_d = 0
            for i in range(total_applications):
                i_d+=1
                application = Application.objects.get(id=i_d)
                if application.post.fellow == fellow and application.fellow_is_rated == True:
                    avg+=application.fellow_rating
                    j+=1
            application = Application.objects.get(id=application_id)
            application.post.fellow.profilefellow.fellow_avg_rating = avg/j
            application.post.fellow.profilefellow.save()

            messages.success(request, f'Your review has been submitted. Thank you!')
            return redirect('application_detail', application_id=application_id)
        else:
            form = FellowRateForm(request.POST)
    return redirect('application_detail', application_id=application_id)


@login_required(login_url=reverse_lazy('login'))
def fellows_complaint(request, application_id=None):
    if request.method == 'POST':
        form = FellowsComplaintForm(request.POST)
        if form.is_valid():
            application = Application.objects.get(id=application_id)
            application.fellows_complaint_subject = form.cleaned_data['fellows_complaint_subject']
            application.fellows_complaint = form.cleaned_data['fellows_complaint']
            application.fellow_complained = True
            application.save()
            
            messages.success(request, f'Your feedback has been submitted. Partshala would contact you soon. Thank you!')
            return redirect('hire_associate_detail', application_id=application_id)
        else:
            form = FellowsComplaintForm(request.POST)
    return redirect('hire_associate_detail', application_id=application_id)


@login_required(login_url=reverse_lazy('login'))
def associates_complaint(request, application_id=None):
    if request.method == 'POST':
        form = AssociatesComplaintForm(request.POST)
        if form.is_valid():
            application = Application.objects.get(id=application_id)
            application.associates_complaint_subject = form.cleaned_data['associates_complaint_subject']
            application.associates_complaint = form.cleaned_data['associates_complaint']
            application.associate_complained = True
            application.save()
            
            messages.success(request, f'Your feedback has been submitted. Partshala would contact you soon. Thank you!')
            return redirect('application_detail', application_id=application_id)
        else:
            form = AssociatesComplaintForm(request.POST)
    return redirect('application_detail', application_id=application_id)



@login_required(login_url=reverse_lazy('login'))
def fellows_complaint_update(request, application_id=None):
    # try:
    obj = Application.objects.get(id=application_id)
    obj.fellows_complaint_resolved = False
    obj.fellows_complaint_updating = True
    obj.save()
    return redirect('hire_associate_detail', application_id=application_id)


@login_required(login_url=reverse_lazy('login'))
def fellows_complaint_updated(request, application_id=None):
    if request.method == 'POST':
        form = FellowsComplaintForm(request.POST)
        if form.is_valid():
            application = Application.objects.get(id=application_id)
            application.fellows_complaint_subject = form.cleaned_data['fellows_complaint_subject']
            application.fellows_complaint = form.cleaned_data['fellows_complaint']
            application.fellow_complained = True
            application.fellows_complaint_updating = False
            application.save()
            
            messages.success(request, f'Your feedback has been submitted. Partshala would contact you soon. Thank you!')
            return redirect('hire_associate_detail', application_id=application_id)
        else:
            form = FellowsComplaintForm(request.POST)
    return redirect('hire_associate_detail', application_id=application_id)



@login_required(login_url=reverse_lazy('login'))
def associates_complaint_update(request, application_id=None):
    # try:
    obj = Application.objects.get(id=application_id)
    obj.associates_complaint_resolved = False
    obj.associates_complaint_updating = True
    obj.save()
    return redirect('application_detail', application_id=application_id)


@login_required(login_url=reverse_lazy('login'))
def associates_complaint_updated(request, application_id=None):
    if request.method == 'POST':
        form = AssociatesComplaintForm(request.POST)
        if form.is_valid():
            application = Application.objects.get(id=application_id)
            application.associates_complaint_subject = form.cleaned_data['associates_complaint_subject']
            application.associates_complaint = form.cleaned_data['associates_complaint']
            application.associate_complained = True
            application.associates_complaint_updating = False
            application.save()
            
            messages.success(request, f'Your feedback has been submitted. Partshala would contact you soon. Thank you!')
            return redirect('application_detail', application_id=application_id)
        else:
            form = AssociatesComplaintForm(request.POST)
    return redirect('application_detail', application_id=application_id)


def ssc_marksheet(request, application_id=None):
    application = Application.objects.get(id=application_id)

    context = {
        'application': application
    }

    return render(request, 'users/ssc_marksheet.html', context)


def hsc_marksheet(request, application_id=None):
    application = Application.objects.get(id=application_id)

    context = {
        'application': application
    }

    return render(request, 'users/hsc_marksheet.html', context)


def dl_copy(request, application_id=None):
    application = Application.objects.get(id=application_id)

    context = {
        'application': application
    }

    return render(request, 'users/dl_copy.html', context)


class AssociateJobListView(ListView):
    model = Application
    template_name = 'users/associate_record.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'application'
    pk_url_kwarg = 'application_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        application = Application.objects.get(id=self.kwargs['application_id'])
        context['application'] = application
        objec = Application.objects.get(id=self.kwargs['application_id'])
        associate = objec.associate
        context['jobs'] = Application.objects.filter(associate=associate).order_by('-created_at')
        return context


class RecruitmentHistoryListView(ListView):
    model = Post
    template_name = 'users/recruitment_history.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    # paginate_by = 3

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self.request, *args, **kwargs)

    def get_queryset(self):
        return Post.objects.filter(fellow=self.request.user).order_by('-post_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = datetime.now().date()
        return context
