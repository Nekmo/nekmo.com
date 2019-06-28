from .defaults import *

SECRET_KEY = getattr(secrets, 'SECRET_KEY', SECRET_KEY)
HOME = getattr(secrets, 'HOME', os.environ.get('HOME', '')).rstrip('/')

DATABASES = {
    'default': {
        'CONN_MAX_AGE': 0,
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': 'nekmocom_postgres_1',
        'NAME': os.getenv("POSTGRES_DB"),
        'USER': os.getenv("POSTGRES_USER"),
        'PASSWORD': os.getenv("POSTGRES_PASSWORD"),
        'PORT': '',
    }
}


DEBUG = True
ALLOWED_HOSTS = ['*']
STATIC_ROOT = '/static/'
MEDIA_ROOT = '/media/'


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': 'nekmocom_memcached_1:11211',
    }
}

TEMPLATES[0]['OPTIONS']['loaders'] = [
    ('django.template.loaders.cached.Loader', TEMPLATES[0]['OPTIONS']['loaders']),
]
LOGS_DIRECTORY = '/var/log/gunicorn'


def logging(name):
    if not os.path.lexists(LOGS_DIRECTORY):
        print('Logging is not available for {}!'.format(name))
        return
    return {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'file-error': {
                'level': 'ERROR',
                'class': 'logging.handlers.RotatingFileHandler',
                'maxBytes': 1024 * 1024 * 20,  # 20MB
                'backupCount': 3,
                'filename': os.path.join(LOGS_DIRECTORY, '{}.err'.format(name)),
            },
            'file-debug': {
                'level': 'DEBUG',
                'class': 'logging.handlers.RotatingFileHandler',
                'maxBytes': 1024 * 1024 * 20,  # 20MB
                'backupCount': 3,
                'filename': os.path.join(LOGS_DIRECTORY, '{}.log'.format(name)),
            },
        },
        'loggers': {
            'django': {
                'handlers': ['file-error', 'file-debug'],
                'level': 'DEBUG',
                'propagate': True,
            },
            '': {
                'handlers': ['file-error', 'file-debug'],
                'level': 'DEBUG',
                'propagate': True,
            },
        },
    }

