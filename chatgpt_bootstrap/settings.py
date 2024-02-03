"""
Django settings for chatgpt_bootstrap project.

Generated by 'django-admin startproject' using Django 4.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
from loguru import logger
import os
import sys
from datetime import timedelta
from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv(".env"))

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-g79*q+_qc^o9#3d5+9taxzt8cur&49!u@em340w9tkkqm^h(7x'

# SECURITY WARNING: don't run with debug turned on in production!
if 'win' in sys.platform:
  DEBUG = True 
else:
  DEBUG = False

ALLOWED_HOSTS = ['*']


CSRF_TRUSTED_ORIGINS = ['http://54.165.238.232']
# 54.165.238.232


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'chatgpt_user',
    'captcha',
    'rest_framework',
    'drf_yasg',
    'django_comment_migrate',
    'chatgpt_chat',
    'chatgpt_image',
    'django_apscheduler',
    'chatgpt_config',
    'django_celery_results',
    'chatgpt_usage',
]

DCM_COMMENT_APP=['app']

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

SECURE_CROSS_ORIGIN_OPENER_POLICY = 'None'

ROOT_URLCONF = 'chatgpt_bootstrap.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "static", "template")],
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

WSGI_APPLICATION = 'chatgpt_bootstrap.wsgi.app'

APPEND_SLASH = False
# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
 

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "zh-hans"

TIME_ZONE = "Asia/Shanghai"

USE_I18N = False

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static", "template"),
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 重新指定usermodel
"""
在创建任何迁移或者第一次运行 manager.py migrate 前设置 AUTH_USER_MODEL。
设置AUTH_USER_MODEL对你的数据库结构有很大的影响。它改变了一些会使用到的表格，
并且会影响到一些外键和多对多关系的构造。在你有表格被创建后更改此设置是不被 makemigrations 支持的，
并且会导致你需要手动修改数据库结构，从旧用户表中导出数据，可能重新应用一些迁移。
"""
AUTH_USER_MODEL = 'chatgpt_user.FrontUserBase'

# ================================================= #
# **************** 验证码配置  ******************* #
# ================================================= #
CAPTCHA_IMAGE_SIZE = (160, 60)  # 设置 captcha 图片大小
CAPTCHA_LENGTH = 6  # 字符个数
CAPTCHA_TIMEOUT = 5  # 超时(minutes)
CAPTCHA_OUTPUT_FORMAT = "%(image)s %(text_field)s %(hidden_field)s "
CAPTCHA_FONT_SIZE = 30  # 字体大小
CAPTCHA_FOREGROUND_COLOR = "#d2447e"  # 前景色
CAPTCHA_BACKGROUND_COLOR = "#F5F7F4"  # 背景色
CAPTCHA_NOISE_FUNCTIONS = (
    "captcha.helpers.noise_arcs",  # 线
    "captcha.helpers.noise_dots",  # 点
)
CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.random_char_challenge' #字母验证码
# CAPTCHA_CHALLENGE_FUNCT = "captcha.helpers.math_challenge"  # 加减乘除验证码



# ================================================= #
# **************** 邮件配置  ******************* #
# ================================================= #
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ.get("EMAIL_HOST")
EMAIL_PORT = os.environ.get("EMAIL_PORT")
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
EMAIL_TIMEOUT = 10
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = os.environ.get("DEFAULT_FROM_EMAIL")
VERIFICATION_REDIRECT_URL = 'http://wiki.hichat.shop/#/emailValidation?type=email&verifyCode='
EMAIL_SUBJECT = 'AI-Chat 验证'

# ================================================= #
# **************** 日志配置  ******************* #
# ================================================= #
logger_format = "{time:YYYY-MM-DD HH:mm:ss,SSS} [{thread}] {level} {file} {line} - {message}"
logger.add("log/backend.{time:YYYY-MM-DD}.log", rotation="00:00", encoding='utf-8')



# ================================================= #
# **************** REST_FRAMEWORK配置  ************ #
# ================================================= #
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',  # jwt认证方案
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',  # 接口访问权限默认为 允许所有人
    ],
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',   # 限制未认证用户的请求频率
        'rest_framework.throttling.UserRateThrottle',   # 限定认证用户的请求频率

    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '10/min',    # 匿名用户或未登录用户每分钟所有接口总计访问次数
        'user': '50/min'    # 登录认证用户 每分钟所有接口总计访问次数
    },
    'EXCEPTION_HANDLER': 'utils.exception.Custom_exception_handler'  # 自定义的异常处理
}



# ================================================= #
# **************** Simple JWT配置     ************* #
# ================================================= #
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=3), # access token的时效
}


# ================================================= #
# **************** open ai配置  ******************** #
# ================================================= #

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
OPENAI_API_BASE_URL = os.environ.get("OPENAI_API_BASE_URL")
MODEL = os.environ.get("MODEL")

# ================================================= #
# ****************  聚合图床配置  ****************** #
# ================================================= #
SUPERBED_TOKEN = os.environ.get("SUPERBED_TOKEN")
SUPERBED_URL = os.environ.get("SUPERBED_URL")

# ================================================= #
# **************** 缓冲文件数据配置  **************** #
# ================================================= #
FILE_UPLOAD_MAX_MEMORY_SIZE = 52428800  # 50 MB
DATA_UPLOAD_MAX_MEMORY_SIZE = 52428800  # 50 MB


# ================================================= #
# **************** celery配置  ********************* #
# ================================================= #
# 最重要的配置，设置消息broker,格式为：db://user:password@host:port/dbname
# 如果redis安装在本机，使用localhost
# 如果docker部署的redis，使用redis://redis:6379
CELERY_BROKER_URL = os.environ.get("CELERY_BROKER_URL")

# celery时区设置，建议与Django settings中TIME_ZONE同样时区，防止时差
# Django设置时区需同时设置USE_TZ=True和TIME_ZONE = 'Asia/Shanghai'
CELERY_TIMEZONE = TIME_ZONE
# 为django_celery_results存储Celery任务执行结果设置后台
# 格式为：db+scheme://user:password@host:port/dbname
# 支持数据库django-db和缓存django-cache存储任务状态及结果
CELERY_RESULT_BACKEND = "django-db"
# celery内容等消息的格式设置，默认json
CELERY_ACCEPT_CONTENT = ['application/json', ]
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

# 为任务设置超时时间，单位秒。超时即中止，执行下个任务。
CELERY_TASK_TIME_LIMIT = 5

# 为存储结果设置过期日期，默认1天过期。如果beat开启，Celery每天会自动清除。
# 设为0，存储结果永不过期
CELERY_RESULT_EXPIRES = 1

# 任务限流
CELERY_TASK_ANNOTATIONS = {'tasks.add': {'rate_limit': '10/s'}}

# Worker并发数量，一般默认CPU核数，可以不设置
CELERY_WORKER_CONCURRENCY = 2

# 每个worker执行了多少任务就会死掉，默认是无限的
CELERY_WORKER_MAX_TASKS_PER_CHILD = 200

CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True