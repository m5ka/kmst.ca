from django.db.models import TextChoices


class Colour(TextChoices):
    PRIMARY = "primary", "Primary"
    ACCENT = "accent", "Accent"
    GREEN = "green", "Green"
    CREAM = "cream", "Cream"


class ImageSize(TextChoices):
    THUMBNAIL = "thumb", "Thumbnail"
    FULL = "full", "Full"
