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
    path('vicco/', admin.site.urls),
    path('register-fellow/', user_views.register_fellow, name='register_fellow'),
    path('register-associate/', user_views.register_associate, name='register_associate'),
    path('profile-fellow/', include([
        path('', user_views.profile_fellow, name='profile_fellow'),
        path('applications/<int:post_id>/', user_views.ApplicantPerJobView.as_view(), name='post_applications'),
        path('mark-filled/<int:post_id>/', user_views.filled, name='post-mark-filled'),
        path('hire-associate/<int:application_id>/', user_views.hire_associate, name='hire_associate'),
        path('hire-associate-detail/<int:application_id>/', user_views.ApplicantDetailView.as_view(), name='hire_associate_detail'),
    ])),
    path('apply-job/<int:post_id>/', user_views.ApplyJobView.as_view(), name='apply_job'),
    path('associate-rate/<int:application_id>/', user_views.associate_rating, name='associate_rating'),
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
