from django.contrib import admin
from django.urls import path

from . import views

urlpatterns=[
    path('admin/', admin.site.urls),
    path('home/', views.HomeView.as_view()),
    path('authorized/', views.AuthorizedView.as_view()),
]