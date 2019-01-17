"""
Django settings for myset project.

Generated by 'django-admin startproject' using Django 2.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'gu1a@39%%mpx1t+h@2n_(s&0s4xc_m#jog2c=0=ne*=0*(m!fn'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["47.98.117.129",'localhost','0.0.0.0:8888','0.0.0.0:8000','127.0.0.1','192.168.30.200','192.168.30.200:8000']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'weixin.apps.WeixinConfig',
    'shandian.apps.ShandianConfig',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myset.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'myset.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME' : 'shandjjdb',
        'USER': 'gongnanxiong',
        'PASSWORD': 'Yuhan@235',
        'HOST': '192.168.30.122',
        'PORT': '3306',
        'OPTIONS':{
            'init_command':"SET sql_mode='traditional'",
            'charset':'utf8mb4',
        },

        'ATOMIC_REQUEST': True,
    },
    'mytest': {
        'ENGINE': 'django.db.backends.mysql',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'NAME' : 'mytest',
        'USER': 'root',
        'PASSWORD': 'Yuhan235',
        'HOST': '47.98.117.129',
        'PORT': '3306',
        'CHARSET':'utf8',
        'COLLATION':'utf8_general_ci',
        'OPTIONS':{
            'init_command':"SET sql_mode='traditional'",
            'charset':'utf8mb4',
        },
        'ATOMIC_REQUEST': True,
    },
    'permission': {
        'ENGINE': 'django.db.backends.mysql',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'NAME' : 'permission',
        'USER': 'root',
        'PASSWORD': 'Yuhan235',
        'HOST': '47.98.117.129',
        'PORT': '3306',
        'CHARSET':'utf8',
        'COLLATION':'utf8_general_ci',
        'OPTIONS':{
            'init_command':"SET sql_mode='traditional'",
            'charset':'utf8mb4',
        },
        'ATOMIC_REQUEST': True,
    },
    'sms': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME' : 'cbdsms_db',
        'USER': 'gongnanxiong',
        'PASSWORD': 'Yuhan@235',
        'HOST': '192.168.30.122',
        'PORT': '3306',
        'OPTIONS':{
            'init_command':"SET sql_mode='traditional'",
            'charset':'utf8mb4',
        },
        'ATOMIC_REQUEST': True,
    },
    'db1': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME' : 'db1',
        'USER': 'gongnanxiong',
        'PASSWORD': 'Yuhan@235',
        'HOST': '192.168.30.122',
        'PORT': '3306',
        'OPTIONS':{
            'init_command':"SET sql_mode='traditional'",
            'charset':'utf8mb4',
        },
        'ATOMIC_REQUEST': True,
    },
    'db2': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME' : 'db2',
        'USER': 'gongnanxiong',
        'PASSWORD': 'Yuhan@235',
        'HOST': '192.168.30.122',
        'PORT': '3306',
        'OPTIONS':{
            'init_command':"SET sql_mode='traditional'",
            'charset':'utf8mb4',
        },
        'ATOMIC_REQUEST': True,
    },
    'db3': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME' : 'db3',
        'USER': 'gongnanxiong',
        'PASSWORD': 'Yuhan@235',
        'HOST': '192.168.30.122',
        'PORT': '3306',
        'OPTIONS':{
            'init_command':"SET sql_mode='traditional'",
            'charset':'utf8mb4',
        },
        'ATOMIC_REQUEST': True,
    },

}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/abc/'
STATICFILES_DIRS=(
    os.path.join(BASE_DIR,"statics"),
)

# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'formatters': {
#         'simple': {
#             'format': '[%(asctime)s] %(message)s'
#         },
#     },
#     'handlers': {
#         'console': {
#             'level': 'DEBUG',
#             'class': 'logging.StreamHandler',
#             'formatter': 'simple'
#         },
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['console'],
#             'level': 'DEBUG',
#         },
#     },
# }
