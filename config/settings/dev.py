# config/settings/dev.py

from .base import *

DEBUG = True
ALLOWED_HOSTS = []

# Можно переопределить настройки базы данных для разработки, если нужно:
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db_dev.sqlite3",
#     }
# }
