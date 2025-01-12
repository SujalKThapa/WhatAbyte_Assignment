from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import PasswordResetForm


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Required. Enter a valid email address.")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

def logoutView(request):
    logout(request)
    return redirect('/accounts/login')


@login_required
def send_reset_email(request):
    error_message = None
    success_message = None
    if request.method == "POST":
        email = request.POST.get("email")
        user = User.objects.filter(email=email).first()
        if user:
            # Logic to send the password reset email
            reset_link = f"http://example.com/reset-password/{user.pk}/"  # Replace with actual password reset logic
            send_mail(
                "Password Reset Request",
                f"Click the link to reset your password: {reset_link}",
                settings.DEFAULT_FROM_EMAIL,
                [email],
            )
            success_message = "A password reset email has been sent!"
        else:
            error_message = "Email not found in our database."

    return render(request, "resetPassword/enterMail.html", {
        "error_message": error_message,
        "success_message": success_message,
    })

@login_required
def homeView(request):
    return render(request, "home.html", {})

def authView(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('/accounts/login')  # Redirect to login after successful signup
    else:
        form = CustomUserCreationForm()
    return render(request, "registration/signup.html", {"form": form})


def resetView(request):
    return render(request, "resetPassword/enterMail.html", {})

def resetSentView(request):
    return render(request, "resetPassword/mailSent.html",{})