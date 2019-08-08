from allauth.account.forms import SignupForm as BaseSignupForm
from django import forms
from django.utils.translation import gettext_lazy as _

from . import app_settings


class SignupForm(BaseSignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if app_settings.NAME_REQUIRED:
            self.fields["first_name"] = forms.CharField(
                label=_("First name"),
                min_length=app_settings.FIRST_NAME_MIN_LENGTH,
                widget=forms.TextInput(
                    attrs={"placeholder": _("First name"), "autofocus": "autofocus"}
                ),
            )
            self.fields["last_name"] = forms.CharField(
                label=_("Last name"),
                min_length=app_settings.LAST_NAME_MIN_LENGTH,
                widget=forms.TextInput(attrs={"placeholder": _("Last name")}),
            )
