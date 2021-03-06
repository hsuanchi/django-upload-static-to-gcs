from django.urls import include, path

from cloud_storage import views

urlpatterns = [
    path("", views.index),
]


# from .views import UploadView

# urlpatterns = [path("", UploadView.as_view(), name="upload-image")]
