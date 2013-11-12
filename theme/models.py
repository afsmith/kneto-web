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


class BetaInterview(models.Model):
    """
    model for beta thanks page
    """
    NUMBER_EMPLOYES_CHOICES = (
            ('00', '----------',),
            ('01', 'Self Employed',),
            ('10', '1-10',),
            ('20', '11-20',),
            ('50', '20-50',),
            ('100', '51-100',),
            ('500', '100-500',),
            ('501', 'More than 500'),
        )
    
    HOW_MANY_IN_SALES = (
            ('00', '----------',),
            ('01', 'None',),
            ('05', '1-5',),
            ('10', '6-10',),
            ('20', '11-20',),
            ('50', '20-50',),
            ('100', '51-100',),
            ('500', '100-500',),
            ('501', 'More than 500',),
        )

    HOW_MANY_IN_SALES = (
            ('00', '----------',),
            ('01', 'None',),
            ('05', '1-5',),
            ('10', '6-10',),
            ('20', '11-20',),
            ('50', '21-50',),
            ('100', '51-100',),
            ('500', '100-500',),
            ('501', 'More than 500',),
        )

    NUMBER_OF_MEETINGS = (
            ('00', '----------',),
            ('01', 'None',),
            ('05', '1-5',),
            ('10', '6-10',),
            ('20', '11-20',),
            ('50', '21-50',),
            ('100', 'More than 50',),
        )
    NUMBER_OF_OFFERS = (
            ('00', '----------',),
            ('01', 'None',),
            ('05', '1-5',),
            ('10', '6-10',),
            ('20', '11-20',),
            ('50', '21-50',),
            ('100', '51-100',),
            ('500', '101-500',),
            ('501', 'More than 500',),
        )

    AUTOMATION_TOOL = (
            ('00', '----------',),
            ('hb','Hubspot',),
            ('mk','Marketo',),
            ('el','Elequa',),
            ('ls','Leadsius',),
            ('ot','Other',),
        )

    OFFER_DIST = (
        ('00', '----------',),
        ('01', 'In person',),
        ('02', 'By email',),
        ('03', 'With CRM',),
        ('04', 'Other',),

        )



    how_many_employees_are_in_your_company = models.CharField(max_length=20,
                                        choices=NUMBER_EMPLOYES_CHOICES,
                                        default='None',)

    how_many_work_in_sales = models.CharField(max_length=20,
                                        choices=HOW_MANY_IN_SALES,
                                        default='Self Employed',)

    how_many_sales_meetings_do_you_have_per_week = models.CharField(max_length=20,
                                        choices=NUMBER_OF_MEETINGS,
                                        default='None',)

    how_many_offers_do_you_send_out_per_month =  models.CharField(max_length=20,
                                        choices=NUMBER_OF_OFFERS,
                                        default='None',)

    do_you_use_a_marketing_automation_tool =  models.CharField(max_length=20,
                                        choices=AUTOMATION_TOOL,
                                        default='None',)

    how_do_you_deliver_your_offers =  models.CharField(max_length=20,
                                        choices=OFFER_DIST,
                                        default='None',)
    email = models.EmailField()
    county = models.CharField(null=True, max_length=50)
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
