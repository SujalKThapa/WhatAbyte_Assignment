from tkinter.font import names

from django.urls import path, include
from .views import authView, homeView, logoutView

urlpatterns = [
    path("",homeView,name="home"),
    path('accounts/logout/', logoutView, name='logout'),
    path("signup/", authView, name="authView"),
    path("accounts/", include("django.contrib.auth.urls")),
]