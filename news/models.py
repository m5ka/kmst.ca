from django.db.models import CASCADE, PROTECT, SET_NULL, CharField, ForeignKey
from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey
from taggit.models import ItemBase
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.fields import StreamField
from wagtail.models import Page

from kmstca.blocks import KmstcaBlocks
from news.constants import NewsCategory


class TopicTaggedArticle(ItemBase):
    tag = ForeignKey(
        "kmstca.TopicTag", related_name="tagged_articles", on_delete=CASCADE
    )
    content_object = ParentalKey(
        to="news.Article", on_delete=CASCADE, related_name="topic_tagged_items"
    )


class LocationTaggedArticle(ItemBase):
    tag = ForeignKey(
        "kmstca.LocationTag", related_name="tagged_articles", on_delete=CASCADE
    )
    content_object = ParentalKey(
        to="news.Article", on_delete=CASCADE, related_name="location_tagged_items"
    )


class Article(Page):
    body = StreamField(KmstcaBlocks())
    image = ForeignKey(
        "wagtailimages.Image",
        related_name="+",
        blank=True,
        null=True,
        on_delete=SET_NULL,
    )
    topics = ClusterTaggableManager(
        through="news.TopicTaggedArticle", blank=True, verbose_name="Topics"
    )
    locations = ClusterTaggableManager(
        through="news.LocationTaggedArticle", blank=True, verbose_name="Locations"
    )
    category = CharField(max_length=64, choices=NewsCategory.choices)
    author = ForeignKey("kmstca.User", on_delete=PROTECT, related_name="+")

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [FieldPanel("topics"), FieldPanel("locations")], heading="Tags", icon="tag"
        ),
        FieldPanel("category", icon="folder-open-1"),
        FieldPanel("author", icon="user"),
        FieldPanel("image", icon="image"),
        FieldPanel("body", icon="pilcrow"),
    ]

    parent_page_types = ["news.ArticleIndex"]
    subpage_types = []


class ArticleIndex(Page):
    subpage_types = ["news.Article"]
    max_count = 1

    def get_context(self, request, *args, **kwargs):
        return {
            **super().get_context(request, *args, **kwargs),
            "articles": Article.objects.order_by("-first_published_at")[:9],
        }
