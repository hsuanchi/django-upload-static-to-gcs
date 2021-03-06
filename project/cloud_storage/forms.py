from django import forms
from cloud_storage.models import Photo


class UploadModelForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ("image",)
        widgets = {"image": forms.FileInput(attrs={"class": "form-control-file"})}
