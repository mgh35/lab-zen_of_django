from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter

from blog import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/login/", auth_views.LoginView.as_view(), name="login"),
    path("accounts/logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("accounts/signup/", views.SignupView.as_view(), name="signup"),
    path("", views.PublicHomeList.as_view(), name="public-home"),
    path("home/", views.HomeList.as_view(), name="home"),
]

router = DefaultRouter()
router.register("posts", views.PostViewSet, basename="post")
router.register("comments", views.CommentViewSet, basename="comment")

urlpatterns.append(path("", include(router.urls)))
