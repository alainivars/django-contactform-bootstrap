.. image:: https://api.travis-ci.org/alainivars/django-contact-form.svg?branch=master
   :target: http://travis-ci.org/alainivars/django-contact-form
   :alt: Build status

.. image:: https://coveralls.io/repos/alainivars/django-contact-form/badge.svg?branch=devel
   :target: https://coveralls.io/r/alainivars/django-contact-form?branch=devel
   :alt: Test coverage status

* An Extensible Contact Form::

    Based entirely on James Bennett's django_contact_form:
      - https://bitbucket.org/ubernostrum/django_contact_form
    Based on Aaron Madison django_contact_form:
      - https://github.com/madisona/django-contact-form
    By Alain Ivars django_contactform_bootstrap:
      - https://github.com/alainivars/django-contact-form


Features
===========================

* Functionality as a django contact form::

  - easy integration into an existing django project
  - Bootstrap 3
  - integrate geographical map
  - log (not yet finish)
  - tests and coverage
  - link to your : FACEBOOK, LINKEDIN, TWITTER, GOOGLE+

Todo
===========================

 - finish english translation and add other translations
 - improve coverage
 - improve log
 - manage display a link only if it exist
 - correct broken links in this file

Use (NOT READY TO USE)
===========================

    + Add in your setting file::

        ADMINS = (
            ('your admin name', 'contact@yourdomain.com'),
        )

        COMPANY = {
            'NAME': "my company",
            'ADDRESS': "26 streets from here th there",
            'ZIP': "1234",
            'CITY': "Maybe-there",
            'LAT': 48.81484460000001,
            'LNG': 2.0523723999999675,
            'PHONE': "+336 1234 5678",
            'EMAIL': 'contact@yourdomain.com',
            'FACEBOOK': "Maybe-there",
            'LINKEDIN': "Maybe-there",
            'TWITTER': "Maybe-there",
            'GOOGLEPLUS': "+Maybe-there",
        }

        CRISPY_TEMPLATE_PACK = 'bootstrap3'


    + Don't forget to set::

        EMAIL_HOST, EMAIL_PORT, EMAIL_HOST_USER and EMAIL_HOST_PASSWORD


    + Be sure to have::

        'homepage' defined in your url file


Documentation
===========================

.. note::
    Please note that this Project is documented poorly. If you have any questions please contact us!
    We'd love to update the documentation and answer your question!

Getting Help
===========================

Please report bugs or ask questions using the `Issue Tracker`

Check also for the latest updates of this project on Github_.

Credits
===========================

* `django`_

.. _Github: https://github.com/alainivars/django_contactform_bootstrap
.. _Issue Tracker: https://github.com/alainivars/django_contactform_bootstrap/issues
.. _django: http://www.djangoproject.com

.. image:: https://pypip.in/version/django_contactform_bootstrap/badge.svg
   :target: https://pypi.python.org/pypi/django_contactform_bootstrap/
   :alt: PyPi version

.. image:: https://pypip.in/wheel/django_contactform_bootstrap/badge.svg
   :target: https://pypi.python.org/pypi/django_contactform_bootstrap/
   :alt: PyPi wheel

.. image:: https://readthedocs.org/projects/django_contactform_bootstrap/badge/?version=latest
    :target: https://readthedocs.org/projects/django_contactform_bootstrap/?badge=latest
    :alt: Documentation status
