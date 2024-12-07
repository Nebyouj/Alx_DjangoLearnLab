from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)


urlpatterns = [
    path('login/', LoginView.as_view(template_name = 'blog/login.html'), name = 'login'),
    path('logout/', LogoutView.as_view(next_page = '/'), name = 'logout'),
    path('register/', views.register, name = 'register'),
    path('profile/', views.profile, name= 'profile'),
    path('home/', views.home, name='home'),
    path('post/<int:pk>/', views.post_detail, name='post'),
    path('', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
]