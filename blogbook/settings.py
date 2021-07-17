from pathlib import Path
from datetime import timedelta
import dj_database_url

ENV = "PROD"

BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = BASE_DIR / "templates"
MEDIA_DIR = BASE_DIR / "media"
STATIC_URL = "/static/"

if ENV == "DEV":
    STATIC_DIR = BASE_DIR / "static"
    STATICFILES_DIRS = [STATIC_DIR]
    DEBUG = True

if ENV == "PROD":
    STATIC_ROOT = BASE_DIR / "static"
    STATICFILES_STORAGE = "django.contrib.staticfiles.storage.StaticFilesStorage"
    DEBUG = False

AUTH_USER_MODEL = "writers.Writer"

SECRET_KEY = "django-insecure-q0-mimlxlphjz5*p+t7396%xp&&hh3wsfzp69(b0ugacg-*jx5"


CORS_ORIGIN_ALLOW_ALL = False
ALLOWED_HOSTS = ["localhost", ".herokuapp.com"]
CORS_ORIGIN_WHITELIST = ("http://localhost:3000", "https://blogbook.web.app")
# CORS_ALLOWED_ORIGIN_REGEXES = [r"^https://blogbook\w+\.web\.app$"]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "corsheaders",
    "rest_framework",
    "writers",
    "blogs",
]

# REST_FRAMEWORK = {
#     "DEFAULT_AUTHENTICATION_CLASSES": (
#         "rest_framework_simplejwt.authentication.JWTAuthentication",
#     )
# }

# SIMPLE_JWT = {
#     "ACCESS_TOKEN_LIFETIME": timedelta(minutes=15),
#     "REFRESH_TOKEN_LIFETIME": timedelta(days=15),
#     "ROTATE_REFRESH_TOKENS": True,
#     "BLACKLIST_AFTER_ROTATION": True,
#     "USER_ID_FIELD": "pk",
#     "USER_ID_CLAIM": "user_pk",
# }

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "corsheaders.middleware.CorsMiddleware",
]

EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = "argon.intelligence@gmail.com"
EMAIL_HOST_PASSWORD = "1806@two000"
EMAIL_PORT = 587
EMAIL_USE_TLS = True

ROOT_URLCONF = "blogbook.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [TEMPLATE_DIR],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "blogbook.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
DATABASES["default"].update(dj_database_url.config(conn_max_age=500))

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Kolkata"
USE_I18N = True
USE_L10N = True
USE_TZ = True

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
