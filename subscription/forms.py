# -*- encoding: utf-8 -*-
from django import forms
from subscription.models import Subscription

class SubscriptionForm(forms.ModelForm): # Cria formularios dinamicos com base nas metainformacoes
    class Meta:
        model = Subscription
        exclude = ('created_at','paid')