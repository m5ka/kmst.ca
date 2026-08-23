from .base import *  # noqa: F403

DEBUG = True
LOCAL = False

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

MEDIA_ROOT = BASE_DIR / "media"
MEDIA_URL = "/media/"
