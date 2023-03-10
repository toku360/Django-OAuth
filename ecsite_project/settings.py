"""
Django settings for ecsite_project project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'hg+es8yb8cl*ljp&3ha3(wqpoxfog!fuqsu$83^@!39!i6!4w9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
#    'django.contrib.sites',
#    'allauth',
#    'allauth.account',
#    'allauth.socialaccount',
#    'allauth.socialaccount.providers.google',
    'accounts',
    'stores',
]

AUTH_USER_MODEL = 'accounts.Users'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend', # デフォルトの認証
    'allauth.account.auth_backends.AuthenticationBackend', # allauthの認証
)

ROOT_URLCONF = 'ecsite_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
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

WSGI_APPLICATION = 'ecsite_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

# LoginRequiredではじかれた場合のリダイレクト先
LOGIN_URL = '/accounts/user_login'
# LoginViewで遷移先が指定されていない場合のリダイレクト先
LOGIN_REDIRECT_URL = '/accounts/home'
# LogoutViewで遷移先が指定されていない場合のリダイレクト先
LOGOUT_REDIRECT_URL = '/accounts/user_login'

# 商品画像
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

#SITE_ID = 1 # django_siteテーブル上のどのサイトを認証に用いるか（基本は1）
#ACCOUNT_EMAIL_REQUIRED = True # 認証にメールアドレスが必要か（デフォルトはFalse）
#ACCOUNT_USERNAME_REQUIRED = False # 認証にユーザ名が必要か（デフォルトはTrue）
#ACCOUNT_AUTHENTICATION_METHOD = 'email' # 何を認証に利用するか（email, username, username_emailから選択）

# プロバイダーごとの設定を記述する
# SOCIALACCOUNT_PROVIDERS = {
#     'google': {
#         'SCOPE': [ # Google APIで何を取得するか
#             'profile','email'
#         ],
#         'AUTH_PARAMS': {
#         'access_type': 'onine', # offlineでのアクセスをする場合はofflineに設定する(offlineとは、ネットにつながっていないことでなく、ユーザーがいない状態（バッチなど）のこと)
    
#         }
#     }
# }
