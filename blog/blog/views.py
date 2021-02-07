from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import redirect

from blog.forms import AnyPasswordUserCreationForm
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
