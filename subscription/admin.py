# -*- coding: utf-8 -*- 

from datetime import date
from django.contrib import admin
from subscription.models import Subscription
from django.utils.translation import gettext as _
from django.utils.translation import ungettext

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'cpf', 'email', 'phone', 'created_at','today', 'paid' )
    list_filter = ('created_at', )
    date_hierarchy = 'created_at'
    search_fields = ('name', 'cpf', 'email', 'phone', 'created_at', )
    
    def today(self, obj):
        return date.today() == obj.created_at.date()
    today.boolean = True
    today.short_description = u'Inscrito hoje?'
    
    # Cria uma action que sera acionada pela view do subscription
    
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
       
#admin.site.register(Subscription) # Usa o modelo padrao do Admin
admin.site.register(Subscription, SubscriptionAdmin) # Usa o model descrito na classe acima


