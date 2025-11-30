from taggit.models import TagBase
from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet


class LocationTag(TagBase):
    free_tagging = False

    class Meta:
        verbose_name = "location"
        verbose_name_plural = "locations"


@register_snippet
class LocationTagViewSet(SnippetViewSet):
    model = LocationTag
    icon = "thumbtack"


class TopicTag(TagBase):
    free_tagging = False

    class Meta:
        verbose_name = "topic"
        verbose_name_plural = "topics"


@register_snippet
class TopicTagViewSet(SnippetViewSet):
    model = TopicTag
    icon = "tag"
