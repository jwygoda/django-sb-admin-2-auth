# django-sb-admin-2-auth

django-sb-admin-2-auth is a theme for [django-allauth](https://github.com/pennersr/django-allauth/) based on [startbootstrap-sb-admin-2
](https://github.com/BlackrockDigital/startbootstrap-sb-admin-2)

## Installation

Go through https://django-allauth.readthedocs.io/en/latest/installation.html.

Add sb_admin_2_auth urls instead of allauth's:

```python
urlpatterns = [
    ...
    path('accounts/', include('sb_admin_2_auth.urls')),
    ...
]
```

## Configuration

For allauth settings see https://django-allauth.readthedocs.io/en/latest/configuration.html.

Additional settings:

**ACCOUNT_NAME_REQUIRED (=False)**

The user is required to hand over a first and last name when signing up.

**ACCOUNT_FIRST_NAME_MIN_LENGTH (=1)**

An integer specifying the minimum allowed length of a first name.

**ACCOUNT_LAST_NAME_MIN_LENGTH (=1)**

An integer specifying the minimum allowed length of a last name.

## Providers

Social accounts are not being currently supported.