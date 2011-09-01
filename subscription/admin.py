# -*- coding: utf-8 -*- 

from datetime import date
from django.contrib import admin
from subscription.models import Subscription
from django.utils.translation import gettext as _
from django.utils.translation import ungettext
from django.http import HttpRequest, HttpResponse
from django.conf.urls.defaults import patterns, url

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'cpf', 'email', 'phone', 'created_at','today', 'paid' )
    list_filter = ('created_at', )
    date_hierarchy = 'created_at'
    search_fields = ('name', 'cpf', 'email', 'phone', 'created_at', )
    
    def today(self, obj):
        return date.today() == obj.created_at.date()
    today.boolean = True
    today.short_description = u'Inscrito hoje?'
    
    #
    # Cria uma action que sera acionada pela view do subscription
    #
    
    actions = ['mark_as_paid']
    
    def mark_as_paid(self, request, queryset):
        count = queryset.update(paid=True)
        
        msg = ungettext(
            u'%(count)d inscrição marcada como paga.',
            u'%(count)d inscrições marcadas como pagas.',
            count
                       
        ) % {'count': count}
        
        self.message_user(request, msg)
        
    mark_as_paid.short_description = _(u'Marcar como pagas') 
 
 
    #
    # Custom View que extende ModelAdmin para exportar arquivo CSV
    #

    def export_subscriptions(self, request):
        subscriptions = self.model.objects.all()
        rows = [','.join([s.name, s.email]) for s in subscriptions]
        
        response = HttpResponse('\r\n'.join(rows))
        response.mimetype = 'text/csv'
        response['Content-Disposition'] = 'attachement; filename=inscricoes.csv'
        
        return response
 
 
    #
    # Define URL de download e aproveita a 'admin_view' para controlar permissoes e cache.
    # A ordem das URLs eh importante, pois as URLs do Admin sao muito permissivas.
    #
    
    def get_urls(self):
        original_urls = super(SubscriptionAdmin, self).get_urls()
        extra_urls = patterns('',
            url(r'exportar-inscricoes/$',
                self.admin_site.admin_view(self.export_subscriptions),
                name='export_subscriptions') 
        )
        return extra_urls + original_urls
        

#admin.site.register(Subscription) # Usa o modelo padrao do Admin
admin.site.register(Subscription, SubscriptionAdmin) # Usa o model descrito na classe acima


