from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.static import serve
from rest_framework.views import APIView
from rest_framework.response import Response

from download_app.forms import Form_File
from download_app.models import FileUpload


def index(request):
    if request.method == 'POST':
        file = FileUpload(title=request.POST['title'], file=request.FILES['file_upload'])
        file.save()
        return redirect('url', file=file.id)

    form = Form_File()
    return render(request, 'index.html')


def url(request, file):
    files = FileUpload.objects.get(id=file).file
    return render(request, 'url.html', {'id': files})


def url_view(request, file_uploads, file):
    path = f'{file_uploads}/{file}'
    document = get_object_or_404(FileUpload, file=path)

    if document:
        return serve(request,
                     path=path,
                     document_root=settings.MEDIA_ROOT)

    return HttpResponse('Ups, Error!')


class FileUploadAPIView(APIView):
    def post(self, request):
        return Response({'title': 'title'})

    def get(self, request):
        return Response({'title': 'Hello'})