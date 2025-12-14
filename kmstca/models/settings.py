from django.db.models import CharField, ImageField
from wagtail.contrib.settings.models import (
    BaseGenericSetting,
    BaseSiteSetting,
    register_setting,
)

from kmstca.constants import Colour


@register_setting
class KmstcaSettings(BaseGenericSetting):
    copyright = CharField(max_length=64, blank=True)


@register_setting
class SiteSettings(BaseSiteSetting):
    logo = ImageField()
    colour_scheme = CharField(
        max_length=32, choices=Colour.choices, default=Colour.ACCENT
    )
