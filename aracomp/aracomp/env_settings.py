import os
from pathlib import Path
from django.core.exceptions import ImproperlyConfigured


def get_env_value(env_variable):
    try:
        return str(os.environ[env_variable]).strip()
    except KeyError:
        error_msg = f'Set the {env_variable} environment variable'
        raise ImproperlyConfigured(error_msg)


BASE_DIR = Path(__file__).resolve().parent.parent


if get_env_value('ARACOMP_PRODUCTION') == 'FALSE':
    DEBUG = True
    ALLOWED_HOSTS = []
    SECRET_KEY = get_env_value('SECRET_KEY')
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
    
elif get_env_value('ARACOMP_PRODUCTION') == 'TRUE':
    DEBUG = False
    ALLOWED_HOSTS = ['https://aracomp.herokuapp.com']
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True
