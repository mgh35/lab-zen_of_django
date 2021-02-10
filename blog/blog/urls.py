from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path

from blog import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/login/", auth_views.LoginView.as_view(), name="login"),
    path("accounts/logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("accounts/signup/", views.SignupView.as_view(), name="signup"),
    path("", views.PublicHomeList.as_view(), name="public-home"),
    path("home/", views.HomeList.as_view(), name="home"),
    path("posts/", views.PostsList.as_view(), name="posts-list"),
    path("posts/<int:pk>/", views.PostsDetail.as_view(), name="posts-detail"),
    path("posts/compose/", views.PostsCompose.as_view(), name="posts-compose"),
]
