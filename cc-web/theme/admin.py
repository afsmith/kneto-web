from copy import deepcopy
from django.contrib import admin
from mezzanine.core.admin import TabularDynamicInlineAdmin
from mezzanine.pages.admin import PageAdmin
from mezzanine.pages.models import Page
from mezzanine.forms.admin import FormAdmin
from mezzanine.galleries.admin import GalleryAdmin
from mezzanine.pages.models import RichTextPage
from .models import Slide, IconBlurb, HomePage

class SlideAdmin(TabularDynamicInlineAdmin):
    """ """
    model = (Slide,)
    inlines = (Slide,)
   

class IconBlurbAdmin(TabularDynamicInlineAdmin):
    """ """
    model = (IconBlurb,)
    inlines = (IconBlurb,)
    

class HomeAdmin(PageAdmin):
    inlines = (HomePage,)
    fieldsets = deepcopy(PageAdmin.fieldsets)


    admin.site.register( HomePage,)
    admin.site.register( Slide,)
    admin.site.register( IconBlurb,)
   