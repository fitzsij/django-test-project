from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Form.views.home', name='home'),
    # url(r'^Form/', include('Form.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^form/', 'form_app.views.showPackages'),
    #url(r'^contact/', 'form_app.views.ContactForm'),
    url(r'^contact/$', 'form_app.views.search_form'),
    url(r'^search/$', 'form_app.views.search'),
)
