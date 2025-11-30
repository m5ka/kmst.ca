from django.db.models import CASCADE, SET_NULL, CharField, ForeignKey
from modelcluster.models import ParentalKey
from wagtail.admin.forms import WagtailAdminPageForm
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.fields import RichTextField, StreamField
from wagtail.models import Orderable, Page
from wagtail.search.index import FilterField, SearchField

from kmstca.blocks import KmstcaBlocks
from kmstca.constants import Colour


class IndexPageCategory(Orderable):
    index_page = ParentalKey(
        "infodesk.IndexPage", related_name="categories", on_delete=CASCADE
    )
    name = CharField(max_length=64)
    tagline = RichTextField(blank=True)

    def __str__(self):
        return self.name


class ContentPageForm(WagtailAdminPageForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if "parent_page" in kwargs and kwargs["parent_page"] is not None:
            self.fields["category"].queryset = IndexPageCategory.objects.filter(
                index_page=kwargs["parent_page"]
            )


class ContentPage(Page):
    category = ForeignKey(
        "infodesk.IndexPageCategory",
        on_delete=SET_NULL,
        related_name="pages",
        blank=True,
        null=True,
    )
    body = StreamField(KmstcaBlocks())

    content_panels = Page.content_panels + [
        FieldPanel("category", icon="tag"),
        FieldPanel("body", icon="pilcrow"),
    ]
    base_form_class = ContentPageForm

    search_fields = Page.search_fields + [SearchField("body"), FilterField("category")]

    parent_page_types = ["infodesk.IndexPage"]


class IndexPage(Page):
    colour = CharField(max_length=16, choices=Colour.choices, default=Colour.PRIMARY)
    icon = CharField(max_length=32, verbose_name="BoxIcon class")
    tagline = RichTextField(features=["bold", "italic"])
    pre_body = StreamField(KmstcaBlocks(), verbose_name="Pre-index body", blank=True)
    post_body = StreamField(KmstcaBlocks(), verbose_name="Post-index body", blank=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [FieldPanel("colour"), FieldPanel("icon"), FieldPanel("tagline")],
            heading="Appearance",
            icon="palette",
        ),
        InlinePanel("categories"),
        MultiFieldPanel(
            [FieldPanel("pre_body"), FieldPanel("post_body")],
            heading="Content",
            icon="pilcrow",
        ),
    ]

    subpage_types = ["infodesk.ContentPage"]

    search_fields = Page.search_fields + [SearchField("tagline")]

    def get_context(self, request, *args, **kwargs):
        return {
            **super().get_context(request, *args, **kwargs),
            "children": ContentPage.objects.select_related("category")
            .order_by("category__sort_order", "title")
            .child_of(self),
        }
