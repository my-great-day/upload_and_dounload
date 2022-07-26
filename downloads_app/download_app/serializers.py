from .models import FileUpload
from rest_framework import serializers


class FileUploadDownSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FileUpload
        fields = ['title', 'file', 'date_upload_file']


class FileUploadUpSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FileUpload
        fields = ['title', 'file']
