# config/settings_production.py
from .settings import *
from decouple import config

DEBUG = False

ALLOWED_HOSTS = [
    'gamedev.tiltpenguin.com',
    'localhost',
    '127.0.0.1',
    '.tiltpenguin.com',
]

# Security for Cloudflare
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
CSRF_TRUSTED_ORIGINS = [
    'https://gamedev.tiltpenguin.com',
    'https://*.tiltpenguin.com',
]

# Static files
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Use environment variable for secret key
SECRET_KEY = config('SECRET_KEY')