import os

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)


# Security and CSRF
SECRET_KEY = os.environ["KMSTCA_SECRET_KEY"]
ALLOWED_HOSTS = os.environ["KMSTCA_ALLOWED_HOSTS"].split(",")
CSRF_TRUSTED_ORIGINS = os.environ["KMSTCA_CSRF_ORIGINS"].split(",")


# Application definition
INSTALLED_APPS = [
    "kmstca",
    "home",
    "search",
    "news",
    "infodesk",
    "wagtail.contrib.forms",
    "wagtail.contrib.redirects",
    "wagtail.contrib.settings",
    "wagtail.embeds",
    "wagtail.sites",
    "wagtail.users",
    "wagtail.snippets",
    "wagtail.documents",
    "wagtail.images",
    "wagtail.search",
    "wagtail.admin",
    "wagtail",
    "modelcluster",
    "taggit",
    "django_filters",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_minify_html",
]

MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "kmstca.middleware.WebsiteMinifyHtmlMiddleware",
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",
]

ROOT_URLCONF = "kmstca.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "wagtail.contrib.settings.context_processors.settings",
            ]
        },
    },
]

WSGI_APPLICATION = "kmstca.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ["KMSTCA_POSTGRES_NAME"],
        "USER": os.environ["KMSTCA_POSTGRES_USER"],
        "PASSWORD": os.environ["KMSTCA_POSTGRES_PASSWORD"],
        "HOST": os.environ["KMSTCA_POSTGRES_HOST"],
        "PORT": os.environ["KMSTCA_POSTGRES_PORT"],
        "CONN_HEALTH_CHECKS": True,
        "OPTIONS": {
            "pool": {
                "min_size": 2,
                "max_size": 6,
                "timeout": 10,
            },
        },
    }
}


# Default auto field
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"  # noqa: E501
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# User model
# https://docs.wagtail.org/en/stable/advanced_topics/customization/custom_user_models.html

AUTH_USER_MODEL = "kmstca.User"

LOGIN_URL = "/admin/login/"
LOGIN_REDIRECT_URL = "/admin/"


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = "en"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

STATICFILES_DIRS = [os.path.join(PROJECT_DIR, "static")]

STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = os.environ["KMSTCA_STATIC_URL"]


# Storage
# https://docs.djangoproject.com/en/5.2/ref/settings/#std-setting-STORAGES
STORAGES = {
    "default": {"BACKEND": "django.core.files.storage.FileSystemStorage"},
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"
    },
}

# Django sets a maximum of 1000 fields per form by default, but particularly complex
# page models can exceed this limit within Wagtail's page editor.
DATA_UPLOAD_MAX_NUMBER_FIELDS = 10_000


# Wagtail settings

WAGTAIL_SITE_NAME = "kmst.ca"

# Search
# https://docs.wagtail.org/en/stable/topics/search/backends.html
WAGTAILSEARCH_BACKENDS = {"default": {"BACKEND": "wagtail.search.backends.database"}}

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
WAGTAILADMIN_BASE_URL = os.environ["KMSTCA_BASE_URL"]

# Allowed file extensions for documents in the document library.
# This can be omitted to allow all files, but note that this may present a security risk
# if untrusted users are allowed to upload files -
# see https://docs.wagtail.org/en/stable/advanced_topics/deploying.html#user-uploaded-files
WAGTAILDOCS_EXTENSIONS = [
    "csv",
    "docx",
    "key",
    "odt",
    "pdf",
    "pptx",
    "rtf",
    "txt",
    "xlsx",
    "zip",
]
