from pathlib import Path
from environs import Env

# Initialize the env object
env = Env()
env.read_env()  # Reads the .env file if it exists

# Basic settings
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = env.str("SECRET_KEY")
DEBUG = env.bool("DEBUG", default=False)  # Default to False if DEBUG is not set
DATABASES = {
    "default": env.dj_db_url("DATABASE_URL", default="sqlite:///db.sqlite3")  # Read DATABASE_URL, default to SQLite if not set
}

# Allowed Hosts
ALLOWED_HOSTS = ['.herokuapp.com', 'localhost', '127.0.0.1']

# Installed Apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',  # new
    'accounts',  # new
    'pages',  # new
    'articles',  # new
    'whitenoise.runserver_nostatic',  # new: WhiteNoise to handle static files during development
]

# Middleware settings
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # new: WhiteNoise middleware for serving static files
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Time Zone and Language settings
TIME_ZONE = 'America/New_York'
LANGUAGE_CODE = 'en-us'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files settings
STATIC_URL = '/static/'
STATICFILES_DIRS = [str(BASE_DIR.joinpath('static'))]  # new: additional locations to search for static files
STATIC_ROOT = str(BASE_DIR.joinpath('staticfiles'))  # new: the directory where collected static files will be stored

# WhiteNoise for handling static file storage
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'  # new: uses WhiteNoise to compress and serve static files efficiently

# Custom User Model
AUTH_USER_MODEL = 'accounts.CustomUser'

# Login and Logout Redirect URLs
LOGIN_REDIRECT_URL = 'home'  # new
LOGOUT_REDIRECT_URL = 'home'  # new

# Crispy Forms template pack
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Email Settings for SendGrid
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'apikey'  # This is fixed (for SendGrid)
EMAIL_HOST_PASSWORD = 'your_sendgrid_api_key'  # Your actual SendGrid API key
DEFAULT_FROM_EMAIL = 'you@yourdomain.com'  # This should be the email you verified

# Database settings (uses DATABASE_URL from environment)
DATABASES = {
    'default': env.dj_db_url('DATABASE_URL', default='sqlite:///db.sqlite3')  # Default to SQLite if DATABASE_URL is not set
}

# Password validation settings
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Additional settings such as template configurations, URL configurations, etc., can follow here.
