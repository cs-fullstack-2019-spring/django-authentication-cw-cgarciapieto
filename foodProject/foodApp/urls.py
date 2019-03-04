from django.urls import path

from . import views

urlpatterns = [
    path('', views.newForm, name='newForm'),
    path('posted/', views.newpost, name='newpost'),

]