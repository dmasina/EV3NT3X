# -*- encoding: utf-8 -*-
from django.conf.urls.defaults import patterns, url
from eventex.route import route # route.py deve ficar dentro do diretorio eventex

urlpatterns = patterns('subscription.views',                                            
    #url(r'^$', 'subscribe', name='subscribe'),
    route(r'^$', GET='new', POST='create', name='subscribe'),
    url(r'^(\d+)/sucesso/$', 'success', name='success'),
)
