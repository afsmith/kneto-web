from django.conf import settings
from datetime import datetime    
from django import forms
from django.shortcuts import render_to_response
from django.forms import ModelForm
from django.http import HttpResponseRedirect
from templated_email import send_templated_mail
from mezzanine.pages.page_processors import processor_for
from .models import HomePage, HomePageInc, ContactFormInc, ContactPage
import pygeoip


class HomePageForm(ModelForm):

    class Meta:
        model = HomePageInc
        widgets = {
            'form_name': forms.HiddenInput()
        }
        fields = ('email', 'form_name',)

class ContactForm(ModelForm):

    class Meta:
        model = ContactFormInc
        widgets = {
            'form_name': forms.HiddenInput(),
            'message': forms.Textarea()
        }
        fields = ('first_name', 'last_name', 'email', 'message',)


@processor_for(HomePage)
def beta_form(request, page):
   form = HomePageForm()
   if request.method == "POST":
       form = HomePageForm(request.POST)
       if form.is_valid():
           ip = request.META.get('REMOTE_ADDR', None)
           gi4 = pygeoip.GeoIP(settings.GEO_DATA, pygeoip.STANDARD)
           county = gi4.country_name_by_addr(ip)
           homeForm = form.save(commit=False)
           # Form processing goes here.
           homeForm.date = datetime.now()
           homeForm.ip = ip
           homeForm.county = county
           homeForm.form_name = 'HomePageForm'
           homeForm.save()
           send_templated_mail(
            template_name='beta_thanks',
            from_email= settings.DEFAULT_FROM_EMAIL,
            recipient_list=[ homeForm.email ],
            bcc=[settings.DEFAULT_BCC_EMAIL],
            context={
            'email': homeForm.email,
            },
            )

           #redirect = request.path + "?submitted=true"
           redirect = "beta_thanks/" 
           return HttpResponseRedirect(redirect)
   
   return {"form": form}

@processor_for('contact-page')
def contact_form(request, page):
   form = ContactForm()
   if request.method == "POST":
       form = ContactForm(request.POST)
       if form.is_valid():
          ContForm = form.save(commit=False)
           # Form processing goes here.
          ContForm.date = datetime.now()
          ContForm.save()
          send_templated_mail(
            template_name='contact',
            from_email= settings.DEFAULT_FROM_EMAIL,
            bcc=[settings.DEFAULT_BCC_EMAIL],
            recipient_list=[ ContForm.email ],
            context={
            'first_name': ContForm.first_name,
            'last_name': ContForm.last_name,
            'message': ContForm.message,
            },
            )

          #redirect = request.path + "?submitted=true"
          mredirect = "/thanks-for-your-interest/" 
          return HttpResponseRedirect(mredirect)
   
   return {"form": form}
