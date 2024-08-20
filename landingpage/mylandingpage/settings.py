from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Static files (CSS, JavaScript, Images) configuration
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "comingsoon" / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Deployer specific settings
DEPLOYER = os.getenv('DEPLOYER', 'Vercel')  # You can set this environment variable in Vercel

if DEPLOYER == "Heroku":
    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = os.getenv('SECRET_KEY', 'your-default-secret-key')

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = False

elif DEPLOYER == "Vercel":
    SECRET_KEY = os.getenv('SECRET_KEY', 'your-default-secret-key')
    DEBUG = os.getenv('DEBUG', 'False') == 'True'

# Allowed Hosts
ALLOWED_HOSTS = [
    '.vercel.app',
    'www.nookbio.com',
    'nookbio-landingpage.herokuapp.com',
    'nookbio.com',
    'localhost',
    '127.0.0.1',
    '.herokuapp.com',
    'nookbio-landingpage-b237f8a313ed.herokuapp.com',
]

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

ROOT_URLCONF = "mylandingpage.urls"

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'comingsoon' / 'templates' / 'comingsoon'],  # Paths for templates
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = "mylandingpage.wsgi.application"

# Database
# Default to SQLite, but you might want to switch to a more robust solution for production
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = "static/"

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# CSRF Settings - Add if necessary
CSRF_TRUSTED_ORIGINS = [
    'https://your-vercel-domain.vercel.app',
    'https://your-custom-domain.com',
]
