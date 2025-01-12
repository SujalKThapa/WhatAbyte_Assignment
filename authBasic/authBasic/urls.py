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
    path('password-change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change_form.html'), name='password_change'),
    path('password-change-done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), name='password_change_done'),
    # Main app URLs
    path('', include(("mainApp.urls", "mainApp"), "mainApp")),
] + static(settings.STATIC_URL)
