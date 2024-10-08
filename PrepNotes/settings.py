"""
Django settings for PrepNotes project.

Generated by 'django-admin startproject' using Django 4.2.10.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
import django_heroku
import dj_database_url
from decouple import config
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ['DEBUG']

ALLOWED_HOSTS = ['www.prepnotes.me','prepnotes.me', 'hydrophobic-finch-y97ovybh7zbyky6voacx8o78.herokudns.com', 'prepnotes-999c25a3799e.herokuapp.com', 'www.prepnotes-999c25a3799e.herokuapp.com', 'localhost', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
   'tailwind',
   'theme',
    'notes',
    'tinymce',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'PrepNotes.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'PrepNotes.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PW'],
        'HOST': 'aws-0-ap-south-1.pooler.supabase.com',
        'PORT': '6543',  # Default PostgreSQL port
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / "static"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


TAILWIND_APP_NAME = 'theme' # This is the name of the app that will be used to generate the tailwind files
INTERNAL_IPS = ['localhost', '127.0.0.1','www.prepnotes.me','prepnotes.me', 'hydrophobic-finch-y97ovybh7zbyky6voacx8o78.herokudns.com', 'www.prepnotes-999c25a3799e.herokuapp.com', 'prepnotes-999c25a3799e.herokuapp.com']

#NPM_BIN_PATH = '/app/.local/state/fnm_multishells/29_1724768850072/bin/npm'
NPM_BIN_PATH = "/app/.heroku/node/bin/npm"


# for windows
#NPM_BIN_PATH = r"C:\Program Files\nodejs\npm.cmd"


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # Replace with your SMTP server's host
EMAIL_PORT = 587  # Common ports are 587 for TLS, 465 for SSL
EMAIL_USE_TLS = True  # Use TLS or SSL as required by your SMTP server
EMAIL_USE_SSL = False  # Use SSL if TLS is not required
EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']  # Your email address
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']  # Your email password
EMAIL_TO_USER = os.environ['EMAIL_TO_USER']  # Default sender address

TINYMCE_DEFAULT_CONFIG = {
  "theme": "silver",
  "resize": "false",
  "menubar": "file edit view insert format tools table help",
  "toolbar":
    "undo redo | bold italic underline strikethrough | fontselect fontsizeselect customerfontsizeselect formatselect | alignleft aligncenter alignright alignjustify | outdent indent |  numlist bullist checklist | forecolor backcolor casechange permanentpen formatpainter removeformat | pagebreak | charmap emoticons | fullscreen  preview save print | insertfile image media pageembed template link anchor codesample | a11ycheck ltr rtl | showcomments addcomment code typography",
  "plugins":
    "advlist autolink lists link image charmap print preview anchor searchreplace visualblocks code fullscreen insertdatetime media table powerpaste advcode help wordcount spellchecker typography",
  "selector": '.tinymce', 
};

django_heroku.settings(locals())