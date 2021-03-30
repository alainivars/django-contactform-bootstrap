# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import reverse
# from django.http import HttpResponseForbidden
from django.views.generic.base import TemplateView
from django.views.generic import FormView

from django.conf import settings
# from werkzeug.utils import redirect

from contact_form_bootstrap.forms import ContactForm


class CompletedPage(TemplateView):
    template_name = "contact_completed.html"

    def get_context_data(self, **kwargs):
        context = super(CompletedPage, self).get_context_data(**kwargs)
        context['url'] = 'contact'
        return context


class ContactFormMixin(object):
    """
    Form view that sends email when form is valid. You'll need
    to define your own form_class and template_name.
    """
    def form_valid(self, form):
        form.send_email(self.request)
        return super(ContactFormMixin, self).form_valid(form)

    def get_success_url(self):
        return reverse("completed")

# from django import forms
# class ContactForm(forms.Form):
#     """
#     Form view that sends email when form is valid. You'll need
#     to define your own form_class and template_name.
#     """
#     subject = forms.CharField(max_length=100)
#
#     def form_valid(self, form):
#         form.send_email(self.request)
#         return super(ContactForm, self).form_valid(form)
#
#     def get_success_url(self):
#         return reverse("completed")
#
#
# from django.views.generic import View
# from django.views.generic.edit import FormMixin
# class ContactFormView(View):
#     template_name = "contact.html"
#     form_class = ContactForm
#
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['form'] = ContactForm()
#         return context
#
#     def post(self, request, *args, **kwargs):
#         if not request.user.is_authenticated:
#             return HttpResponseForbidden()
#         self.object = self.get_object()
#         form = self.get_form()
#         if form.is_valid():
#             return self.form_valid(form)
#         else:
#             return self.form_invalid(form)
#
#     def form_valid(self, form):
#         # Here, we would record the user's interest using the message
#         # passed in form.cleaned_data['message']
#         return super().form_valid(form)


class ContactFormView(ContactFormMixin, FormView):
    template_name = "contact.html"
    form_class = ContactForm

    def get_context_data(self, **kwargs):
        context = super(ContactFormView, self).get_context_data(**kwargs)
        context['url'] = 'contact'
        context['COMPANY_LAT'] = settings.COMPANY_INFOS['LAT']
        context['COMPANY_LNG'] = settings.COMPANY_INFOS['LNG']
        context['COMPANY_NAME'] = settings.COMPANY_INFOS['NAME']
        context['COMPANY_ADDRESS'] = settings.COMPANY_INFOS['ADDRESS']
        context['COMPANY_ZIP'] = settings.COMPANY_INFOS['ZIP']
        context['COMPANY_CITY'] = settings.COMPANY_INFOS['CITY']
        context['COMPANY_PHONE'] = settings.COMPANY_INFOS['PHONE']
        context['COMPANY_EMAIL'] = settings.COMPANY_INFOS['EMAIL']
        context['COMPANY_FACEBOOK'] = settings.COMPANY_INFOS['FACEBOOK']
        context['COMPANY_LINKEDIN'] = settings.COMPANY_INFOS['LINKEDIN']
        context['COMPANY_TWITTER'] = settings.COMPANY_INFOS['TWITTER']
        context['COMPANY_GOOGLEPLUS'] = settings.COMPANY_INFOS['GOOGLEPLUS']
        return context
