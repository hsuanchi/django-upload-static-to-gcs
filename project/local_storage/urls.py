from django.urls import include, path
from local_storage import views

urlpatterns = [
    path("uploads/", views.index),
]
