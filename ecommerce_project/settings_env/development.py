import socket

from ecommerce_project.settings_env.common import *

LOCALHOST = 'localhost'

# INSTALLED_APPS = ['django_pdb'] + INSTALLED_APPS + ['django_extensions']
# MIDDLEWARE = MIDDLEWARE + ['django_pdb.middleware.PdbMiddleware']

DEBUG = True
FORCE_SSL = False

db = {'ENGINE': 'django.db.backends.postgresql',
      'NAME': 'muradb',
      'USER': '',
      'PASSWORD': '',
      'HOST': LOCALHOST,
      'PORT': '',
      'TEST': {'NAME': 'testmuradb', },
      }
DATABASES = {'default': db, 'session': db, }
