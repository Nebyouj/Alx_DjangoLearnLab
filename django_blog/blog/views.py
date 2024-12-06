from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.views import LoginView,LogoutView
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save,sender=User)
def create_or_update_user_profile(sender,instance,created,**kwargs):
    if created:
        profile.objects.create(user = instance)
    instance.profile.save()

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/register.html', {'form':form})

@login_required
def profile(requests):
    return render(requests, 'blog/profile.html')


def home(request):
    posts = Post.objects.all().order_by('-published_date')
    return render(request, 'blog/home.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post.html', {'post': post})


