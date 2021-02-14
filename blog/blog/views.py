from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.http.response import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.renderers import JSONRenderer
from rest_framework.viewsets import ModelViewSet
from typing import List
from blog.filters import PostFilter

from blog.forms import AnyPasswordUserCreationForm
from blog.forms import PostForm
from blog.models import Post
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


class PublicHomeList(TemplateView):
    template_name = "blog/public_home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_list"] = PostFilter().qs.order_by("-create_time")[:10]
        return context


class HomeList(LoginRequiredMixin, TemplateView):
    template_name = "blog/home.html"


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    filterset_class = PostFilter
    serializer_class = PostSerializer
    renderer_classes = [ModelTemplateHTMLRenderer, JSONRenderer]
    permission_classes = [IsAuthenticatedOrReadOnly]
    ordering = ["-create_time"]

    def get_template_names(self) -> List[str]:
        if self.detail:
            return ["blog/posts_detail.html"]
        else:
            return ["blog/posts_list.html"]

    @action(detail=False, methods=["GET", "POST"], permission_classes=[IsAuthenticated])
    def compose(self, request):
        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.save()
                self.post_pk = form.instance.id
                return HttpResponseRedirect(
                    reverse("post-detail", kwargs={"pk": self.post_pk})
                )
        else:
            form = PostForm()

        return render(request, "blog/posts_compose.html", {"form": form})
