from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^contact/', include("contact_form_bootstrap.urls", namespace="contact_form_bootstrap")),
    url(r'^admin/', include(admin.site.urls)),
)
