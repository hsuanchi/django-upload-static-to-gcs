from django.db import models


class Photo(models.Model):
    image = models.ImageField(upload_to="image/", blank=False, null=False)
    upload_date = models.DateTimeField(auto_now_add=True)
