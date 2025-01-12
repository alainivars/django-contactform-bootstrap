# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging

from captcha.widgets import ReCaptchaV2Checkbox
from django.conf import settings
from django.core.mail.message import EmailMessage
from django.forms import Form, CharField, EmailField, EmailInput, Textarea, TextInput
from django.template import loader
from django.utils.translation import ugettext_lazy as _

from captcha.fields import ReCaptchaField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit
from crispy_forms.bootstrap import FormActions

logger = logging.getLogger(__name__)


class BaseEmailFormMixin(object):
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [email for _, email in settings.ADMINS]

    def get_message(self):
        logger.debug('get_message')
        template = settings.CONTACT_FORM_SUBJECT_TEMPLATE_NAME or 'email_subject.txt'
        content = loader.render_to_string(template, self.get_context())
        return ''.join(content.splitlines())

    def get_subject(self):
        logger.debug('get_subject')
        template = settings.CONTACT_FORM_MESSAGE_TEMPLATE_NAME or 'email_message.txt'
        content = loader.render_to_string(template, self.get_context())
        return ''.join(content.splitlines())

    def get_context(self):
        """
        Context sent to templates for rendering include the form's cleaned
        data and also the current Request object.
        """
        logger.debug('get_context')
        if not self.is_valid():
            # import pprint
            # pprint.pprint('self %s' % self.cleaned_data)
            raise ValueError("Cannot generate Context when form is invalid.")
        return dict(request=self.request, **self.cleaned_data)

    def get_email_headers(self):
        """
        Subclasses can replace this method to define additional settings like
        a reply_to value.
        """
        logger.debug('get_email_headers')
        return None

    def get_message_dict(self):
        logger.debug('get_message_dict')
        message_dict = {
            "from_email": self.from_email,
            "to": self.recipient_list,
            "subject": self.get_subject(),
            "body": self.get_message(),
        }
        headers = self.get_email_headers()
        if headers is not None:
            message_dict['headers'] = headers
        return message_dict

    def send_email(self, request, fail_silently=False):
        logger.debug('send_email')
        assert self.recipient_list
        self.request = request
        return EmailMessage(**self.get_message_dict()).send(fail_silently=fail_silently)


class ContactForm(Form, BaseEmailFormMixin):
    """
    A very basic contact form you can use out of the box if you wish.
    """
    name = CharField(
        widget=TextInput(
            attrs={
                "placeholder": "Name",
                "class": "form-control"
            }
        ))
    email = EmailField(
        widget=EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"
            }
        ))
    phone = CharField(
        widget=TextInput(
            attrs={
                "placeholder": "Phone",
                "class": "form-control"
            }
        ))
    body = CharField(
        widget=Textarea(
            attrs={
                "placeholder": "Message",
                "class": "form-control"
            }
        ))
    # captcha = ReCaptchaField(
    #     widget=ReCaptchaV2Checkbox(
    #         attrs={'theme': 'clean'}
    #     ))

    def __init__(self, *args, **kwargs):
        logger.debug('__init__')
        super(ContactForm, self).__init__(*args, **kwargs)
        # Add captcha in the constructor to allow mock it
        # because https://github.com/mbi/django-simple-captcha/issues/84
        self.fields["captcha"] = ReCaptchaField(
            widget=ReCaptchaV2Checkbox(
                attrs={'theme': 'clean'}
            )
        )
        # cryspy
        self.helper = FormHelper()
        self.helper.form_id = 'id-CcontactForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_class = 'form'
        if settings.USE_RECAPTCHA:
            self.helper.layout = Layout(
                Div(
                    Div('name', css_class="form-group col-lg-4"),
                    Div('email', css_class="form-group col-lg-4"),
                    Div('phone', css_class="form-group col-lg-4"),
                    Div(css_class="clearfix"),
                    Div('body', css_class="form-group col-lg-12"),
                    Div(css_class="clearfix"),
                    Div('captcha', css_class="form-group col-lg-12"),
                    FormActions(
                        Div(
                            Submit('submit', _('Submit'), css_class='btn btn-primary'),
                            css_class="form-group col-lg-12"
                        ),
                    ),
                    css_class="row",
                ),
            )
        else:
            self.helper.layout = Layout(
                Div(
                    Div('name', css_class="form-group col-lg-4"),
                    Div('email', css_class="form-group col-lg-4"),
                    Div('phone', css_class="form-group col-lg-4"),
                    Div(css_class="clearfix"),
                    Div('body', css_class="form-group col-lg-12"),
                    FormActions(
                        Div(
                            Submit('submit', _('Submit'), css_class='btn btn-primary'),
                            css_class="form-group col-lg-12"
                        ),
                    ),
                    css_class="row",
                ),
            )

    def get_email_headers(self):
        logger.debug('get_email_headers')
        return {'Reply-To': self.cleaned_data['email']}
