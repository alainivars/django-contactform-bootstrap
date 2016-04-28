__author__ = 'alainivars'

ADMINS = (
    ('Alain Ivars', 'contact@mydomain.com'),
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
