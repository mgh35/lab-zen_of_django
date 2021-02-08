from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path

from blog import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/login/", auth_views.LoginView.as_view(), name="login"),
    path("accounts/logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("accounts/signup/", views.signup, name="signup"),
    path("", views.public_home, name="public-home"),
    path("home/", views.home, name="home"),
    path("posts/compose/", views.posts_compose, name="posts-compose"),
    path("posts/<int:post_id>/", views.posts_detail, name="posts-detail"),
]
