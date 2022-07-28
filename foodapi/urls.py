from django.urls import path
from . import views

urlpatterns = [
    path("food/<str:ingr>",views.food, name="food")
]
