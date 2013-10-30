from datetime import datetime    
from django import forms
from django.shortcuts import render_to_response
from django.forms import ModelForm
from django.http import HttpResponseRedirect
from mezzanine.pages.page_processors import processor_for
from .models import HomePage, HomePageInc


class HomePageForm(ModelForm):

    class Meta:
        model = HomePageInc
        widgets = {
            'form_name': forms.HiddenInput()
        }
        fields = ('email', 'form_name',)


@processor_for(HomePage)
def beta_form(request, page):
   form = HomePageForm()
   if request.method == "POST":
       form = HomePageForm(request.POST)
      # homeForm = form.save(commit=False)
       if form.is_valid():
           # Form processing goes here.
           homeForm.date = datetime.now()
           homeForm.form_name = 'HomePageForm'
           homeForm.save()

           #redirect = request.path + "?submitted=true"
           redirect = "beta_thanks/" 
           return HttpResponseRedirect(redirect)
   
   return {"form": form}
