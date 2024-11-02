from django.db import models
from django.utils import timezone

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
