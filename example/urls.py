from django.conf.urls import patterns, include, url
from django.contrib import admin
from example.views import IndexView

urlpatterns = patterns(
    '',
    url(r'^$', IndexView.as_view(), name="homepage"),
    url(r'^contact/', include("contact_form_bootstrap.urls", namespace="contact_form_bootstrap")),
    url(r'^admin/', include(admin.site.urls)),
)
