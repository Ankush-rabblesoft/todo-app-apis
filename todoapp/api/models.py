
from django.db import models
from django.utils import timezone


class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=2550)
    phone = models.BigIntegerField()
    password = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class TaskCategory(models.Model):
    category = models.CharField(max_length=255)
    user = models.ForeignKey(User, default=None,on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.category

class TaskPriority(models.Model):
    type = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.type

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=2550)
    time = models.DateTimeField()
    user = models.ForeignKey(User, default=None,on_delete=models.CASCADE)
    category = models.ForeignKey(TaskCategory, null=True, on_delete= models.SET_NULL)
    priority = models.ForeignKey(TaskPriority, null=True, on_delete= models.SET_NULL)
    tag = models.TextField(max_length=255, null=True)
    pin_status = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
