An Extensible Contact Form.
Based entirely on James Bennett's django_contactform_bootstrap:
https://bitbucket.org/ubernostrum/django_contactform_bootstrap/

|Build status| |PyPi version| |PyPi downloads| |Python version| |PyPi wheel| |Project license|

Features
===========================

* Functionality as a django contact form
  - easy integration into an existing django project
  - Bootstrap 3
  - integrate geographical map
  - vcard in settings file
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

Use
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


    + Don't forget to set::

        EMAIL_HOST, EMAIL_PORT, EMAIL_HOST_USER and EMAIL_HOST_PASSWORD


    and to generate messages by::

        django-admin compilemessages


Documentation
===========================

.. note::
    Please note that this Project is documented poorly. If you have any questions please contact us!
    We'd love to update the documentation and answer your question!

    Why version 0.5.0 and not 1.0.0 ?
    - This django_contact_form_bootstrap is already in use in production, but it first time packaged for distribute
      and I'm not sure the packaging is ready to use immediately, please be wait a little, a release will arrive.

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

.. |Build status| image:: https://api.travis-ci.org/django-contact-form/django-contact-form.svg?branch=master
   :target: http://travis-ci.org/alainivars/django-contact-form
.. |PyPi version| image:: https://pypip.in/v/alainivars/badge.svg?text=version
   :target: https://pypi.python.org/pypi/django_contactform_bootstrap/
.. |PyPi downloads| image:: https://pypip.in/d/django_contactform_bootstrap/badge.svg?period=month
   :target: https://pypi.python.org/pypi/django_contactform_bootstrap/
.. |Python version| image:: https://pypip.in/py_versions/django_contactform_bootstrap/badge.svg
   :target: https://pypi.python.org/pypi/django_contactform_bootstrap/
.. |PyPi wheel| image:: https://pypip.in/wheel/django_contactform_bootstrap/badge.svg
   :target: https://pypi.python.org/pypi/django_contactform_bootstrap/
.. |Project license| image:: https://pypip.in/license/django_contactform_bootstrap/badge.svg
   :target: https://pypi.python.org/pypi/django_contactform_bootstrap/
