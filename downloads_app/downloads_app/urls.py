from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from download_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/looking_the_file/<pk>', views.FileUploadListAPIView.as_view()),
    path('api/v1/create_the_file/', views.FileUploadCreateAPIView.as_view()),
    path('', include('download_app.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
