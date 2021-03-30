from __future__ import unicode_literals

from unittest import mock

"""
Contact Form tests
"""
import os
from django import test
from django.core import mail
from django.urls import reverse
from django.forms import Form, TextInput, CharField
from django.views.generic import TemplateView

from contact_form_bootstrap.forms import BaseEmailFormMixin, ContactForm
from contact_form_bootstrap.views import CompletedPage, ContactFormMixin, ContactFormView, FormView

from mock import Mock


def test_BaseEmailFormMixin_get_email_headers():
    form = BaseEmailFormMixin()
    assert not form.get_email_headers()


class BaseEmailFormMixinTests(test.TestCase):

    def test_goods_values_in_contact_page(self):
        resp = self.client.get(reverse("contact"))
        assert b'center: new google.maps.LatLng(48.8148446' in resp.content
        assert b'map: map, position: new google.maps.LatLng(48.8148446' in resp.content
        assert b'<h3 class="fn org">my company</h3>' in resp.content
        assert b'<span class="locality">Maybe-there</span>' in resp.content
        assert b'<abbr title="Phone">P</abbr>: +336 1234 5678</p>' in resp.content
        assert b'<a class="email" href="mailto:contact@mycompany.com">contact@mycompany.com</a>' in resp.content
        assert b'<abbr title="Hours">H</abbr>: Monday - Friday: 9:00 to 18:00' in resp.content
        assert b'facebook-link"><a href="http://fr-fr.facebook.com/people/Maybe-there"' in resp.content
        assert b'linkedin-link"><a href="http://www.linkedin.com/in/Maybe-there"' in resp.content
        assert b'twitter-link"><a href="http://twitter.com/Maybe-there"' in resp.content
        assert b'google-plus-link"><a href="https://plus.google.com/Maybe-there/posts"' in resp.content

    def test_get_context_returns_cleaned_data_with_request_when_form_is_valid(self):
        class TestForm(BaseEmailFormMixin, Form):
            name = TextInput()

        form = TestForm(data={'name': b'test'})
        form.request = test.RequestFactory().post(reverse("contact"))
        self.assertEqual(dict(request=form.request), form.get_context())

    def test_get_context_returns_value_error_when_form_is_invalid(self):
        class TestForm(BaseEmailFormMixin, Form):
            name = TextInput()

        form = TestForm(data={})
        with self.assertRaises(AttributeError) as ctx:
            form.get_context()
            assert "AttributeError: 'TestForm' object has no attribute 'request'" \
                   == str(ctx.exception)


def test_sends_mail_with_message_dict(monkeypatch):
    request = test.RequestFactory().get(reverse("contact"))
    get_message_dict = Mock()
    get_message_dict.return_value = {"to": ["user@example.new.com"]}
    monkeypatch.setattr(
        "contact_form_bootstrap.forms.BaseEmailFormMixin.get_message_dict",
        get_message_dict)
    send = Mock()
    send.return_value = 1
    monkeypatch.setattr("django.core.mail.message.EmailMessage.send", send)

    form = ContactForm()
    assert form.send_email(request) == 1


def test_send_mail_sets_request_on_instance(monkeypatch):
    request = test.RequestFactory().get(reverse("contact"))
    get_message_dict = Mock()
    get_message_dict.return_value = {"to": ["user@example.new.com"]}
    monkeypatch.setattr(
        "contact_form_bootstrap.forms.BaseEmailFormMixin.get_message_dict",
        get_message_dict)
    send = Mock()
    send.return_value = 1
    monkeypatch.setattr("django.core.mail.message.EmailMessage.send", send)

    form = ContactForm()
    form.send_email(request)
    assert request == form.request


class ContactFormTests(test.TestCase):

    def test_is_subclass_of(self):
        self.assertTrue(issubclass(ContactForm, BaseEmailFormMixin))
        self.assertTrue(issubclass(ContactForm, Form))

    @mock.patch("contact_form_bootstrap.forms.ReCaptchaField",
                lambda: CharField(required=False))
    def test_sends_mail_with_headers(self):
        os.environ['RECAPTCHA_TESTING'] = 'True'
        request = test.RequestFactory().get(reverse("contact"))
        reply_to_email = u'user@example.new.com' # the user's email
        data = {
            'name': b'Test',
            'body': b'Test message',
            'phone': b'0123456789',
            'email': reply_to_email,
            'recaptcha_response_field': 'PASSED'
        }
        form = ContactForm(data=data)
        assert form.is_valid()
        assert form.send_email(request)
        assert len(mail.outbox) == 1
        assert reply_to_email == mail.outbox[0].extra_headers['Reply-To']
        assert form.get_email_headers() == {'Reply-To': 'user@example.new.com'}
        os.environ['RECAPTCHA_TESTING'] = 'False'


class CompletedPageTests(test.TestCase):

    def test_is_subclass_of(self):
        self.assertTrue(issubclass(CompletedPage, TemplateView))

    def test_get_context_data(self):
        c = CompletedPage()
        context = c.get_context_data()
        assert context['url'] == 'contact'


class ContactFormViewTests(test.TestCase):

    def test_is_subclass_of(self):
        self.assertTrue(issubclass(ContactFormView, ContactFormMixin))
        self.assertTrue(issubclass(ContactFormView, FormView))

    def test_get_success_url(self):
        v = ContactFormView()
        assert v.get_success_url() == reverse("completed")

    def test_form_valid(self):
        class MyForm(object):
            def send_email(self, request):
                pass

        f = MyForm()
        v = ContactFormView()
        v.request = test.RequestFactory().get(reverse("contact"))
        assert v.form_valid(f)
