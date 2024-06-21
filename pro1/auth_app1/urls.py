from django.urls import path

from .views import *

urlpatterns =[
    path("lov/",logout),
    path("suv/",signview),
    path("lv/",loginview)
]