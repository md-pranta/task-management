from django.urls import path,include
from .views import *
urlpatterns = [
    path('add/', add_category, name='add_category'),
]