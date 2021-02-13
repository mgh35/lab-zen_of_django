from django.contrib.auth.models import User
from django.db.models import Q
from django.db.models import QuerySet

from blog.models import Post


def all_permissioned_posts(user: User) -> QuerySet:
    if user.is_authenticated:
        user_filter = Q(is_public=True) | Q(author=user)
    else:
        user_filter = Q(is_public=True)
    return Post.objects.filter(user_filter)
