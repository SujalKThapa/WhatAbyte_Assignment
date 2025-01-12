from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import CustomPasswordResetForm

urlpatterns = [
    # Admin URL
    #ath('admin/', admin.site.urls),

    # Password Reset URLs (elevated to the root level)
    path('password_reset/', auth_views.PasswordResetView.as_view(form_class=CustomPasswordResetForm), name='password_reset'),  # Use the custom form here
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    # Main app URLs
    path('', include(("mainApp.urls", "mainApp"), "mainApp")),
] + static(settings.STATIC_URL)
