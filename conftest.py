__author__ = 'Alain Ivars'


def pytest_configure(config):
    from django.conf import settings
    if not settings.configured:
        from example import settings_tests as test_settings

        settings.configure(**test_settings.__dict__)

    if not hasattr(settings, 'CACHES'):  # pragma: no cover
        settings.CACHES = {
            'default': {
                'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
            }
        }
    # settings.SITE_NAME = 'contact_form_bootstrap'
    import django
    django.setup()

