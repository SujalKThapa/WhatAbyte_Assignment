from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import homeView, authView, logoutView

urlpatterns = [
    # Custom views
    path("", homeView, name="home"),
    path("signup/", authView, name="authView"),
    path("accounts/logout/", logoutView, name="logout"),
    path("accounts/", include("django.contrib.auth.urls")),
]
