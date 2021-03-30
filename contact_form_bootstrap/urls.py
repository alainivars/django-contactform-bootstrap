from django.urls import re_path

from contact_form_bootstrap.views import ContactFormView, CompletedPage


urlpatterns = [
    re_path(r'^$', ContactFormView.as_view(), name="contact"),
    re_path(r'^completed/$', CompletedPage.as_view(), name="completed"),
]
