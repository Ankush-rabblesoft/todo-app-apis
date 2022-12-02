from django.contrib import admin

from api.models import User, Task, TaskCategory, TaskPriority

# Register your models here.
admin.site.register(User)
admin.site.register(Task)
admin.site.register(TaskCategory)
admin.site.register(TaskPriority)
