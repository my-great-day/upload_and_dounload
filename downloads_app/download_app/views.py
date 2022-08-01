from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_protect
from django.views.static import serve
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import ModelViewSet, ViewSet

from download_app.forms import Form_File
from download_app.models import FileUpload
from download_app.serializers import FileUploadUpSerializer, FileUploadDownSerializer, FileUploadSerializer


@csrf_protect
def index(request):
    """Главный окно и форма для добавлении файла в базу данних"""
    try:
        if request.method == 'POST':
            file = FileUpload(title=request.POST['title'], file=request.FILES['file_upload'])
            file.save()  # Запись в базу данних
            return redirect('url', file=file.id)
        form = Form_File()
        return render(request, 'index.html')

    except:
        form = Form_File()
        return render(request, 'index.html')


def url(request, file):
    """Просмотр ссилки"""
    files = FileUpload.objects.get(id=file).file
    return render(request, 'url.html', {'id': files})


def url_view(request, file_uploads, file):
    """Откритие или скачивание файла"""
    path = f'{file_uploads}/{file}'
    document = get_object_or_404(FileUpload, file=path)

    if document:
        return serve(request,
                     path=path,
                     document_root=settings.MEDIA_ROOT)

    return HttpResponse('Ups, Error!')


class FileUploadCreateAPIView(CreateAPIView, ViewSet):
    """Откритие или скачивание файла"""
    queryset = FileUpload
    serializer_class = FileUploadUpSerializer
