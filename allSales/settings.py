"""
Django settings for allSales project.

Generated by 'django-admin startproject' using Django 1.11.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ''

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
DEVELOPMENT = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'allSales',
    'collar',
    'customer',
    'faktura',
    'prioListe',
    'rma',
    'sales',
    'staff',
    'statistic',
    'survey',
    'vertexLite',
    'warranty',
    'ordercontact',
    'trapTransmitter',
    'miniFawn',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'allSales.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        'libraries': {
            'extra_tags': 'allSales.templatetags.extra_tags'
        },
        },
    },
]

WSGI_APPLICATION = 'allSales.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

if DEVELOPMENT:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'testingdb.sqlite3'),
        },
        'order_db': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'orderdb',
            'USER': 'foobar',
            'PASSWORD': 'foopwd',
            'HOST': 'foo.com',
            'PORT': '5432',
        },
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'CollarDB',
            'USER': 'foobar',
            'PASSWORD': 'passwd',
            'HOST': '192.168.0.26',
            'PORT': '5432',
        },
        'prio_db': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'VASPriorityList',
            'USER': 'foobar',
            'PASSWORD': 'passwd',
            'HOST': '192.168.0.26',
            'PORT': '5432',
        },
        'faktura_db': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'Faktura',
            'USER': 'foobar',
            'PASSWORD': 'passwd',
            'HOST': '192.168.0.26',
            'PORT': '5432',
        },
        'rma_db': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'refurbishments',
            'USER': 'foobar',
            'PASSWORD': 'passwd',
            'HOST': '192.168.0.26',
            'PORT': '5432',
        },
        'order_db': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'orderdb',
            'USER': 'foobar',
            'PASSWORD': 'passwd',
            'HOST': 'wombat.vectronic-wildlife.com',
            'PORT': '5432',
        },
    }

    DATABASE_ROUTERS = ['faktura.FakturaRouter.FakturaRouter', 'rma.RmaRouter.RmaRouter',
                        'sales.OrderRouter.OrderRouter', 'prioListe.PrioRouter.PrioRouter', 'survey.OrderRouter.OrderRouter']
    DATABASE_APPS_MAPPING = {'sales': 'order_db',
                             'survey': 'order_db',
                             'rma': 'rma_db',
                             'faktura': 'faktura_db',
                             'prioListe': 'prio_db',
                            }


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

TIME_ZONE = 'Europe/Berlin'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'handlers': {
#         'console': {
#             'level': 'DEBUG',
#             'class': 'logging.StreamHandler',
#         }
#     },
#     'loggers': {
#         'django.db.backends': {
#             'handlers': ['console'],
#             'level': 'DEBUG',
#         },
#     }
# }