import datetime
from django import forms
from django.forms import ModelForm
from django.http import HttpResponseRedirect
from mezzanine.pages.page_processors import processor_for
from .models import HomePage, HomePageInc

#class BetaForm(forms.Form):
#    name = forms.CharField()
#   email = forms.EmailField()

class HomePageForm(ModelForm):
    class Meta:
        model = HomePageInc
        fields = ('email',)


@processor_for(HomePage)
def beta_form(request, page):
   form = HomePageForm()
   if request.method == "POST":
       form = HomePageForm(request.POST)
       homeForm = form.save(commit=False)
       if form.is_valid():
           # Form processing goes here.
           homeForm.date = datetime.date.today()
           homeForm.name = 'placeHolder'
           homeForm.save()

           redirect = request.path + "?submitted=true"
           return HttpResponseRedirect(redirect)
   return {"form": form}
