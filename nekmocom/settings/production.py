from .defaults import *

SECRET_KEY = getattr(secrets, 'SECRET_KEY', SECRET_KEY)
DATABASES = getattr(secrets, 'DATABASES', DATABASES)

DEBUG = False
ALLOWED_HOSTS = ['*']
STATIC_ROOT = os.path.expanduser('~/Static')
MEDIA_ROOT = os.path.expanduser('~/Media')


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
                'filename': os.path.expanduser('~/Log/{}.err'.format(name)),
            },
            'file-debug': {
                'level': 'DEBUG',
                'class': 'logging.handlers.RotatingFileHandler',
                'maxBytes': 1024 * 1024 * 20,  # 20MB
                'backupCount': 3,
                'filename': os.path.expanduser('~/Log/{}.log'.format(name)),
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
