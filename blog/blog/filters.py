from django.db.models import Q
from django_filters import FilterSet

from blog.models import Post


class PostFilter(FilterSet):
    class Meta:
        model = Post
        fields = ["create_time", "author"]

    @property
    def qs(self):
        queryset = super().qs

        user = getattr(self.request, "user", None)
        if user and user.is_authenticated:
            user_filter = Q(is_public=True) | Q(author=user)
        else:
            user_filter = Q(is_public=True)
        queryset = queryset.filter(user_filter)

        return queryset
