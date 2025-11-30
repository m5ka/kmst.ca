from django.db.models import TextChoices


class NewsCategory(TextChoices):
    POLITICS = "politics", "Uettis"
    WORLD = "world", "Ardá"
    SCIENCE = "science", "Gnátiá"
    CULTURE = "culture", "Teutá"
    ENVIRONMENT = "environment", "Mbinektis"
    BUSINESS = "business", "Meiamtis"
    CRIME = "crime", "Uargdétiá"
    SPORTS = "sports", "Gamán"
    OPINION = "opinion", "Gustus"
