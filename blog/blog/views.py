from django.http import HttpResponse
from django.template import loader

from blog.models import Post


def home(request):
    template = loader.get_template("home.html")
    context = {
        "posts": Post.objects.order_by("-create_time")[:10]
    }
    return HttpResponse(template.render(context, request))
