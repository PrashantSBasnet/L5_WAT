from django.contrib import admin
from django.urls import path

from . import views
from .views import authorized

urlpatterns=[
    path('admin', admin.site.urls),
    path('welcome/', views.home),
]