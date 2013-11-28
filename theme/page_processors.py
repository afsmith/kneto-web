qfrom django.conf import settings
from datetime import datetime    
from django import forms
from django.forms import ModelForm
from django.http import HttpResponseRedirect
from templated_email import send_templated_mail
from mezzanine.pages.page_processors import processor_for
from .models import HomePage, HomePageInc, ContactFormInc, BetaInterview
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

class BetaInterview(ModelForm):

    class Meta:
        model = BetaInterview
        widgets = {
        #    'email': forms.HiddenInput(),
         #   'county': forms.Textarea()
        }
        fields = ('how_many_employees_are_in_your_company', 'how_many_work_in_sales',
                    'how_many_sales_meetings_do_you_have_per_week', 'how_many_offers_do_you_send_out_per_month',
                    'do_you_use_a_marketing_automation_tool', 'how_do_you_deliver_your_offers',)





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

           response = HttpResponseRedirect(redirect)
           response.set_cookie( 'email', homeForm.email )
           response.set_cookie( 'county', homeForm.county )
           return response
           #return HttpResponseRedirect(redirect)
   
   return {"form": form}

@processor_for('beta_thanks')
def beta_interview(request, page):
   form = BetaInterview()
   if request.method == "POST":
       form = BetaInterview(request.POST)
       if form.is_valid():
          ContForm = form.save(commit=False)
           # Form processing goes here.

          ContForm.email = request.COOKIES[ 'email' ]
          ContForm.county = request.COOKIES[ 'county' ] 
          ContForm.date = datetime.now()
          ContForm.save()


          #redirect = request.path + "?submitted=true"
          mredirect =  "/beta-thanks-for-your-help/"
          return HttpResponseRedirect(mredirect)
   
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




