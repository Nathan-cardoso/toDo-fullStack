from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4
from django.contrib.auth.models import User
from django.db.models import OneToOneField

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    concluded = models.BooleanField(default=False)


    class Meta:
        ordering = ['-created_at']


    def __str__(self):
        return self.title
    


class Profile(AbstractUser):
    uuid = models.UUIDField(primary_key=True,default=uuid4(), editable=False, unique=True)
    tasks = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='tasks', null=True, blank=True)
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'users'
    

    def __str__(self):
        return self.first_name





