from django.db.models import TextChoices


class NewsCategory(TextChoices):
    POLITICS = "politics", "Wettis"
    WORLD = "world", "Ardā"
    SCIENCE = "science", "Gnātjā"
    CULTURE = "culture", "Teutā"
    ENVIRONMENT = "environment", "Mbinektis"
    BUSINESS = "business", "Mejamtis"
    CRIME = "crime", "Wargdētjā"
    SPORTS = "sports", "Gamān"
    OPINION = "opinion", "Gustus"
