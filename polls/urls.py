from django.urls import path
from . import views

#Creating URL Patterns To Call App View's

urlpatterns = [
    path('', views.index, name="index"),
] 