from __future__ import absolute_import, unicode_literals

import os
import dj_database_url
from .base import *

ALLOWED_HOSTS = ['*']
DEBUG=True
 

DATABASES['default'] = dj_database_url.config()

SECRET_KEY = os.environ['SECRET_KEY']

#ALLOWED_HOSTS = ['cosio.herokuapp.com']
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))




# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, 'static'),
]

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')



AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = 'cosio'
AWS_QUERYSTRING_AUTH = False

DEFAULT_FILE_STORAGE = 'website.s3utils.S3BotoStorage'
STATICFILES_STORAGE = 'website.s3utils.S3BotoStorage'

STATIC_DIRECTORY = 'static/'
MEDIA_DIRECTORY = 'media/'

STATIC_URL = 'http://' + AWS_STORAGE_BUCKET_NAME + '.s3.amazonaws.com/' + STATIC_DIRECTORY
MEDIA_URL = 'http://' + AWS_STORAGE_BUCKET_NAME + '.s3.amazonaws.com/' + MEDIA_DIRECTORY
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

try:
    from .local import *
except ImportError:
    pass
