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

    def __unicode__(self):
        return self.name



class HomePage(Page, RichText):
    '''
    A page representing the format of the home page
    '''
    heading = models.CharField(max_length=200,
        help_text="The heading under the icon blurbs")
    subheading = models.CharField(max_length=200,
        help_text="The subheading just below the heading")
    featured_works_heading = models.CharField(max_length=200,
        default="Featured Works")
    featured_portfolio = models.ForeignKey("Portfolio", blank=True, null=True,
        help_text="If selected items from this portfolio will be featured "
                  "on the home page.")
    content_heading = models.CharField(max_length=200,
        default="About us!")
    latest_posts_heading = models.CharField(max_length=200,
        default="Latest Posts")

    class Meta:
        verbose_name = _("Home page")
        verbose_name_plural = _("Home pages")


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
