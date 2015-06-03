from django.conf.urls import url, patterns

from contact_form_bootstrap.views import ContactFormView, CompletedPage


urlpatterns = patterns('',
    url(r'^$', ContactFormView.as_view(), name="contact"),
    url(r'^completed/$', CompletedPage.as_view(), name="completed"),
)