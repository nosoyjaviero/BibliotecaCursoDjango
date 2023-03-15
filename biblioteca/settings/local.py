from .base import *
# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases




DB_FILE = BASE_DIR.child('db.sqlite3')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': DB_FILE,
    }
}


STATIC_URL = '/static/'

static = BASE_DIR.child('static')
css = static.child('css')
img = static.child('img')
js = static.child('js')

STATICFILES_DIRS = [static, css,img, js,]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'


MEDIA_ROOT =BASE_DIR.child('media')
