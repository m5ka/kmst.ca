from django.db.models import CharField, ImageField
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting

from kmstca.constants import Colour


@register_setting
class SiteSettings(BaseSiteSetting):
    logo = ImageField()
    colour_scheme = CharField(
        max_length=32, choices=Colour.choices, default=Colour.ACCENT
    )
