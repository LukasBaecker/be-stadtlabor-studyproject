"""
Django settings for urbangarden project.

Generated by 'django-admin startproject' using Django 3.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%i5*%7%zlim4#m%9y^+m$#-mqd0a$1l0m977%)yrwt&-gc1*2c'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['giv-project15.uni-muenster.de','*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_gis',
    'rest_framework_swagger',
    'corsheaders',
    'users',
    'crops',
    'gardens',
    'events',
    'django.contrib.gis',
    
    
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'urbangarden.urls'

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
                'staticfiles': 'django.templatetags.static',
            },
        },
    },
]

WSGI_APPLICATION = 'urbangarden.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'gardening', #YOUR_DATABASE_NAME
        'USER': 'postgres', #YOUR_USER_NAME
        'PASSWORD': 'postgres',#YOUR_DB_PASSWORD
        'HOST': 'giv-project15.uni-muenster.de', #HOST
        'PORT': '5432'   #PORT
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'


#User Issues - Brian 
AUTH_USER_MODEL = "users.User" 

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

REST_FRAMEWORK = {'DEFAULT_SCHEMA_CLASS' : 'rest_framework.schemas.coreapi.AutoSchema'}

#Brian's Path
#GDAL_LIBRARY_PATH='/opt/homebrew/Cellar/gdal/3.3.3' 
#Javier's Path
GDAL_LIBRARY_PATH= 'C:/Users/jmmartin/.5 Citylab/be-stadtlabor/venv/Lib/site-packages/osgeo/gdal303.dll'
GEOS_LIBRARY_PATH= 'C:/Users/jmmartin/.5 Citylab/be-stadtlabor/venv/Lib/site-packages/osgeo/geos_c.dll'

#Javier -> added to solve the geometry problem: "GDALException at /admin/gardens/garden/5/change/ OGR failure"    
os.environ['GDAL_DATA'] = "C:/Users/jmmartin/.5 Citylab/be-stadtlabor/venv/Lib/site-packages/osgeo/data/gdal"
os.environ['PROJ_LIB'] = "C:/Users/jmmartin/.5 Citylab/be-stadtlabor/venv/Lib/site-packages/osgeo/data/proj"
os.environ['PATH'] = "C:/Users/jmmartin/.5 Citylab/be-stadtlabor/venv/Lib/site-packages/osgeo/" + ";" + os.environ['PATH']

#Nivedita's Path
#GDAL_LIBRARY_PATH='C:/Citylab/be-stadtlabor/venv/Lib/site-packages/osgeo/gdal303.dll'
#GEOS_LIBRARY_PATH='C:/Citylab/be-stadtlabor/venv/Lib/site-packages/osgeo/geos_c.dll'

MEDIA_ROOT =  os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


EMAIL_HOST = '0.0.0.0'
EMAIL_PORT = 1025

# Google Chrome LAX
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SAMESITE = 'None'
SESSION_COOKIE_SAMESITE = 'None'

