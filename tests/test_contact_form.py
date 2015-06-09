"""
Contact Form tests
"""
from django import test
from django.core import mail
from django.core.urlresolvers import reverse
from django.template import loader, TemplateDoesNotExist

from contact_form_bootstrap import forms, views

from mock import Mock


def test_BaseEmailFormMixin_get_email_headers():
    form = forms.BaseEmailFormMixin()
    assert not form.get_email_headers()

class BaseEmailFormMixinTests(test.TestCase):

    def test_goods_values_in_contact_page(self):
        resp = self.client.get(reverse("contact"))
        assert 'center: new google.maps.LatLng(48.8148446, 2.0523724)' in resp.content
        assert 'map: map, position: new google.maps.LatLng(48.8148446, 2.0523724)' in resp.content
        assert '<h3 class="fn org">my company</h3>' in resp.content
        assert '<span class="locality">Maybe-there</span>' in resp.content
        assert '<abbr title="Phone">P</abbr>: +336 1234 5678</p>' in resp.content
        assert '<a class="email" href="mailto:contact@mycompany.com">contact@mycompany.com</a>' in resp.content
        assert '<abbr title="Hours">H</abbr>: Monday - Friday: 9:00 to 18:00' in resp.content
        assert 'facebook-link"><a href="http://fr-fr.facebook.com/people/Maybe-there"' in resp.content
        assert 'linkedin-link"><a href="http://www.linkedin.com/in/Maybe-there"' in resp.content
        assert 'twitter-link"><a href="http://twitter.com/Maybe-there"' in resp.content
        assert 'google-plus-link"><a href="https://plus.google.com/+Maybe-there/posts"' in resp.content

    # @mock.patch('django.template.loader.render_to_string')
    # def test_get_message_returns_rendered_message_template(self, render_to_string):
    #     context = {'message': 'an example message.'}
    #
    #     class TestForm(forms.BaseEmailFormMixin):
    #         message_template_name = "my_template.html"
    #
    #         def get_context(self):
    #             return context
    #
    #     form = TestForm()
    #
    #     message = form.get_message()
    #     self.assertEqual(render_to_string.return_value, message)
    #     render_to_string.assert_called_once_with(form.message_template_name, context)

    # @mock.patch('django.template.loader.render_to_string')
    # def test_get_subject_returns_single_line_rendered_subject_template(self, render_to_string):
    #     render_to_string.return_value = 'This is \na \ntemplate.'
    #     context = {'message': 'an example message.'}
    #
    #     class TestForm(forms.BaseEmailFormMixin):
    #         subject_template_name = "my_template.html"
    #
    #         def get_context(self):
    #             return context
    #
    #     form = TestForm()
    #
    #     subject = form.get_subject()
    #     self.assertEqual('This is a template.', subject)
    #     render_to_string.assert_called_once_with(form.subject_template_name, context)

    def test_get_context_returns_cleaned_data_with_request_when_form_is_valid(self):
        request = test.RequestFactory().post(reverse("contact"))

        class TestForm(forms.BaseEmailFormMixin, forms.forms.Form):
            name = forms.forms.CharField()

        form = TestForm(data={'name': 'test'})
        form.request = request
        self.assertEqual(dict(name='test', request=request), form.get_context())

    def test_get_context_returns_value_error_when_form_is_invalid(self):
        class TestForm(forms.BaseEmailFormMixin, forms.forms.Form):
            name = forms.forms.CharField()

        form = TestForm(data={})
        with self.assertRaises(ValueError) as ctx:
            form.get_context()
        assert "Cannot generate Context when form is invalid." == str(ctx.exception)

def test_sends_mail_with_message_dict(monkeypatch):
    mock_request = test.RequestFactory().get(reverse("contact"))
    get_message_dict = Mock()
    get_message_dict.return_value = {"to": ["user@example.com"]}
    monkeypatch.setattr(
        "contact_form_bootstrap.forms.BaseEmailFormMixin.get_message_dict",
        get_message_dict)
    send = Mock()
    send.return_value = 1
    monkeypatch.setattr("django.core.mail.message.EmailMessage.send", send)

    form = forms.BaseEmailFormMixin()
    assert form.send_email(mock_request) == 1

def test_send_mail_sets_request_on_instance(monkeypatch):
    mock_request = test.RequestFactory().get(reverse("contact"))
    get_message_dict = Mock()
    get_message_dict.return_value = {"to": ["user@example.com"]}
    monkeypatch.setattr(
        "contact_form_bootstrap.forms.BaseEmailFormMixin.get_message_dict",
        get_message_dict)
    send = Mock()
    send.return_value = 1
    monkeypatch.setattr("django.core.mail.message.EmailMessage.send", send)

    form = forms.BaseEmailFormMixin()
    form.send_email(mock_request)
    assert mock_request == form.request

# def test_gets_message_dict(monkeypatch):
#     form = forms.BaseEmailFormMixin()
#     message_dict = form.get_message_dict()
#
#     assert message_dict == {
#         "from_email": form.from_email,
#         "to": form.recipient_list,
#         "body": 'get_message.return_value',
#         "subject": 'get_subject.return_value',
#     }

    # @mock.patch("contact_form_bootstrap.forms.BaseEmailFormMixin.get_subject")
    # @mock.patch("contact_form_bootstrap.forms.BaseEmailFormMixin.get_message")
    # def test_get_message_dict_adds_headers_when_present(self, get_message, get_subject):
    #     email_headers = {"Reply-To": "user@example.com"}
    #
    #     class HeadersForm(forms.BaseEmailFormMixin):
    #
    #         def get_email_headers(self):
    #             return email_headers
    #
    #     form = HeadersForm()
    #     message_dict = form.get_message_dict()
    #
    #     self.assertEqual({
    #         "from_email": form.from_email,
    #         "to": form.recipient_list,
    #         "body": get_message.return_value,
    #         "subject": get_subject.return_value,
    #         "headers": email_headers,
    #     }, message_dict)


class ContactFormTests(test.TestCase):

    def test_is_subclass_of_form_and_base_email_form_mixin(self):
        self.assertTrue(issubclass(forms.ContactForm, forms.BaseEmailFormMixin))
        self.assertTrue(issubclass(forms.ContactForm, forms.forms.Form))

    def test_sends_mail_with_headers(self):
        class ReplyToForm(forms.ContactForm):
            email = forms.forms.EmailField()

            def get_email_headers(self):
                return {'Reply-To': self.cleaned_data['email']}

        mock_request = test.RequestFactory().get(reverse("contact"))
        reply_to_email = u'user@example.com' # the user's email
        data = {
            'name': 'Test',
            'body': 'Test message',
            'phone': '0123456789',
            'email': reply_to_email,
        }
        form = ReplyToForm(data=data)
        assert form.send_email(mock_request)
        assert len(mail.outbox) == 1
        reply_to_header_email = mail.outbox[0].extra_headers['Reply-To']
        self.assertEqual(reply_to_email, reply_to_header_email)
