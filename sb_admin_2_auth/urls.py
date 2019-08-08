from django.urls import path, re_path

from . import views

urlpatterns = [
    path("signup/", views.SignupView.as_view(), name="account_signup"),
    path("login/", views.LoginView.as_view(), name="account_login"),
    path("logout/", views.LogoutView.as_view(), name="account_logout"),
    path(
        "confirm-email/",
        views.EmailVerificationSentView.as_view(),
        name="account_email_verification_sent",
    ),
    re_path(
        r"^confirm-email/(?P<key>[-:\w]+)/$",
        views.ConfirmEmailView.as_view(),
        name="account_confirm_email",
    ),
    path(
        "password/reset/",
        views.PasswordResetView.as_view(),
        name="account_reset_password",
    ),
    path(
        "password/reset/done/",
        views.PasswordResetDoneView.as_view(),
        name="account_reset_password_done",
    ),
    re_path(
        r"password/reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$",
        views.PasswordResetFromKeyView.as_view(),
        name="account_reset_password_from_key",
    ),
    path(
        "password/reset/key/done/",
        views.PasswordResetFromKeyDoneView.as_view(),
        name="account_reset_password_from_key_done",
    ),
]
