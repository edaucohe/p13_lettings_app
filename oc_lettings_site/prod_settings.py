from oc_lettings_site.settings import *

DEBUG = False

MIDDLEWARE += [
    "whitenoise.middleware.WhiteNoiseMiddleware",
]
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

ALLOWED_HOSTS = ["oc-lettings-edaucohe.herokuapp.com"]
