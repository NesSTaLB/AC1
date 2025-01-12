"""
Django settings for ac1_management project.

Generated by 'django-admin startproject' using Django 5.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-w_o)7-3w+oqlg62@=9#wlq%+#_1p(lsai9p&m#11gw86(!c^r^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']  # يمكنك تحديد المضيفات المسموح بها هنا

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'management',  # تطبيقك الرئيسي
    'debug_toolbar',  # إضافة Django Debug Toolbar
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',  # إضافة Debug Toolbar Middleware
]

ROOT_URLCONF = 'ac1_management.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # مسار القوالب
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',  # لإضافة MEDIA_URL إلى القوالب
            ],
        },
    },
]

WSGI_APPLICATION = 'ac1_management.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'ar'  # اللغة العربية

TIME_ZONE = 'Asia/Riyadh'  # المنطقة الزمنية للمملكة العربية السعودية

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]  # مسار الملفات الثابتة

# Media files (الملفات التي يرفعها المستخدمون)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# إعدادات الأمان (للاستخدام في الإنتاج)
if not DEBUG:
    SECURE_HSTS_SECONDS = 31536000  # 1 year
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

# إعدادات البريد الإلكتروني (للاستخدام في الإنتاج)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'  # استبدل ببريدك الإلكتروني
EMAIL_HOST_PASSWORD = 'your-email-password'  # استبدل بكلمة مرور البريد الإلكتروني

# إعدادات التخزين المؤقت (Caching)
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
    }
}

# إعدادات الترجمة (Internationalization)
LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale')]  # مسار ملفات الترجمة

# إعدادات تسجيل الدخول
LOGIN_URL = '/login/'  # مسار تسجيل الدخول
LOGIN_REDIRECT_URL = '/'  # الصفحة التي يتم توجيه المستخدم إليها بعد تسجيل الدخول
LOGOUT_REDIRECT_URL = '/'  # الصفحة التي يتم توجيه المستخدم إليها بعد تسجيل الخروج

# إعدادات إضافية لتحسين الأداء
if DEBUG:
    # إضافة Django Debug Toolbar للتطوير
    INTERNAL_IPS = ['127.0.0.1']

# إعدادات لتحسين الأداء في الإنتاج
if not DEBUG:
    # استخدام WhiteNoise لتقديم الملفات الثابتة
    MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# إعدادات لتحسين الأمان
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'

# إعدادات لتحسين تجربة المستخدم
MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

# إعدادات لتحسين الأداء في الإنتاج
if not DEBUG:
    # استخدام قاعدة بيانات PostgreSQL في الإنتاج
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'your-db-name',
            'USER': 'your-db-user',
            'PASSWORD': 'your-db-password',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }

    # استخدام Redis للتخزين المؤقت
    CACHES = {
        'default': {
            'BACKEND': 'django_redis.cache.RedisCache',
            'LOCATION': 'redis://127.0.0.1:6379/1',
            'OPTIONS': {
                'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            }
        }
    }

    # إعدادات لتسجيل الأخطاء
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'file': {
                'level': 'ERROR',
                'class': 'logging.FileHandler',
                'filename': os.path.join(BASE_DIR, 'logs/django_errors.log'),
            },
        },
        'loggers': {
            'django': {
                'handlers': ['file'],
                'level': 'ERROR',
                'propagate': True,
            },
        },
    }

# إعدادات المصادقة المخصصة
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',  # المصادقة الافتراضية
]

# إعدادات نموذج المستخدم المخصص
AUTH_USER_MODEL = 'management.CustomUser'  # استبدل بمسار نموذج المستخدم المخصص إذا كنت تستخدم واحدًا

# إعدادات الجلسات
SESSION_COOKIE_AGE = 1209600  # عمر الجلسة (أسبوعين)
SESSION_SAVE_EVERY_REQUEST = True  # حفظ الجلسة في كل طلب

# إعدادات ملفات الوسائط
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# إعدادات ملفات الثابتة
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# إعدادات الرسائل
from django.contrib.messages import constants as message_constants
MESSAGE_TAGS = {
    message_constants.DEBUG: 'debug',
    message_constants.INFO: 'info',
    message_constants.SUCCESS: 'success',
    message_constants.WARNING: 'warning',
    message_constants.ERROR: 'danger',
}

# إعدادات الترجمة
LANGUAGES = [
    ('ar', 'العربية'),
    ('en', 'English'),
]

# إعدادات الوقت والتاريخ
DATE_FORMAT = 'Y-m-d'
DATETIME_FORMAT = 'Y-m-d H:i:s'
TIME_FORMAT = 'H:i:s'

# إعدادات الترجمة اليدوية
USE_THOUSAND_SEPARATOR = True
THOUSAND_SEPARATOR = ','
NUMBER_GROUPING = 3

# إعدادات الترجمة التلقائية
USE_L10N = True
USE_I18N = True
