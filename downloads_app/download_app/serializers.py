from .models import FileUpload
from rest_framework import serializers


class FileUploadUpSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FileUpload
        fields = ['title', 'file']
