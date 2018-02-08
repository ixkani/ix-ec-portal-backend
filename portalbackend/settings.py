"""
Django settings for portalbackend project.

Generated by 'django-admin startproject' using Django 1.11.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import datetime
import os

import dj_database_url
from corsheaders.defaults import default_headers

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# todo: set this up on heroku, or possibly S3
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# todo: fix this for production
SECRET_KEY = os.environ.get('SECRET_KEY', '%p37+p0!hdk$awrqo!m_%1optv1gc$e55uw&nj$blvqy6_mt02')

ENVIRONMENT_DEVELOPMENT = "DEVELOPMENT"
ENVIRONMENT_STAGING = "STAGING"
ENVIRONMENT_PRODUCTION = "PRODUCTION"

# todo: replace this based on environment of the application, Should replace with above variables
environment = ENVIRONMENT_PRODUCTION

# Application definition

INSTALLED_APPS = [
    # for local dev only. remove for production todo: remove for production
    # 'sslserver',

    # our applications, inside project folder
    'portalbackend.lendapi',
    'portalbackend.lendapi.reporting',
    'portalbackend.lendapi.accounts',
    'portalbackend.lendapi.accounting',
    'portalbackend.lendapi.v1',
    'portalbackend.lendapi.v0',
    # rest framework and oauth applications, needed for the models inheritted
    'oauth2_provider',
    'rest_framework',
    'django_filters',
    # documentation module
    'rest_framework_swagger',

    # core django packages
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_json_widget',
    'djangosecure',
    # handles cors headers, self explanatory
    'corsheaders',
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
        'portalbackend.lendapi.v1.accounts.permissions.IsCompanyUser'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'PAGE_SIZE': 10,
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',

    # breaks application, must explicity define renderers/parsers on each
    # function if Content-Type: application/json not present in header, will fail with code 415
    # 'DEFAULT_RENDERER_CLASSES': (
    #    'rest_framework.renderers.JSONRenderer',),
    # 'DEFAULT_PARSER_CLASSES': (
    #    'rest_framework.parsers.JSONParser',)
}

# the default auth user model is now our own object, not django.contrib.auth as default
AUTH_USER_MODEL = 'accounts.User'

# what the requests pass through
MIDDLEWARE = [
    # authentication token detection
    'corsheaders.middleware.CorsMiddleware',
    'oauth2_provider.middleware.OAuth2TokenMiddleware',
    # cors header, might need to be switched, needs more usage with frontend,
    # but dont forget about the order of these

    # Default
    'django.middleware.security.SecurityMiddleware',
    'djangosecure.middleware.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',

    # 3rd party staticfiles handler
    'whitenoise.middleware.WhiteNoiseMiddleware',

    # more default
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'portalbackend.lendapi.v1.accounts.permissions.SessionValidator',

]

CORS_ALLOW_HEADERS = default_headers + (
    'Content-Disposition',
)

# disable in production
# todo: disable before production release
CORS_ORIGIN_ALLOW_ALL = True

# add the portal frontend url
CORS_ORIGIN_WHITELIST = (
    'ec-portal-frontend.herokuapp.com',
    'prod-ec-portal-frontend.herokuapp.com',
    'portal.espressocapital.com',
    'portal.espressocapital.com.herokudns.com',
    'espressocapital--dev.cs50.my.salesforce.com',
)

ROOT_URLCONF = 'portalbackend.urls'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s',
            'datefmt': "%Y-%m-%d %H:%M:%S"
        }
    },
    'handlers': {
        # writes to logfile, rotates daily, local
        'console': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(BASE_DIR,
                                     'logs/django_{}.log'.format(datetime.datetime.now().strftime("%Y_%m_%d"))),
            'formatter': 'verbose',
            'when': 'midnight',
            'backupCount': '60',
        },
        # unused, add 'heroku' to handlers below to add debug logging to heroku logs
        'heroku': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        }
    },
    'loggers': {
        'django': {
            # add heroku here for handlers
            'handlers': ['console'],  # , 'heroku'],
            'level': 'DEBUG',
            'propagate': True
        },
    }
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['portalbackend/templates/'],
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

WSGI_APPLICATION = 'portalbackend.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

try:
    from .databases import DBCONFIG
except ModuleNotFoundError:
    DATABASES = {'default': {'ENGINE': 'django.db.backends.postgresql_psycopg2', 'NAME': 'borrowerportal',
                             'HOST': '', 'PORT': 5432, 'USER': '', 'PASSWORD': ''}}
else:
    DATABASES = DBCONFIG

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
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Update database configuration with $DATABASE_URL.
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
LOGIN_URL = '/login'

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = [
    # os.path.join(BASE_DIR, 'static'),
    # os.path.join(STATIC_ROOT, 'static'),
    os.path.join(PROJECT_ROOT, 'static')
]

if environment == ENVIRONMENT_DEVELOPMENT:

    DEBUG = True

    # Quickbooks
    # TODO: Only for identity,need to remove once confirmed, CLIENT_ID & CLIENT_SECRET
    QBO_AUTH_REDIRECT_URL = "http://localhost:4200/coa-match/quickbooks"
    QBO_AUTH_CANCEL_URL = "http://localhost:4200/sync"
    CLIENT_ID = 'Q0W1osEOriGM0rwlt7ZBE2ArpDAuczZyDxUmQyx6neVBbU4lkI'
    CLIENT_SECRET = 'RPHtn6oWjCsQuwYyi5j0Jh2M8hl93LsYk934pR81'
    REDIRECT_URI = 'http://localhost:8000/lend/v1/qbo/authCodeHandler'

    # Xero accounting access configuration
    # TODO: Only for identity,need to remove once confirmed, XERO_CONSUMER_KEY & XERO_CONSUMER_SECRET
    XERO_CONSUMER_KEY = 'KHEGRFHVARTOKMGELZ9DYQFOGK1DCH'
    XERO_CONSUMER_SECRET = '5JXM0W7K9HDAKOWQJLNNVRA2ZWSY40'
    XERO_CALL_BACK_URI = 'http://localhost:8000/lend/v1/xero/authCodeHandler'
    XERO_AUTH_VERIFIER_URI = 'http://localhost:8000/lend/v1/xero/authVerifier'

    # FORGOT PASSWORD EMAIL
    FORGOT_PASSWORD_EMAIL_URL = "http://localhost:4200/forgot_password/"

    # EMAIL CONFIGURATION
    EMAIL_ENABLED = False
    EMAIL_HOST_USER = 'vivek.tamilarasan@ionixxtech.com'
    EMAIL_HOST_PASSWORD = 'lifeissimple'
    ADMIN_EMAIL = 'vivek.tamilarasan@ionixxtech.com'

elif environment == ENVIRONMENT_STAGING:

    DEBUG = True

    # QUICKBOOKS
    # TODO: Only for identity,need to remove once confirmed, CLIENT_ID & CLIENT_SECRET
    QBO_AUTH_REDIRECT_URL = os.environ.get('QBO_AUTH_REDIRECT_URL',
                                           "http://wolverine.espressocapital.com/coa-match/quickbooks")
    QBO_AUTH_CANCEL_URL = os.environ.get('QBO_AUTH_CANCEL_URL', "http://wolverine.espressocapital.com/sync")
    CLIENT_ID = os.environ.get('QBO_CLIENT_ID',
                               'Q0UiG1tR7U0AKACCX6hdsusfO3jESCD7I48GO3afqK3yXFO43I')
    CLIENT_SECRET = os.environ.get('QBO_CLIENT_SECRET',
                                   'R30D0n8KCJjmXFoCX6e33SjZl927LbFcsNhpleOW')
    REDIRECT_URI = os.environ.get('QBO_REDIRECT_URI',
                                  'https://ec-portal-backend.herokuapp.com/lend/v1/qbo/authCodeHandler')

    # XERO
    # TODO: Only for identity,need to remove once confirmed, XERO_CONSUMER_KEY & XERO_CONSUMER_SECRET
    XERO_CONSUMER_KEY = 'RFIHMTMEP9FA1UOEPLMLK3EFC5SBSM'
    XERO_CONSUMER_SECRET = 'PULH0QMOXALVHC69PSYMXLZWHLW7SV'
    XERO_CALL_BACK_URI = 'https://ec-portal-backend.herokuapp.com/lend/v1/xero/authCodeHandler'
    XERO_AUTH_VERIFIER_URI = 'https://ec-portal-backend.herokuapp.com/lend/v1/xero/authVerifier'

    # FORGOT PASSWORD EMAIL
    FORGOT_PASSWORD_EMAIL_URL = os.environ.get('FORGOT_PASSWORD_EMAIL_URL',
                                               "http://wolverine.espressocapital.com/forgot_password/")

    # EMAIL CONFIGURATION
    EMAIL_ENABLED = True
    EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', 'vivek.tamilarasan@ionixxtech.com')
    EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', 'lifeissimple')
    ADMIN_EMAIL = os.environ.get('ADMIN_EMAIL', 'vivek.tamilarasan@ionixxtech.com')

elif environment == ENVIRONMENT_PRODUCTION:

    # SECURITY WARNING: don't run with debug turned on in production!
    # todo: fix this for production

    # Debug should be false for verify the valid URL

    DEBUG = False

    if DEBUG is True:
        print("\n**DEBUG is set as True in production environment, It should be changed to False inorder to run the "
              "application in production\n")
        raise ValueError

    # Environment Check
    # Add all the variables in this list to prevalidate the environment
    environment_variable_check = ['DATABASE_URL', 'DISABLE_COLLECTSTATIC', 'FIXIE_URL',
                                  'FORGOT_PASSWORD_EMAIL_URL', 'MAKE_SAVE_CALL_TO_ALL_SIGHT',
                                  'MONITORING_REDIRECT_PAGE', 'ALLSIGHT_URL', 'PAPERTRAIL_API_TOKEN', 'PROXY_REQUIRED',
                                  'QBO_AUTH_CANCEL_URL', 'QBO_AUTH_REDIRECT_URL', 'QBO_BASEURL',
                                  'QBO_CLIENT_ID', 'QBO_CLIENT_SECRET', 'QBO_DISCOVERY_DOCUMENT', 'QBO_PROFILE_URL',
                                  'QBO_REDIRECT_URI', 'QUICKBOOKS_DESKTOP_APP_FILE_NAME',
                                  'QUICKBOOKS_DESKTOP_APP_VERSION', 'REDIS_URL', 'SECRET_KEY',
                                  'EMAIL_HOST_USER', 'EMAIL_HOST_PASSWORD', 'ADMIN_EMAIL', 'ESPRESSO_COMPANY_ID','XERO_AUTH_REDIRECT_URL']
    # Add all the variables in this list to ignore from prevalidation the environment
    environment_variable_uncheck = ['ALLSIGHT_URL']
    for environment in environment_variable_check:
        if environment in environment_variable_uncheck:
            continue
        env_value = os.environ.get(environment)
        if env_value == "" or env_value is None:
            print("This should match the variables defined in Heroku.Env.Vars list.")
            print("\nVariable " + environment + " need to be filled and cannot be empty\n")
            raise EnvironmentError

    # QUICKBOOKS
    QBO_AUTH_REDIRECT_URL = os.environ.get('QBO_AUTH_REDIRECT_URL')
    QBO_AUTH_CANCEL_URL = os.environ.get('QBO_AUTH_CANCEL_URL')
    CLIENT_ID = os.environ.get('QBO_CLIENT_ID')
    CLIENT_SECRET = os.environ.get('QBO_CLIENT_SECRET')
    REDIRECT_URI = os.environ.get('QBO_REDIRECT_URI')

    # XERO
    XERO_CONSUMER_KEY = os.environ.get('XERO_CONSUMER_KEY')
    XERO_CONSUMER_SECRET = os.environ.get('XERO_CONSUMER_SECRET')
    XERO_CALL_BACK_URI = os.environ.get('XERO_CALL_BACK_URI')
    XERO_AUTH_VERIFIER_URI = os.environ.get('XERO_AUTH_VERIFIER_URI')
    XERO_ACCOUNT_TYPE = os.environ.get('XERO_ACCOUNT_TYPE')
    XERO_AUTH_REDIRECT_URL = os.environ.get('XERO_AUTH_REDIRECT_URL')

    # FORGOT PASSWORD EMAIL
    FORGOT_PASSWORD_EMAIL_URL = os.environ.get('FORGOT_PASSWORD_EMAIL_URL')

    # EMAIL CONFIGURATION
    EMAIL_ENABLED = True
    EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', 'vivek.tamilarasan@ionixxtech.com')
    EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', 'lifeissimple')
    ADMIN_EMAIL = os.environ.get('ADMIN_EMAIL', 'vivek.tamilarasan@ionixxtech.com')

# Celery configuration
# task queue? some kinda queue
BROKER_URL = os.environ.get('REDIS_URL', 'redis://localhost:6379/0')
BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 3600}
# where the results are stored
CELERY_RESULT_BACKEND = os.environ.get('REDIS_URL', 'redis://localhost:6379/0')

# Quickbooks Configuration
# OAuth specific variables, also quickbooks,
# QBO Auth - Defaults to Sandbox if env vars aren't found
DISCOVERY_DOCUMENT = os.environ.get('QBO_DISCOVERY_DOCUMENT',
                                    'https://developer.api.intuit.com/.well-known/openid_sandbox_configuration/')

ACCOUNTING_SCOPE = 'com.intuit.quickbooks.accounting'

GET_APP_SCOPES = ['com.intuit.quickbooks.accounting']  # , 'openid','profile','email','phone','address'

# todo: this shouldn't be called SANDBOX, since it's used for both testing and production
#       it currently works because it's assigned from the proper environment variable
#       but just looking at the code where it's used and seeing SANDBOX, is confusing.
SANDBOX_QBO_BASEURL = os.environ.get('QBO_BASEURL', 'https://sandbox-quickbooks.api.intuit.com')

###########
# todo: these don't appear to be used, look at QBO code and if not used then remove
SANDBOX_PROFILE_URL = os.environ.get('QBO_PROFILE_URL',
                                     'https://sandbox-accounts.platform.intuit.com/v1/openid_connect/userinfo')
OPENID_SCOPES = []
ID_TOKEN_ISSUER = 'https://oauth.platform.intuit.com/op/v1'
############

# XERO Configuration
XERO_BASE_URL = "https://api.xero.com"
REQUEST_TOKEN_URL = "/oauth/RequestToken"
AUTHORIZE_URL = "/oauth/Authorize"
ACCESS_TOKEN_URL = "/oauth/AccessToken"
XERO_API_URL = "/api.xro/2.0"
XERO_FILES_URL = "/files.xro/1.0"
XERO_PAYROLL_URL = "/payroll.xro/1.0"

# Email Configuration
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
OAUTH2_PROVIDER_ACCESS_TOKEN_MODEL = 'oauth2_provider.AccessToken'

DEVELOPMENT_TESTING_IP = "210.18.176.194"
ESPRESSO_COMPANY_ID = os.environ.get('ESPRESSO_COMPANY_ID', 1)
CELERY_IMPORTS = ('portalbackend.lendapi.v1.accounting.tasks',)
