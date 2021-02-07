from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader

from blog.models import Post


def home(request):
    template = loader.get_template("blog/home.html")
    context = {"posts": Post.objects.order_by("-create_time")[:10]}
    return HttpResponse(template.render(context, request))


@login_required
def profile(request):
    template = loader.get_template("blog/profile.html")
    context = {}
    return HttpResponse(template.render(context, request))
