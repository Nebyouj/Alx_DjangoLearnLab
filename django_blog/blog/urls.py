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
from .views import add_comment, edit_comment, delete_comment


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
        path('post/<int:post_id>/comment/new/', add_comment, name='add_comment'),
    path('comment/<int:comment_id>/edit/', edit_comment, name='edit_comment'),
    path('comment/<int:comment_id>/delete/', delete_comment, name='delete_comment'),
]