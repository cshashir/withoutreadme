from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import Http404, HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.conf import settings
from users.models import User


# def home(request):
#     context = {
#         'posts': Post.objects.all()
#     }
#     return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-post_date']
    paginate_by = 3


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/fellow_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 3

    def get_queryset(self):
        fellow = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(fellow=fellow).order_by('-post_date')


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
    pk_url_kwarg = 'id'

    def get_object(self, queryset=None):
        obj = super(PostDetailView, self).get_object(queryset=queryset)
        if obj is None:
            raise Http404("Job doesn't exist")
        return obj

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            # raise error
            raise Http404("Job doesn't exist")
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['job_title', 'job_description', 'start_date', 'end_date', 'start_time', 'end_time', 'skills_reqd', 'vacancy', 'stipend', 'city', 'address']

    def form_valid(self, form):
        form.instance.fellow = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['job_title', 'job_description', 'start_date', 'end_date', 'start_time', 'end_time', 'skills_reqd', 'vacancy', 'stipend', 'city', 'address']

    def form_valid(self, form):
        form.instance.fellow = self.request.user
        messages.info(self.request, 'Successfully updated the job!')
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.fellow:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.fellow:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {' title': 'About'})


def career(request):
    return render(request, 'blog/career.html', {' title': 'Career'})


def contactus(request):
    return render(request, 'blog/contactus.html', {' title': 'Contact us'})


def faqs(request):
    return render(request, 'blog/faqs.html', {' title': 'FAQs'})
