from django.contrib import admin
from django.urls import include
from django.urls import path

from blog import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", views.public_home, name="public-home"),
    path("home/", views.home, name="home"),
]
