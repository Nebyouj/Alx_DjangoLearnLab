# views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseForbidden
from .models import Post

@permission_required('myapp.can_view', raise_exception=True)
def view_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'view_post.html', {'post': post})

@permission_required('myapp.can_create', raise_exception=True)
def create_post(request):
    if request.method == 'POST':
        # Handle form submission and create the post
        new_post = Post.objects.create(title=request.POST['title'], content=request.POST['content'])
        return redirect('post_detail', post_id=new_post.id)
    return render(request, 'create_post.html')

@permission_required('myapp.can_edit', raise_exception=True)
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        # Handle editing the post
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.save()
        return redirect('post_detail', post_id=post.id)
    return render(request, 'edit_post.html', {'post': post})

@permission_required('myapp.can_delete', raise_exception=True)
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect('post_list')
