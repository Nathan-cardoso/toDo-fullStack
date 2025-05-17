from django.db import models
from django.contrib.auth.models import AbstractUser

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    concluded = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Customer(AbstractUser):
    email = models.EmailField(unique=True)
    tasks = models.ForeignKey(Task, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.username