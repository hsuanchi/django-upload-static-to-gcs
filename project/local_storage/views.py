from django.shortcuts import render, redirect

from local_storage.forms import UploadModelForm
from local_storage.models import Photo
import os

from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.http import require_POST


# def upload_file(request):
#     if request.method == "POST":
#         save_path = os.path.join(settings.MEDIA_ROOT, "uploads", request.FILES["file"])
#         path = default_storage.save(save_path, request.FILES["file"])
#         document = Document.objects.create(document=path, upload_by=request.user)
#         return JsonResponse({"document": document.id})


def index(request):
    photos = Photo.objects.all()  # 查詢所有資料
    form = UploadModelForm()
    if request.method == "POST":
        form = UploadModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/local/uploads/")
    context = {"photos": photos, "form": form}
    return render(request, "photos/index.html", context)
