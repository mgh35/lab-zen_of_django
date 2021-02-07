from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.template import loader

from blog.forms import AnyPasswordUserCreationForm
from blog.models import Post


def public_home(request):
    template = loader.get_template("blog/public_home.html")
    context = {"posts": Post.objects.order_by("-create_time")[:10]}
    return HttpResponse(template.render(context, request))


@login_required
def home(request):
    template = loader.get_template("blog/home.html")
    context = {}
    return HttpResponse(template.render(context, request))


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
