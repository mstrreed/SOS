from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views

urlpatterns = [
    path('', views.sos_list,name='sos_list'),
    path('create/', views.sos_create,name='sos_create'),
    path('<int:sos_id>/edit/', views.sos_edit,name='sos_edit'),
    path('<int:sos_id>/delete/', views.sos_delete,name='sos_delete'),
    path('register/', views.register,name='register'),
]
