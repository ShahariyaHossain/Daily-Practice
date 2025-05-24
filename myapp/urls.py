from django.contrib import admin
from django.urls import path, re_path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', TemplateView.as_view(template_name='index.html'), name='home'),
    path('temp/', TemplateView.as_view(template_name = 'temp.html'), name='temp'),
    path('circle/', TemplateView.as_view(template_name='circle.html'), name='circle'),
    path('signup/', TemplateView.as_view(template_name='signup.html'), name='signup'),
    path('login/', TemplateView.as_view(template_name='login.html'), name='login'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('news-list/', views.news_list, name='news-list'),
    path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),
    path('shop/', TemplateView.as_view(template_name='shop.html'), name='product-list'),
    path('cart/', TemplateView.as_view(template_name='cart.html'), name='cart'),
    path('window/', TemplateView.as_view(template_name='window-manager.html'), name='window'),
        
]
