from .settings import *
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

DEBUG = False

MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware']
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

ALLOWED_HOSTS = ['oc-lettings-edaucohe.herokuapp.com']

sentry_sdk.init(
    dsn=
    "https://49da25c999164788aabe940edfc65cf5@o4504124745711616.ingest.sentry.io/4504124749971456",
    integrations=[
        DjangoIntegration(),
    ],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)
