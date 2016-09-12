from __future__ import absolute_import, unicode_literals

import dj_database_url
from .base import *

DEBUG = False
DATABASES['default'] = dj_database_url.config()

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['cosio.herokuapp.com']
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)


try:
    from .local import *
except ImportError:
    pass
