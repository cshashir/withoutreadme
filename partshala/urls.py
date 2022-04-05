"""django_first URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static

app_name = "partshala"

urlpatterns = [
    path('oloRider/', admin.site.urls),
    path('register-fellow/', user_views.register_fellow, name='register_fellow'),
    path('register-associate/', user_views.register_associate, name='register_associate'),
    path('profile-fellow/', include([
        path('', user_views.profile_fellow, name='profile_fellow'),
        path('recruitment-history/', user_views.RecruitmentHistoryListView.as_view(), name='recruitment_history'),
        path('applications/<int:post_id>/', user_views.ApplicantPerJobView.as_view(), name='post_applications'),
        path('mark-filled/<int:post_id>/', user_views.filled, name='post-mark-filled'),
        path('hire-associate/<int:application_id>/', user_views.hire_associate, name='hire_associate'),
        path('reject-associate-associate/<int:application_id>/', user_views.reject_associate, name='reject_associate'),
        path('hire-associate-detail/<int:application_id>/', user_views.ApplicantDetailView.as_view(), name='hire_associate_detail'),
        path('hire-associate-recall/<int:application_id>/', user_views.recall, name='recall'),
        path('hire-associate-detail/<int:application_id>/ssc-marksheet/', user_views.ssc_marksheet, name='ssc_marksheet'),
        path('hire-associate-detail/<int:application_id>/hsc-marksheet/', user_views.hsc_marksheet, name='hsc_marksheet'),
        path('hire-associate-detail/<int:application_id>/driving-license/', user_views.dl_copy, name='dl_copy'),
        path('hire-associate-detail/<int:application_id>/associate-record/', user_views.AssociateJobListView.as_view(), name='associate_record'),
    ])),
    path('fellow-dashboard/', user_views.FellowApplicationListView.as_view(), name='fellow_dashboard'),
    path('apply-job/<int:post_id>/', user_views.ApplyJobView.as_view(), name='apply_job'),
    path('associate-rate/<int:application_id>/', user_views.associate_rating, name='associate_rating'),
    path('fellows-complaint/<int:application_id>/', user_views.fellows_complaint, name='fellows_complaint'),
    path('fellows-complaint-update/<int:application_id>/', user_views.fellows_complaint_update, name='fellows_complaint_update'),
    path('fellows-complaint-updated/<int:application_id>/', user_views.fellows_complaint_updated, name='fellows_complaint_updated'),
    path('associates-complaint/<int:application_id>/', user_views.associates_complaint, name='associates_complaint'),
    path('associates-complaint-update/<int:application_id>/', user_views.associates_complaint_update, name='associates_complaint_update'),
    path('associates-complaint-updated/<int:application_id>/', user_views.associates_complaint_updated, name='associates_complaint_updated'),
    path('felow-rating/<int:application_id>/', user_views.fellow_rating, name='fellow_rating'),
    path('associate-dashboard/', user_views.AssociateApplicationListView.as_view(), name='associate_dashboard'),
    path('profile-associate/', user_views.profile_associate, name='profile_associate'),
    path('login/', user_views.user_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('password-reset/confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
    path('', include('blog.urls')),
    path('application-detail/<int:application_id>/', user_views.ApplicationDetailView.as_view(), name='application_detail'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
