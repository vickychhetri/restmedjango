from django.urls import path
from .views import Task

urlpatterns = [
    path('', Task.post()),
]
