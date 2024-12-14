from django.urls import path
from .views import UserLoginSerializer,UserRegistrationSerializer, ProfileView

urlpatterns = [
    path('register/', UserRegistrationSerializer.as_view(), name='register'),
    path('login/', UserLoginSerializer.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
]
