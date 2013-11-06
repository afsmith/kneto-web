from django.db import models
from django.utils.translation import ugettext_lazy as _
from mezzanine.pages.models import Page, RichText, Orderable 
from mezzanine.core.fields import FileField
from mezzanine.utils.models import upload_to


class HomePageInc(models.Model):
    """
    model for the homepage form
    """

    form_name = models.CharField(max_length=100, default='NUL')
    date = models.DateTimeField()
    email = models.EmailField()
    ip = models.GenericIPAddressField(null=True)
    county = models.CharField(null=True, max_length=50)

    def __unicode__(self):
        return self.name


class ContactFormInc(models.Model):
    """
    model for the homepage form
    """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.CharField(max_length=5000)
    date = models.DateTimeField()

    def __unicode__(self):
        return self.name


class HomePage(Page, RichText):
    '''
    A page representing the format of the home page
    '''
    calloutleft = models.CharField(max_length=250,
        help_text="Left side Callout", default="callout left")
    callout_title_left = models.CharField(max_length=30,
        help_text="Left side Callout title", default="callout title left")
    calloutcenter = models.CharField(max_length=250,
        help_text="Center Callout", default="callout center")
    callout_title_center = models.CharField(max_length=30,
        help_text="Center side Callout title", default="callout title center")
    calloutright = models.CharField(max_length=250,
        help_text="Right side Callout", default="callout right")
    callout_title_right = models.CharField(max_length=30,
        help_text="Right side Callout title", default="callout title right")

    heading = models.CharField(max_length=200,
        help_text="The heading under the icon blurbs")
    subheading = models.CharField(max_length=200,
        help_text="The subheading just below the heading")
#    featured_works_heading = models.CharField(max_length=200,
#       default="Featured Works")

    center_title = models.CharField(max_length=200,
        default="Center Bottom Title")
    center_bottom = models.CharField(max_length=200,
        default="Center Bottom")

    #latest_posts_heading = models.CharField(max_length=200,
    #   default="Latest Posts")
    

    class Meta:
        verbose_name = _("Home page")
        verbose_name_plural = _("Home pages")


class ContactPage(Page):
    class Meta:
        verbose_name = _("Contact Page")
        verbose_name_plural = _("Contact Pages")


class Slide(Orderable):
    '''
    A slide in a slider connected to a HomePage
    '''
    homepage = models.ForeignKey(HomePage, related_name="slides")
    image = FileField(verbose_name=_("Image"),
        upload_to=upload_to("theme.Slide.image", "slider"),
        format="Image", max_length=255, null=True, blank=True)


class IconBlurb(Orderable):
    '''
    An icon box on a HomePage
    '''
    homepage = models.ForeignKey(HomePage, related_name="blurbs")
    icon = FileField(verbose_name=_("Image"),
        upload_to=upload_to("theme.IconBlurb.icon", "icons"),
        format="Image", max_length=255)
    title = models.CharField(max_length=200)
    content = models.TextField()
    link = models.CharField(max_length=2000, blank=True,
        help_text="Optional, if provided clicking the blurb will go here.")


class Portfolio(Page):
    '''
    A collection of individual portfolio items
    '''
    class Meta:
        verbose_name = _("Portfolio")
        verbose_name_plural = _("Portfolios")
