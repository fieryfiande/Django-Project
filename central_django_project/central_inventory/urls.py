from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    #path('central/',views.site_list, name="central"),
    path('sites/',views.site_list.as_view())
]
