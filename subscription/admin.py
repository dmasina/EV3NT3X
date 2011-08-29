from datetime import date
from django.contrib import admin
from subscription.models import Subscription

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'cpf', 'email', 'phone', 'created_at','today' )
    list_filter = ('created_at', )
    date_hierarchy = 'created_at'
    search_fields = ('name', 'cpf', 'email', 'phone', 'created_at', )
    
    def today(self, obj):
        return date.today() == obj.created_at.date()
    today.boolean = True
    today.short_description = u'Inscrito hoje?'
       
#admin.site.register(Subscription) # Usa o modelo padrao do Admin
admin.site.register(Subscription, SubscriptionAdmin) # Usa o model descrito na classe acima