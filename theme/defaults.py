from django.utils.translation import ugettext_lazy as _
from mezzanine.conf import register_setting

register_setting(
    name="SOCIAL_LINK_FACEBOOK",
    label=_("Facebook link"),
    description=_("If present a Facebook icon linking here will be in the "
        "header."),
    editable=True,
    default="https://facebook.com/mezzatheme",
)

register_setting(
    name="TEMPLATE_ACCESSIBLE_SETTINGS",
    description=_("Sequence of setting names available within templates."),
    editable=False,
    default=("SOCIAL_LINK_FACEBOOK",),
    append=True,
)