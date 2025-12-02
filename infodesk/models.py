from functools import lru_cache

from django.db.models import CASCADE, SET_NULL, BooleanField, CharField, ForeignKey
from modelcluster.models import ParentalKey
from wagtail.admin.forms import WagtailAdminPageForm
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.fields import RichTextField, StreamField
from wagtail.models import ContentType, Orderable, Page
from wagtail.search.index import FilterField, SearchField

from kmstca.blocks import KmstcaBlocks
from kmstca.constants import Colour


@lru_cache
def get_category_page_content_type_id() -> int | None:
    content_type = ContentType.objects.get_for_model(CategoryPage)
    return content_type.id if content_type is not None else None


class CategoryPageSubcategory(Orderable):
    category_page = ParentalKey(
        "infodesk.CategoryPage", related_name="subcategories", on_delete=CASCADE
    )
    name = CharField(max_length=64)
    tagline = RichTextField(blank=True)

    def __str__(self):
        return self.name


class ContentPageForm(WagtailAdminPageForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if "parent_page" in kwargs and kwargs["parent_page"] is not None:
            parent_page = kwargs["parent_page"]
            category_page_content_type_id = get_category_page_content_type_id()
            if parent_page.content_type_id == category_page_content_type_id:
                self.fields[
                    "subcategory"
                ].queryset = CategoryPageSubcategory.objects.filter(
                    category_page=parent_page
                )
            else:
                self.fields["subcategory"].disabled = True


class ContentPage(Page):
    subcategory = ForeignKey(
        "infodesk.CategoryPageSubcategory",
        on_delete=SET_NULL,
        related_name="pages",
        blank=True,
        null=True,
    )
    body = StreamField(KmstcaBlocks(), blank=True)
    act_as_index = BooleanField(
        default=False, help_text="Display an alphabetized index of child pages"
    )

    content_panels = Page.content_panels + [
        FieldPanel("subcategory", icon="tag"),
        FieldPanel("act_as_index", icon="form"),
        FieldPanel("body", icon="pilcrow"),
    ]
    base_form_class = ContentPageForm

    search_fields = Page.search_fields + [
        SearchField("body"),
        FilterField("subcategory"),
    ]

    parent_page_types = ["infodesk.CategoryPage", "infodesk.ContentPage"]

    @property
    def first_letter(self):
        return self.title[0].upper()

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        if self.act_as_index:
            context["children"] = ContentPage.objects.order_by("title").child_of(self)
        return context


class CategoryPage(Page):
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
        InlinePanel("subcategories"),
        MultiFieldPanel(
            [FieldPanel("pre_body"), FieldPanel("post_body")],
            heading="Content",
            icon="pilcrow",
        ),
    ]

    parent_page_types = ["home.HomePage"]
    subpage_types = ["infodesk.ContentPage"]

    search_fields = Page.search_fields + [SearchField("tagline")]

    def get_context(self, request, *args, **kwargs):
        return {
            **super().get_context(request, *args, **kwargs),
            "children": ContentPage.objects.select_related("subcategory")
            .order_by("subcategory__sort_order", "title")
            .child_of(self),
        }
