from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django import forms

class CustomPasswordResetForm(PasswordResetForm):
    def clean_email(self):
        email = self.cleaned_data.get("email")
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise forms.ValidationError("This email is not registered.")
        return email
