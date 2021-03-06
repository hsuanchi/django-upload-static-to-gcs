from django.shortcuts import render, redirect

# from django.views import View
# from django.http.response import HttpResponse
# from django.middleware.csrf import get_token
# from .models import logo_upload_to


# class UploadView(View):
#     def get(self, request):
#         html = """
#                 <form method="post" enctype="multipart/form-data">
#                 <input type='text' style='display:none;' value='%s' name='csrfmiddlewaretoken'/>
#                 <input type="file" name="image" accept="image/*">
#                 <button type="submit">Upload Image</button>
#                 </form>
#             """ % (
#             get_token(request)
#         )
#         return HttpResponse(html)

#     def post(self, request):
#         image = request.FILES["image"]

#         print("==================", image, image.name)
#         public_uri = logo_upload_to(image, image.name)
#         return HttpResponse("<img src='%s'/>" % (public_uri))


from cloud_storage.forms import UploadModelForm
from cloud_storage.models import Photo
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
            return redirect("/cloud")
    photos = Photo.objects.all()  # 查詢所有資料
    context = {"photos": photos, "form": form}
    return render(request, "photos_cloud/index.html", context)
