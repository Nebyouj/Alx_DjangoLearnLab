from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('login/', LoginView.as_view(template_name = 'blog/login.html'), name = 'login'),
    path('logout/', LogoutView.as_view(next_page = '/'), name = 'logout'),
    path('register/', views.register, name = 'register'),
    path('profile/', views.profile, name= 'profile'),
    path('home/', views.home, name='home'),
    path('post/<int:pk>/', views.post_detail, name='post'),
]