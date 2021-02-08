from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import redirect

from blog.forms import AnyPasswordUserCreationForm
from blog.forms import PostForm
from blog.models import Post


def signup(request):
    if request.method == "POST":
        form = AnyPasswordUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect("home")
    else:
        form = AnyPasswordUserCreationForm()
    return render(request, "registration/signup.html", {"form": form})


def public_home(request):
    return render(
        request,
        "blog/public_home.html",
        {"posts": Post.objects.order_by("-create_time")[:10]},
    )


@login_required
def home(request):
    return render(request, "blog/home.html", {})


def posts_detail(request, post_id):
    return render(
        request, "blog/posts_list.html", {"posts": [Post.objects.get(id=post_id)]}
    )


@login_required
def posts_compose(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            breakpoint()
            return redirect("posts-detail", post_id=form.instance.id)
    else:
        form = PostForm()
    return render(request, "blog/posts_create.html", {"form": form})
