#-*- coding: utf-8 -*-


from django.core.urlresolvers import reverse
from django.views.generic.base import TemplateView
from django.views.generic import CreateView, FormView

from contact_form_bootstrap import settings
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
