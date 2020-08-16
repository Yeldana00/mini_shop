from .cammon import *

ALLOWED_HOSTS = []

DEBUG = True

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, '../static')
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '../data.sqlite3')
    }
}
