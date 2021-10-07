from django.contrib import admin
from django.urls import path, include
from .views import FileUploadView


urlpatterns = [path('upload/', FileUploadView.as_view())]
