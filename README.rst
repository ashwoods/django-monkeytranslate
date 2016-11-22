
Django monkey patch translate
=============================

Small utility app for monkeypatching Django do_translate functions.
It enables you to easily mark translations by wrapping them in curly braces,
or do more funky stuff like override how static translations are 
handled completely.


Install
-------

Install into your python environment of choice using pip from
the parent folder:

    pip install django-monkeytranslate


Settings
--------

In your settings file include:

    MONKEYTRANSLATE_ENABLED = True

And if you want to define the callable:

    MONKEYTRANSLATE_CALLABLE = callable


Take a look at monkeytranslate.utils for an example of a callable to
 monkeypatch `django.utils.translation.trans_real.do_translate`

