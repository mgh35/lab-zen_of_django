from django.urls import path

from blog import views


urlpatterns = [path("", views.home), path("profile/", views.profile)]
