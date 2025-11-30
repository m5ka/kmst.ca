from .base import *  # noqa: F403

DEBUG = False

# Google Cloud storage
STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3.S3Storage",
        "OPTIONS": {
            "bucket_name": os.environ["KMSTCA_STORAGE_BUCKET_USER_CONTENT"],
        },
    },
    "staticfiles": {
        "BACKEND": "storages.backends.s3.S3Storage",
        "OPTIONS": {
            "bucket_name": os.environ["KMSTCA_STORAGE_BUCKET_STATIC"],
        },
    },
}
AWS_S3_ACCESS_KEY_ID = os.environ["KMSTCA_S3_ACCESS_KEY"]
AWS_S3_SECRET_ACCESS_KEY = os.environ["KMSTCA_S3_SECRET_KEY"]
