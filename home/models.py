from django.db.models import CharField
from wagtail.admin.panels import FieldPanel
from wagtail.models import Page

from infodesk.models import IndexPage
from news.constants import NewsCategory
from news.models import Article


class HomePage(Page):
    heading = CharField(max_length=511)

    content_panels = Page.content_panels + [FieldPanel("heading")]
    max_count = 1

    def get_context(self, request, *args, **kwargs):
        return {
            **super().get_context(request, *args, **kwargs),
            "children": IndexPage.objects.child_of(self),
            "articles": Article.objects.exclude(category=NewsCategory.OPINION).order_by(
                "-first_published_at"
            )[:6],
        }
