# -*- encoding: utf-8 -*-
from django.conf.urls.defaults import patterns, url, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'core.views.homepage'),
    url(r'^inscricao/', include('subscription.urls', namespace='subscription')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^admin/', include('django.contrib.admin.urls')), # Nao funcionou

)

urlpatterns += staticfiles_urlpatterns()
