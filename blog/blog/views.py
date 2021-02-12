from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponse
from django.urls import reverse
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic.edit import FormView
from rest_framework.viewsets import ModelViewSet

from blog.forms import AnyPasswordUserCreationForm
from blog.forms import PostForm
from blog.models import Post
from blog.serializers import PostSerializer


class SignupView(FormView):
    form_class = AnyPasswordUserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form) -> HttpResponse:
        form.save()
        username = form.cleaned_data.get("username")
        raw_password = form.cleaned_data.get("password1")
        user = authenticate(username=username, password=raw_password)
        login(self.request, user)
        return super().form_valid(form)


class PublicHomeList(ListView):
    queryset = Post.objects.all()
    ordering = ["-create_time"]
    template_name = "blog/public_home.html"
    context_object_name = "posts"


class HomeList(LoginRequiredMixin, ListView):
    queryset = Post.objects.all()
    ordering = ["-create_time"]
    template_name = "blog/home.html"
    context_object_name = "posts"


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    ordering = ["-create_time"]
    serializer_class = PostSerializer


class PostsList(ListView):
    queryset = Post.objects.all()
    ordering = ["-create_time"]
    template_name = "blog/posts_list.html"
    context_object_name = "posts"


class PostsDetail(DetailView):
    queryset = Post.objects.all()
    template_name = "blog/posts_detail.html"
    context_object_name = "post"


class PostsCompose(LoginRequiredMixin, FormView):
    form_class = PostForm
    template_name = "blog/posts_compose.html"
    success_url = reverse_lazy("posts-detail")

    def form_valid(self, form) -> HttpResponse:
        form.save()
        self.post_pk = form.instance.id
        return super().form_valid(form)

    def get_success_url(self) -> str:
        return reverse("posts-detail", kwargs={"pk": self.post_pk})
