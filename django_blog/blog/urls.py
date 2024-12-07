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
from .views import CommentCreateView,CommentDeleteView, CommentUpdateView
from .views import search_posts, posts_by_tag

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
    path('post/<int:pk>/comments/new/', CommentCreateView, name='add_comment'),
    path('comment/<int:pk>/update/', CommentUpdateView, name='edit_comment'),
    path('comment/<int:pk>/delete/', CommentDeleteView, name='delete_comment'),
    path('search/', search_posts, name='search_posts'),
    path('tags/<slug:tag_slug>/', views.PostByTagListView.as_view(), name='posts_by_tag'),
]