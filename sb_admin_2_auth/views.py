from allauth.account import views
from django import forms

from .forms import SignupForm


class LogoutView(views.LogoutView):
    # logout form in startbootstrap-sb-admin-2 is accessible only through the dashboard
    http_method_names = ("post",)


class SbFormView:
    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)

        # change input fields css classes after form initialization
        for _, field in form.fields.items():
            if isinstance(field, forms.BooleanField):
                css_class = "custom-control-input"
            else:
                css_class = "form-control form-control-user"
            field.widget.attrs["class"] = css_class

        return form


class LoginView(SbFormView, views.LoginView):
    template_name = "sb_admin_2/auth/login.html"


class SignupView(SbFormView, views.SignupView):
    form_class = SignupForm
    template_name = "sb_admin_2/auth/register.html"


class PasswordResetView(SbFormView, views.PasswordResetView):
    template_name = "sb_admin_2/auth/forgot_password/base.html"


class PasswordResetFromKeyView(SbFormView, views.PasswordResetFromKeyView):
    template_name = "sb_admin_2/auth/forgot_password/from_key.html"


class PasswordResetDoneView(SbFormView, views.PasswordResetDoneView):
    template_name = "sb_admin_2/auth/forgot_password/done.html"


class PasswordResetFromKeyDoneView(SbFormView, views.PasswordResetFromKeyDoneView):
    template_name = "sb_admin_2/auth/forgot_password/from_key_done.html"


class ConfirmEmailView(views.ConfirmEmailView):
    template_name = "sb_admin_2/auth/confirm-email.html"


class EmailVerificationSentView(views.EmailVerificationSentView):
    template_name = "sb_admin_2/auth/confirm-email-sent.html"
