from django.shortcuts import render, redirect

from local_storage.forms import UploadModelForm
from local_storage.models import Photo
import os

from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.http import require_POST


def index(request):
    form = UploadModelForm()
    if request.method == "POST":
        form = UploadModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/local/uploads/")
    photos = Photo.objects.all()  # 查詢所有資料
    context = {"photos": photos, "form": form}
    return render(request, "photos/index.html", context)
