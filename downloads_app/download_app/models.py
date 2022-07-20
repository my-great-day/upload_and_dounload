from django.db import models


# Create your models here.


class FileUpload(models.Model):
    title = models.CharField(max_length=255, null=False)
    file = models.FileField(upload_to='file_uploads/')
    date_upload_file = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Upload file'

    def __str__(self):
        return self.title
