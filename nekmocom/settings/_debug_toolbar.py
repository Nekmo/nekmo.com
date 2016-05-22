from .defaults import INSTALLED_APPS, MIDDLEWARE_CLASSES
INSTALLED_APPS = list(INSTALLED_APPS)
INSTALLED_APPS.append('debug_toolbar')

DEBUG = True

MIDDLEWARE_CLASSES = list(MIDDLEWARE_CLASSES)
MIDDLEWARE_CLASSES.insert(1, 'debug_toolbar.middleware.DebugToolbarMiddleware')