from django.contrib.auth.models import User
from django.db.models import QuerySet

from blog.models import Post


def all_permissioned_posts(user: User) -> QuerySet:
    return Post.objects.all()
