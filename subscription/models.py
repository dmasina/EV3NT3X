# -*- coding: utf-8 -*- 

from django.db import models

# Create your models here.

class Subscription (models.Model):
    name = models.CharField('Nome', max_length=100)
    cpf = models.CharField('CPF', max_length=11, unique=True)
    email = models.EmailField('E-mail', unique=True)
    phone = models.CharField('Telefone', max_length=20, blank=True)
    created_at = models.DateField('Criado em', auto_now_add=True)
    
    # Representacao do modelo:
    # Retorna o conteudo de 'name' ao inves do tipo do objeto. 
    # Ao trabalhar com muitos objetos, voce sabe exatamente com quem esta trabalhando.
    # Isto eh muito usado pelo Admin do Django.
    def __unicode__ (self):
        return (self.name)
    
    # Classe para fornecer metainforacoes para o Django (Define alguns padroes)
    class Meta:
        
        # Default para pesquisas
        ordering = ["created_at", "name"]
        
        # Informacoes utilizadas pelo Admin do Django
        verbose_name = u"Inscrição"
        verbose_name_plural = u"Inscrições"
        