from .defaults import *

SECRET_KEY = getattr(secrets, 'SECRET_KEY', SECRET_KEY)
DATABASES = getattr(secrets, 'DATABASES', DATABASES)
HOME = getattr(secrets, 'HOME', os.environ.get('HOME', '')).rstrip('/')


def expand_home(path):
    return '{}/{}'.format(HOME, path)


DEBUG = False
ALLOWED_HOSTS = ['*']
STATIC_ROOT = expand_home('Static')
MEDIA_ROOT = expand_home('Media')


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}


def logging(name):
    return {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'file-error': {
                'level': 'ERROR',
                'class': 'logging.handlers.RotatingFileHandler',
                'maxBytes': 1024 * 1024 * 20,  # 20MB
                'backupCount': 3,
                'filename': expand_home('Log/{}.err'.format(name)),
            },
            'file-debug': {
                'level': 'DEBUG',
                'class': 'logging.handlers.RotatingFileHandler',
                'maxBytes': 1024 * 1024 * 20,  # 20MB
                'backupCount': 3,
                'filename': expand_home('Log/{}.log'.format(name)),
            },
        },
        'loggers': {
            'django': {
                'handlers': ['file-error'],
                'level': 'DEBUG',
                'propagate': True,
            },
        },
    }
