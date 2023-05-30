from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ("email", "password1", "password2")  # replace "username" with "email"

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if self._meta.model.objects.filter(email=email).exists():
            raise forms.ValidationError("This email already exists.")
        return email
