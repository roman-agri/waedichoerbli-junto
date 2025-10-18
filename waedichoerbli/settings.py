"""
Django settings for waedichoerbli project.
"""

import os
from django.core.mail import send_mail

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
    'waedichoerbli',
    'juntagrico_assignment_request',
    'juntagrico_billing',
    'juntagrico',  # juntagrico muss neu nach den addons stehen
    'fontawesomefree',  # benötigt ab 1.6
    'import_export',  # benötigt ab 1.6
    'impersonate',
    'crispy_forms',
    'adminsortable2',
    'polymorphic',
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
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # location of your overriding templates
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
    'impersonate.middleware.ImpersonateMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware'
]

# Email config fo django
EMAIL_HOST = os.environ.get('JUNTAGRICO_EMAIL_HOST')
EMAIL_HOST_USER = os.environ.get('JUNTAGRICO_EMAIL_USER')
EMAIL_HOST_PASSWORD = os.environ.get('JUNTAGRICO_EMAIL_PASSWORD')
EMAIL_PORT = int(os.environ.get('JUNTAGRICO_EMAIL_PORT', '25' ))
EMAIL_USE_TLS = os.environ.get('JUNTAGRICO_EMAIL_TLS', 'False')=='True'
EMAIL_USE_SSL = os.environ.get('JUNTAGRICO_EMAIL_SSL', 'False')=='True'

#DEFAULT_MAILER = 'waedichoerbli.mailer.Mailer'

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
            

"""
    base url and css settings
"""
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.ManifestStaticFilesStorage",
    },
}

IMPERSONATE = {
    'REDIRECT_URL': '/my/profile',
    'ALLOW_SUPERUSER': True,
}

LOGIN_REDIRECT_URL = "/"

STYLES = {'static': ['waedichoerbli/css/customize.css']}

"""
    Import & Export Settings
"""
IMPORT_EXPORT_EXPORT_PERMISSION_CODE = 'view'

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
ORGANISATION_PHONE = {"077 485 67 78"}      
      
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
REQUIRED_SHARES=1


"""
  Outgoing-Mail Settings
"""  
CONTACTS = {
    "general": "info@waedichoerbli.ch"
}
ORGANISATION_WEBSITE = {
    'name': "Wädichörbli",
    'url': "https://junto.waedichoerbli.ch"
}
DEFAULT_FROM_EMAIL = "info@waedichoerbli.ch"
MAIL_TEMPLATE = "mails/email.html"
EMAILS = {
    'password': 'waedichoerbli_emails/member/password_reset_mail.txt',
    's_created': 'waedichoerbli_emails/member/share_created.txt',
    'b_sub': 'waedichoerbli_emails/billing/bill_notification.txt',
}

"""
    Jobs
"""    
ASSIGNMENT_UNIT = "HOURS"
ALLOW_JOB_UNSUBSCRIBE="False"

"""
    Depots
"""
DEPOT_LIST_GENERATION_DAYS = [6]

"""
   Appereance
"""
VOCABULARY = {'package': 'Kiste',
              'assignment' : 'Arbeitseinsatz',
              'assignment_pl' : 'Arbeitseinsätze',
              } 

"""
   Juntagrico-Billing
"""
# Anzeige des Rechnungen Menüs für normale Mitglieder
BILLS_USERMENU = True  
# Link zum Fälligkeits-Hinweis Dokument. Falls angegeben wird das auf der Rechnung angezeigt.
DUEDATE_NOTICE_URL= ""


"""
   External Documents
"""
BUSINESS_REGULATIONS = "https://waedichoerbli.ch/dokumente/Betriebsreglement_Waedichoerbli.pdf"
BYLAWS = "https://waedichoerbli.ch/dokumente/Statuten_Waedichoerbli.pdf"


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}
