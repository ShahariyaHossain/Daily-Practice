from django.contrib import admin
from django.urls import path, re_path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', TemplateView.as_view(template_name='index.html'), name='home'),
]
