# -*- encoding: utf-8 -*-
from django.template.context import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import SubscriptionForm
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from subscription.models import Subscription


def subscribe(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new (request)
            
def new(request):
    form = SubscriptionForm()
    context = RequestContext(request, {'form' : form})
    return render_to_response('subscription/form.html', context)

def create(request):
    form = SubscriptionForm(request.POST)     
    if not form.is_valid():
        context = RequestContext(request, {'form' : form})
        return render_to_response('subscription/form.html', context) 
    subscription = form.save()
    send_mail(
        subject = u'Inscrição no EV3NT3X',
        message = u'Obrigado por se inscrever no EV3NT3X.',
        from_email = u'contato@eventex.com',
        recipient_list = ['daniel.masina@gmail.com'],
    )
    return HttpResponseRedirect( # O redirect evita submeter o form novamente caso o user de F5
                reverse('subscription:success', args=[subscription.pk]))
    
def success(request, pk):   
    subscription = get_object_or_404(Subscription, pk=pk) # Aceita modelo ou QuerySet
    context = RequestContext(request, {'subscription': subscription})
    return render_to_response('subscription/success.html', context)
            
    