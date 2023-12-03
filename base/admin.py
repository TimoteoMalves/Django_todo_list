from django.contrib import admin
from .models import Task

# register the model to our admin pannel
admin.site.register(Task)
