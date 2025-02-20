from django.urls import path, include, re_path

# normal views
from . import views
# endpoint views
from .views import (
    TaskListApiView,
)

urlpatterns = [
    path("", views.index, name="index"),
    path('api', TaskListApiView.as_view()),
]