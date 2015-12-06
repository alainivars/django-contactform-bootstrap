from django.conf.urls import url

from contact_form_bootstrap.views import ContactFormView, CompletedPage


urlpatterns = [
    url(r'^$', ContactFormView.as_view(), name="contact"),
    url(r'^completed/$', CompletedPage.as_view(), name="completed"),
]