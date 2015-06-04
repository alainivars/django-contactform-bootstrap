#-*- coding: utf-8 -*-

import os

# Django settings for SiteDJ project.
from contact_form_bootstrap.settings import *

EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'

DATABASES = {
    'default': {
        'NAME': ':memory:',
        'ENGINE': 'django.db.backends.sqlite3',
        'TEST_NAME': ':memory:',
    },
}

TEST_RUNNER = 'django.test.runner.DiscoverRunner'

settings_path = os.path.abspath(os.path.dirname(__file__))

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'the-test-key'

ROOT_URLCONF = 'contact_form_bootstrap.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templatetags".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    ( os.path.join(settings_path, 'templates'), )
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'the-test-key'

# List of callables that know how to import templatetags from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.templatetags.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Allow languages to be selected
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # authentification pour toutes les page
    #'django_base_app.authentification.middleware.LoginRequiredMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.csrf",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
    # pour internationalisation d apres le tuto django du site
    # http://fr.openclassrooms.com/informatique/cours/developpez-votre-site-web-avec-le-framework-django/qu-est-ce-que-le-i18n-et-comment-s-en-servir
    "django.core.context_processors.i18n",
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',

    'crispy_forms',
    'contact_form_bootstrap',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
}

