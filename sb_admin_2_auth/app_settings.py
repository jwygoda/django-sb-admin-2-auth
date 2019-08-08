"""
Based on allauth.account.appsettings
"""
# Ugly? Guido recommends this himself ...
# http://mail.python.org/pipermail/python-ideas/2012-May/014969.html
import sys  # noqa

from allauth.account import app_settings


class AppSettings(type(app_settings)):
    @property
    def NAME_REQUIRED(self):
        return self._setting("NAME_REQUIRED", False)

    @property
    def FIRST_NAME_MIN_LENGTH(self):
        return self._setting("FIRST_NAME_MIN_LENGTH", 1)

    @property
    def LAST_NAME_MIN_LENGTH(self):
        return self._setting("LAST_NAME_MIN_LENGTH", 1)


app_settings = AppSettings("ACCOUNT_")
app_settings.__name__ = __name__
sys.modules[__name__] = app_settings
