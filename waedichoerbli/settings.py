"""
Django settings for waedichoerbli project.
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('JUNTAGRICO_SECRET_KEY')

DEBUG = os.environ.get("JUNTAGRICO_DEBUG", 'False')=='True'

ALLOWED_HOSTS = ['junto.waedichoerbli.ch','waedichoerbli.juntagrico.science', 'localhost',]



# Application definition

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'juntagrico',
    'impersonate',
    'crispy_forms',
    'waedichoerbli',
    'adminsortable2',
    'juntagrico_assignment_request',
]

ROOT_URLCONF = 'waedichoerbli.urls'

DATABASES = {   
    'default': {
        'ENGINE': os.environ.get('JUNTAGRICO_DATABASE_ENGINE','django.db.backends.postgresql'), 
        'NAME': os.environ.get('JUNTAGRICO_DATABASE_NAME','waedichoerbli'), 
        'USER': os.environ.get('JUNTAGRICO_DATABASE_USER', 'lucash'),
        'PASSWORD': os.environ.get('JUNTAGRICO_DATABASE_PASSWORD', 'xxxxxxx'),
        'HOST': os.environ.get('JUNTAGRICO_DATABASE_HOST', 'xx.xx.xx.xx'),
        'PORT': os.environ.get('JUNTAGRICO_DATABASE_PORT', '28087'),
    }
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.request',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader'
            ],
            'debug' : True
        },
    },
]

WSGI_APPLICATION = 'waedichoerbli.wsgi.application'


LANGUAGE_CODE = 'de'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

DATE_INPUT_FORMATS =['%d.%m.%Y',]

AUTHENTICATION_BACKENDS = (
    'juntagrico.util.auth.AuthenticateWithEmail',
    'django.contrib.auth.backends.ModelBackend'
)


MIDDLEWARE = [
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'impersonate.middleware.ImpersonateMiddleware'
]

EMAIL_HOST = os.environ.get('JUNTAGRICO_EMAIL_HOST')
EMAIL_HOST_USER = os.environ.get('JUNTAGRICO_EMAIL_USER')
EMAIL_HOST_PASSWORD = os.environ.get('JUNTAGRICO_EMAIL_PASSWORD')
EMAIL_PORT = int(os.environ.get('JUNTAGRICO_EMAIL_PORT', '25' ))
EMAIL_USE_TLS = os.environ.get('JUNTAGRICO_EMAIL_TLS', 'False')=='True'
EMAIL_USE_SSL = os.environ.get('JUNTAGRICO_EMAIL_SSL', 'False')=='True'

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'

WHITELIST_EMAILS = []

def whitelist_email_from_env(var_env_name):
    email = os.environ.get(var_env_name)
    if email:
        WHITELIST_EMAILS.append(email.replace('@gmail.com', '(\+\S+)?@gmail.com'))


if DEBUG is True:
    for key in os.environ.keys():
        if key.startswith("JUNTAGRICO_EMAIL_WHITELISTED"):
            whitelist_email_from_env(key)
            


STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

IMPERSONATE = {
    'REDIRECT_URL': '/my/profile',
}

LOGIN_REDIRECT_URL = "/my/home"

"""
    File & Storage Settings
"""
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

MEDIA_ROOT = 'media'

"""
     Crispy Settings
"""
CRISPY_TEMPLATE_PACK = 'bootstrap4'

"""
     Juntagrico Settings
"""
ORGANISATION_NAME = "Wädichörbli"
ORGANISATION_LONG_NAME = "Genossenschaft Wädichörbli"
ORGANISATION_ADDRESS = {"name":"Genossenschaft Wädichörbli", 
            "street" : "Froh Ussicht",
            "number" : "",
            "zip" : "8833",
            "city" : "Samstagern",
            "extra" : "Tel. 077 485 67 78"}

"""
 Accounting
"""            
ORGANISATION_BANK_CONNECTION = {"PC" : "46-110-7",
            "IBAN" : "CH41 0839 0031 8837 1000 9",
            "BIC" : "ABSOCH22",
            "NAME" : "Alternative Bank Schweiz AG",
            "ESR" : "01-9252-0"}
CURRENCY= "CHF"   
SHARE_PRICE = "300"

BUSINESS_YEAR_START = {"day":1, "month":6}
BUSINESS_YEAR_CANCELATION_MONTH = 2
MEMBERSHIP_END_MONTH = 5

"""
  Outgoing-Mail Settings
"""  
INFO_EMAIL = "info@waedichoerbli.ch"
SERVER_URL = "junto.waedichoerbli.ch"
ADMINPORTAL_NAME = "Wädichörbli"
ADMINPORTAL_SERVER_URL = "junto.waedichoerbli.ch"
DEFAULT_FROM_EMAIL = "info@waedichoerbli.ch"
STYLE_SHEET = "/static/waedichoerbli/css/customize.css"

MAIL_TEMPLATE = "mails/email.html"
EMAILS = {
    'password': 'waedichoerbli_emails/member/password_reset_mail.txt',
    's_created': 'waedichoerbli_emails/member/share_created.txt',
}

"""
    Jobs
""" 
ASSIGNMENT_UNIT = "HOURS"

"""
    Depots
"""
DEPOT_LIST_GENERATION_DAYS = [0]

"""
   Appereance
"""
VOCABULARY = {'package': 'Kiste'}

"""
   External Documents
"""
BUSINESS_REGULATIONS = "https://waedichoerbli.ch/dokumente/Betriebsreglement_Waedichoerbli.pdf"
BYLAWS = "https://waedichoerbli.ch/dokumente/Statuten_Waedichoerbli.pdf"

""" 
  Logging
"""  
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'waedichoerbli-django.log',
            'maxBytes': 1024*1024*1, # 1 MB
            'backupCount': 5,
        },
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file', 'console'],
            'propagate': True,
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO')
        },
        'juntagrico.mailer': {
            'handlers': ['file', 'console'],
            'propagate': True,
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO')
        },
    },
}

