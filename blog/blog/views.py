from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import QuerySet
from django.http import HttpResponseRedirect
from django.http.response import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import FormView
from rest_framework.decorators import action
from rest_framework.renderers import JSONRenderer
from rest_framework.viewsets import ModelViewSet
from typing import List

from blog.forms import AnyPasswordUserCreationForm
from blog.forms import PostForm
from blog.models import Post
from blog.queries import all_permissioned_posts
from blog.renderers import ModelTemplateHTMLRenderer
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
    ordering = ["-create_time"]
    template_name = "blog/public_home.html"
    context_object_name = "posts"

    def get_queryset(self) -> QuerySet:
        return all_permissioned_posts(self.request.user)


class HomeList(LoginRequiredMixin, ListView):
    ordering = ["-create_time"]
    template_name = "blog/home.html"
    context_object_name = "posts"

    def get_queryset(self) -> QuerySet:
        return all_permissioned_posts(self.request.user)


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    ordering = ["-create_time"]
    serializer_class = PostSerializer
    renderer_classes = [ModelTemplateHTMLRenderer, JSONRenderer]

    def get_template_names(self) -> List[str]:
        if self.detail:
            return ["blog/posts_detail.html"]
        else:
            return ["blog/posts_list.html"]

    @action(detail=False, methods=["GET", "POST"])
    def compose(self, request):
        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                form.save()
                self.post_pk = form.instance.id
                return HttpResponseRedirect(
                    reverse("posts-detail", kwargs={"pk": self.post_pk})
                )
        else:
            form = PostForm()

        return render(request, "blog/posts_compose.html", {"form": form})
