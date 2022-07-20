from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from download_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', views.FileUploadAPIView.as_view()),
    path('', include('download_app.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
