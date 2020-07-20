import os

AUTH_USER_MODEL = 'app.Writer'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TEMPLATE_ROOT = os.path.join(BASE_DIR, 'templates')
STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/
SECRET_KEY = '=g#q8kmb3sg-y1nu@z15ox5h!8mou3mgv5jyuc669fd%!^tk*p'
DEBUG = False

ALLOWED_HOSTS = ['192.168.43.63', 'localhost']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app'
]

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

ROOT_URLCONF = 'key_blogs.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_ROOT],
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

STATICFILES_DIRS = [STATIC_DIR, ]

WSGI_APPLICATION = 'key_blogs.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'key_blogs',
        'USER': 'nandanunni',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}

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


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'
MEDIA_URL = '/media/'
LOGIN_URL = '/login/'


EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'argon.intelligence@gmail.com'
EMAIL_HOST_PASSWORD = '1806@two000'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'