# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'contact_form_bootstrap/templates'),
            os.path.join(BASE_DIR, 'example/templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

ADMINS = (
    ('Firstname Lastname', 'contact@mydomain.com'),
)

CONTACT_FORM_SUBJECT_TEMPLATE_NAME = 'email_subject.txt'
CONTACT_FORM_MESSAGE_TEMPLATE_NAME = 'email_message.txt'

COMPANY_INFOS = {
    'NAME': "my company",
    'ADDRESS': "26 streets from here th there",
    'ZIP': "1234",
    'CITY': "Maybe-there",
    'LAT': 48.81484460000001,
    'LNG': 2.0523723999999675,
    'PHONE': "+336 1234 5678",
    'EMAIL': 'contact@mycompany.com',
    'FACEBOOK': "http://fr-fr.facebook.com/people/Maybe-there",
    'LINKEDIN': "http://www.linkedin.com/in/Maybe-there",
    'TWITTER': "http://twitter.com/Maybe-there",
    'GOOGLEPLUS': "https://plus.google.com/Maybe-there/posts",
}

CRISPY_TEMPLATE_PACK = 'bootstrap3'

# if you use capcha overload these parameters and set USE_RECAPTCHA to True
USE_RECAPTCHA = False
RECAPTCHA_PUBLIC_KEY = 'your reCapcha public key'
RECAPTCHA_PRIVATE_KEY = 'your reCapcha private key'
