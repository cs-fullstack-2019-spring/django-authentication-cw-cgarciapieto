from django.urls import path

from . import views

urlpatterns = [
    path('', views.newForm, name='newForm'),
    path('posted/', views.newPost, name='newpost'),

]