"""
Django settings for kejaAppBackend project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('djangoKejaAppKey')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['keja-app-backend.herokuapp.com', '127.0.0.1']

# Application definition

INSTALLED_APPS = [
    'houses.apps.HousesConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'leaflet',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_gis',
    'djoser',
    'storages',
    'imagekit',
    'oauth2_provider',
    'social_django',
    'rest_framework_social_oauth2',

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

ROOT_URLCONF = 'kejaAppBackend.urls'

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
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'kejaAppBackend.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'df0s93kronbhmu',
        'USER': 'hlbxsadmqbhcmg',
        'PASSWORD': 'fc8ecd7186c43b15cebf6138e23c5f1cb7eb1c2502d00a903fcc34b5b0cbb3c2',
        'HOST': 'ec2-18-215-99-63.compute-1.amazonaws.com',
        'PORT': '5432'
    }
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        # 'oauth2_provider.ext.rest_framework.OAuth2Authentication',  # django-oauth-toolkit < 1.0.0
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',  # django-oauth-toolkit >= 1.0.0
        'rest_framework_social_oauth2.authentication.SocialAuthentication',
    ),
    'DEFAULT_PERMISSIONS_CLASSES': (
        'rest_framework.permissions.IsAuthenticated'
    )
}

AUTHENTICATION_BACKENDS = (
    # Facebook OAuth2
    'social_core.backends.facebook.FacebookAppOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',

    # django-rest-framework-social-oauth2
    'rest_framework_social_oauth2.backends.DjangoOAuth2',

    # django
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_POSTGRES_JSONFIELD = True

# Facebook configuration
SOCIAL_AUTH_FACEBOOK_KEY = '1089568628093051'
SOCIAL_AUTH_FACEBOOK_SECRET = 'a6e85965852eb243566d1a5c4308d11f'

# Define SOCIAL_AUTH_FACEBOOK_SCOPE to get extra permissions from Facebook.
# Email is not sent by default, to get it, you must request the email permission.
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    'fields': 'id, name, email'
}

AUTH_USER_MODEL = 'houses.User'

DJOSER = {
    'USER_ID_FIELD': 'email',
    'LOGIN_FIELD': 'email',
    'PASSWORD_RESET_CONFIRM_URL': 'houses/users/password-reset/{uid}/{token}',
    'SEND_ACTIVATION_EMAIL': True,
    'PASSWORD_CHANGED_EMAIL_CONFIRMATION': True,
    'ACTIVATION_URL': 'houses/users/activate/{uid}/{token}',
    'USER_CREATE_PASSWORD_RETYPE': True,
    'SET_PASSWORD_RETYPE': True,
    'PASSWORD_RESET_CONFIRM_RETYPE': True,
    'LOGOUT_ON_PASSWORD_CHANGE': True,
    'PASSWORD_RESET_SHOW_EMAIL_NOT_FOUND': True,
    'SERIALIZERS': {
        'user_create': 'houses.serializers.UserCreateSerializer',
        'user': 'houses.serializers.UserCreateSerializer',
        'activation': 'djoser.serializers.ActivationSerializer',
        'password_reset': 'djoser.serializers.SendEmailResetSerializer',
        'password_reset_confirm': 'djoser.serializers.PasswordResetConfirmSerializer',
        'password_reset_confirm_retype': 'djoser.serializers.PasswordResetConfirmRetypeSerializer',
        'set_password': 'djoser.serializers.SetPasswordSerializer',
        'set_password_retype': 'djoser.serializers.SetPasswordRetypeSerializer',
        'user_delete': 'djoser.serializers.UserDeleteSerializer',
    },
    'EMAIL': {
        'activation': 'djoser.email.ActivationEmail'
    },
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Nairobi'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "../static")

from .aws import *
