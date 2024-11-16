from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, BaseUserManager



class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, username, password, **extra_fields)

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(default=timezone.now)
    profile_photo = models.ImageField(upload_to='profile_pics/')
    
    objects = CustomUserManager()  # Set the custom manager

    def __str__(self):
        return self.username


# Create your models here.
class Book(models.Model):
    STATUS_CHOICES = [
        ('a', 'Available'),
        ('o', 'On loan'),
        ('r', 'Reserved'),
        ('m', 'Maintenance'),
    ]
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    Due_back = models.DateField(default=timezone.now)
    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        blank=True,
        default='m',
        help_text='Book availiability'
    )

    def __str__(self):
        return f"{self.title} by {self.author}"
