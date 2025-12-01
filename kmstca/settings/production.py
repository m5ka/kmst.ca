from .base import *  # noqa: F403

DEBUG = False

# Google Cloud storage
STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3.S3Storage",
        "OPTIONS": {"bucket_name": os.environ["KMSTCA_STORAGE_BUCKET_USER_CONTENT"]},
    },
    "staticfiles": {
        "BACKEND": "storages.backends.s3.S3Storage",
        "OPTIONS": {"bucket_name": os.environ["KMSTCA_STORAGE_BUCKET_STATIC"]},
    },
}
AWS_S3_ENDPOINT_URL = os.environ["KMSTCA_S3_ENDPOINT_URL"]
AWS_S3_ACCESS_KEY_ID = os.environ["KMSTCA_S3_ACCESS_KEY"]
AWS_S3_SECRET_ACCESS_KEY = os.environ["KMSTCA_S3_SECRET_KEY"]
AWS_DEFAULT_ACL = "public-read"
AWS_S3_SIGNATURE_VERSION = "s3"

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {"format": "{levelname} {asctime} {module} {message}", "style": "{"},
    },
    "handlers": {
        "console": {"class": "logging.StreamHandler", "formatter": "verbose"},
    },
    "loggers": {
        "django": {"handlers": ["console"], "level": "WARNING", "propagate": True}
    },
}
