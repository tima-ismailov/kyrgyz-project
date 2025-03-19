
import os
from pathlib import Path
from .jazzmin import JAZZMIN_SETTINGS, JAZZMIN_UI_TWEAKS

BASE_DIR = Path(__file__).resolve().parent.parent.parent

ALLOWED_HOSTS = ["localhost", "127.0.0.1"] 

DEBUG = True

SECRET_KEY = "django-insecure-o**m^pjx&#lou-%v=2-z=-58%p%$mn-szstd(c()du10ra4oe&"

JAZZMIN_SETTINGS = JAZZMIN_SETTINGS
JAZZMIN_UI_TWEAKS = JAZZMIN_UI_TWEAKS

INSTALLED_APPS = [
    "jazzmin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "encyclopedia",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",  # Обработка локали
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

WSGI_APPLICATION = "config.wsgi.application"

# База данных (SQLite по умолчанию)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Интернационализация
USE_I18N = True
USE_L10N = True
USE_TZ = True

LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Bishkek"

LOCALE_PATHS = [os.path.join(BASE_DIR, "locale")]

# Файлы статики и медиа
STATIC_URL = "static/"
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
