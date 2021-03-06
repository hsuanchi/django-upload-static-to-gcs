from django.db import models

# Create your models here.
from storages.backends.gcloud import GoogleCloudStorage

storage = GoogleCloudStorage()


def logo_upload_to(file, filename):
    try:
        target_path = "/images/" + filename
        path = storage.save(target_path, file.image)
        return path

    except Exception as e:
        print("Failed to upload!")


class Photo(models.Model):
    image = models.ImageField(upload_to=logo_upload_to, blank=False, null=False)
    upload_date = models.DateTimeField(auto_now_add=True)
