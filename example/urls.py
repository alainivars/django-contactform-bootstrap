from django.conf.urls import include, url
from django.contrib import admin
from example.views import IndexView

app_name = 'contact_form_bootstrap'

urlpatterns = [
    url(r'^$', IndexView.as_view(), name="homepage"),
    url(r'^admin/', admin.site.urls),
    url(r'^contact/', include(
        ("contact_form_bootstrap.urls", 'contact_form_bootstrap'),
        namespace="contact_form_bootstrap")
    ),
]
