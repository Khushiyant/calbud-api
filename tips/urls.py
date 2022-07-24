from xml.etree.ElementInclude import include
from django.urls import path, include
from tips import views

urlpatterns = [
    path('tip', views.tips)
]