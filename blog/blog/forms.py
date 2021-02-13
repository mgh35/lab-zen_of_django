from django import forms
from django.contrib.auth.forms import UserCreationForm

from blog.models import Post


class AnyPasswordUserCreationForm(UserCreationForm):
    def _post_clean(self):
        # Skip the password validation step from UserCreationForm
        super(forms.ModelForm, self)._post_clean()


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "text", "is_public"]
