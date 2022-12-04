from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name='list-vendors'),
    path('add/', views.add, name="add-vendor"),    
    path('update/<uuid:pk>', views.update, name="update-vendor"),
    path('delete/<uuid:pk>', views.delete, name='delete-vendor'),
]