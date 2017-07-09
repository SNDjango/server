"""
Django settings for snd project.

Generated by 'django-admin startproject' using Django 1.11.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

from django.contrib.messages import constants as message
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: set the environment variable TUGAG_SECRET_KEY
SECRET_KEY = os.getenv('TUGAG_SECRET_KEY', 'd5-6!1=8baj88-iic*e_r-4u774)5nz=!$$$)!9jsld0b#cwhi')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
        "*"
        ]


# Application definition

INSTALLED_APPS = [
    'image_board',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',

]

AUTHENTICATION_BACKENDS = ('server.snd.image_board.backends.CaseInsensitiveModelBackend', )

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'snd.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'snd.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

import os

#Use the following live settings to build on Travis CI
if os.getenv('BUILD_ON_TRAVIS', None):
    SECRET_KEY = os.getenv('TUGAG_SECRET_KEY', 'SecretKeyForTravis')
    DEBUG = False
    TEMPLATE_DEBUG = True

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'travis_ci_db',
            'USER': 'travis',
            'PASSWORD': '',
            'HOST': '127.0.0.1',
        }
    }
else:
    select_database = os.getenv('TUGAG_DATABASE', 'sqlite3')
    if select_database == 'sqlite3':
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            }
        }
    elif select_database == 'postgresql':
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'NAME': 'tugag_db',
                'USER': os.getenv('TUGAG_DB_USER'),
                'PASSWORD': os.getenv('TUGAG_DB_PASSWORD'),
                'HOST': os.getenv('TUGAG_DB_HOST', '127.0.0.1'),
            }
        }
    elif select_database == 'mysql':
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': 'tugag_db',
                'USER': os.getenv('TUGAG_DB_USER'),
                'PASSWORD': os.getenv('TUGAG_DB_PASSWORD'),
                'HOST': os.getenv('TUGAG_DB_HOST', '127.0.0.1'),
            }
        }
    else:
        raise ValueError("Invalid database setting")

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'CET'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MESSAGE_TAGS = {
    message.INFO: 'alert-info',
    message.DEBUG: 'alert-warning',
    message.SUCCESS: 'alert-success',
    message.WARNING: 'alert-warning',
    message.ERROR: 'alert-danger',
}

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAdminUser',
    ],
    'PAGE_SIZE': 10
}
