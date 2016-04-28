.. image:: https://api.travis-ci.org/alainivars/django-contact-form.svg?branch=master
   :target: http://travis-ci.org/alainivars/django-contact-form
   :alt: Build status

.. image:: https://coveralls.io/repos/alainivars/django-contact-form/badge.svg?branch=devel
   :target: https://coveralls.io/r/alainivars/django-contact-form?branch=devel
   :alt: Test coverage status

.. image:: https://requires.io/github/alainivars/django-contact-form/requirements.svg?branch=master
   :target: https://requires.io/github/alainivars/django-contact-form/requirements/?branch=master
   :alt: Requirements Status

.. image:: https://img.shields.io/pypi/dm/django_contactform_bootstrap.svg
   :target: https://pypi.python.org/pypi/django_contactform_bootstrap/
   :alt: pypi download

.. image:: https://img.shields.io/pypi/pyversions/django_contactform_bootstrap.svg
   :target: https://pypi.python.org/pypi/django_contactform_bootstrap/
   :alt: python supported

.. image:: https://img.shields.io/pypi/l/django_contactform_bootstrap.svg
   :target: https://pypi.python.org/pypi/django_contactform_bootstrap/
   :alt: licence



Releases Notes
==============

    0.6.0: add reCapcha support, fix links to your : FACEBOOK, LINKEDIN, TWITTER, GOOGLE+
    0.5.11: fix a bug with import main settings
    0.5.0: Add support and tests on Django 1.9 and update dependencies

Requirements
============

 - Python 2.7 and 3.3, 3.4
 - Django 1.4.11+, 1.7+, 1.8+, 1.9+ and master

Features
========

* Functionality as a django contact form::

  - easy integration into an existing django project
  - Bootstrap 3
  - integrate geographical map
  - log (not yet finish)
  - tests and coverage
  - links to your : FACEBOOK, LINKEDIN, TWITTER, GOOGLE+

Todo
====

 - finish english translation and add other translations
 - improve log
 - manage display a link only if it exist
 - correct broken links in this file

Screenshot
==========

.. image:: https://dl.dropboxusercontent.com/u/95975146/django-contactform-bootstrap.jpg
   :target: https://dl.dropboxusercontent.com/u/95975146/django-contactform-bootstrap.jpg
   :alt: Contact form Screenshot

Download
========

 - source code here::


        git clone https://github.com/alainivars/django-contact-form.git


 - packet::

        https://pypi.python.org/pypi/django_contactform_bootstrap

 - or::

        pip install django_contactform_bootstrap


Use
===

    + Add in your settings file::

        INSTALLED_APPS = (
            ...
            'contact_form_bootstrap',
            ...
        )

        ADMINS = (
            ('your admin name', 'contact@yourdomain.com'),
        )

        COMPANY = {
            'NAME': "my company",
            'ADDRESS': "26 streets from here th there",
            'ZIP': "1234",
            'CITY': "Paris",
            'LAT': 48.81484460000001,
            'LNG': 2.0523723999999675,
            'PHONE': "+336 1234 5678",
            'EMAIL': 'contact@yourdomain.com',
            'FACEBOOK': "https://www.facebook.com/highfeature",
            'LINKEDIN': "http://www.linkedin.com/in/ivarsalain",
            'TWITTER': "https://twitter.com/HighFeature",
            'GOOGLEPLUS': "https://twitter.com/HighFeature",
        }

        CRISPY_TEMPLATE_PACK = 'bootstrap3'

         USE_RECAPTCHA = False or True
         and if you use it :
         RECAPTCHA_PUBLIC_KEY = 'your reCapcha public key'
         RECAPTCHA_PRIVATE_KEY = 'your reCapcha private key'

    + Don't forget to set::

        EMAIL_HOST, EMAIL_PORT, EMAIL_HOST_USER and EMAIL_HOST_PASSWORD


Documentation
=============

.. note::
    Please note that this Project is documented poorly. If you have any questions please contact us!
    We'd love to update the documentation and answer your question!

Getting Help
============

Please report bugs or ask questions using the `Issue Tracker`

Check also for the latest updates of this project on Github_.

Credits
=======

    Based on James Bennett's django_contact_form:
      - https://bitbucket.org/ubernostrum/django_contact_form
    Based on Aaron Madison django_contact_form:
      - https://github.com/madisona/django-contact-form
    By Alain Ivars django_contactform_bootstrap:
      - https://github.com/alainivars/django-contact-form

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
