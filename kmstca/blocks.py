from wagtail.blocks import CharBlock, RichTextBlock, StreamBlock, StructBlock
from wagtail.images.blocks import ImageBlock


class CaptionedImageBlock(StructBlock):
    image = ImageBlock()
    caption = CharBlock()
    source = CharBlock(required=False)
    date = CharBlock(required=False)

    class Meta:
        icon = "image"


class QuoteBlock(StructBlock):
    text = RichTextBlock(features=["bold", "italic"])
    quotee = CharBlock(help_text="Who originally said or wrote this quote")
    quotee_qualifier = CharBlock(
        required=False,
        help_text=(
            "An optional qualifier for the quotee, such as their profession or role"
        ),
    )
    date = CharBlock(
        required=False,
        help_text="An optional date for when this quote was said or written",
    )
    context = CharBlock(
        required=False,
        help_text="An optional context for the quote, such as the work it comes from",
    )

    class Meta:
        icon = "openquote"
        template = "blocks/quote.html"


class KmstcaBlocks(StreamBlock):
    heading = CharBlock(icon="title", template="blocks/heading.html")
    subheading = CharBlock(icon="h2", template="blocks/subheading.html")
    paragraph = RichTextBlock(features=["bold", "italic", "ol", "ul", "hr", "link"])
    image = CaptionedImageBlock()
    quote = QuoteBlock()
