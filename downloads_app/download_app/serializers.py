from .models import FileUpload
from rest_framework import serializers


class FileUploadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FileUpload
        fields = ['title', 'file']
