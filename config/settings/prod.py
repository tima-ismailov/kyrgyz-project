# config/settings/prod.py

from .base import *

DEBUG = False
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "your-production-domain.com"]
PRODUCTION = False

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": os.environ.get("DB_NAME"),
#         "USER": os.environ.get("DB_USER"),
#         "PASSWORD": os.environ.get("DB_PASSWORD"),
#         "HOST": os.environ.get("DB_HOST"),
#         "PORT": os.environ.get("DB_PORT", "5432"),
#     }
# }

# SECURE_SSL_REDIRECT = True
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True
