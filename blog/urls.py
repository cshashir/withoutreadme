from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView
from . import views

# app_name = "blog"

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('jobs/', PostListView.as_view(), name='jobs'),
    path('fellow/<str:username>/', UserPostListView.as_view(), name='fellow-posts'),
    path('post/<int:id>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='about'),
    path('career/', views.career, name='career'),
    path('contactus/', views.contactus, name='contactus'),
    path('faqs/', views.faqs, name='faqs'),
]
