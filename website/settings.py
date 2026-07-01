# ===============================
# TREVILLE MODERN SCHOOLS SETTINGS
# CLEAN WORKING VERSION
# ===============================
import os
from pathlib import Path

# BASE DIRECTORY (this tells Django where your project lives)
BASE_DIR = Path(__file__).resolve().parent.parent


# ===============================
# SECURITY SETTINGS
# ===============================

SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-change-this-in-production')

DEBUG = os.environ.get('DEBUG', 'False') == 'True'  # MUST be True while developing

ALLOWED_HOSTS = ['*']   


# ===============================
# INSTALLED APPS
# ===============================

INSTALLED_APPS = [
    #...your existing apps stay here...
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',]


# ===============================
# MIDDLEWARE (Django internal system)
# ===============================

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# ===============================
# ROOT URL CONFIGURATION
# ===============================

ROOT_URLCONF = 'website.urls'


# ===============================
# TEMPLATES CONFIGURATION (VERY IMPORTANT)
# ===============================

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        # 👇 THIS LINE FIXES YOUR HTML NOT LOADING ISSUE
        'DIRS': [BASE_DIR / "templates"],   # make sure this isn't an empty list []
        # ...

        'APP_DIRS': True,

        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# ===============================
# DATABASE (default SQLite)
# ===============================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# ===============================
# PASSWORD VALIDATION
# ===============================

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# ===============================
# LANGUAGE / TIME SETTINGS
# ===============================

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Lagos'

USE_I18N = True

USE_TZ = True


# ===============================
# STATIC FILES (THIS FIXES YOUR CSS ISSUE)
# ===============================

STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"
STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}
# ===============================
# DEFAULT AUTO FIELD
# ===============================

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'