from django.urls import path
from . import views

urlpatterns = [
    # URL for viewing a post
    path('post/<int:id>/', views.view_post, name='view_post'),
    
    # URL for creating a new post
    path('post/create/', views.create_post, name='create_post'),
    
    # URL for editing an existing post
    path('post/edit/<int:id>/', views.edit_post, name='edit_post'),
    
    # URL for deleting a post
    path('post/delete/<int:id>/', views.delete_post, name='delete_post'),
    
    # URL for listing all posts (optional, if needed)
    path('posts/', views.post_list, name='post_list'),
]
