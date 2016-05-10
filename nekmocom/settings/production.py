from .defaults import *

SECRET_KEY = getattr(secrets, 'SECRET_KEY', SECRET_KEY)
DATABASES = getattr(secrets, 'DATABASES', DATABASES)
