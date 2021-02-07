from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader

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
