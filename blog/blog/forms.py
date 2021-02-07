from django import forms
from django.contrib.auth.forms import UserCreationForm


class AnyPasswordUserCreationForm(UserCreationForm):
    def _post_clean(self):
        # Skip the password validation step from UserCreationForm
        super(forms.ModelForm, self)._post_clean()
