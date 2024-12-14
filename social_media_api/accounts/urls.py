from django.urls import path
from .views import FollowUserView, UnfollowUserView, UserLoginSerializer,UserRegistrationSerializer, ProfileView

urlpatterns = [
    path('register/', UserRegistrationSerializer.as_view(), name='register'),
    path('login/', UserLoginSerializer.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
     path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow-user'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow-user'),
]
