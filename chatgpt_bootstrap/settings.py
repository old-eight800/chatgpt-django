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

INTERNAL_IPS = ['127.0.0.1']

# Application definition

INSTALLED_APPS = [
    'simpleui', # 管理后台
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'debug_toolbar',
    'chatgpt_user',
    'captcha',
    'rest_framework',
    'drf_yasg',
    'django_apscheduler',
    'django_comment_migrate',
    'chatgpt_chat',
    'chatgpt_image',
    'chatgpt_config',
    'chatgpt_usage',
]

DCM_COMMENT_APP=['app']

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
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
import sqlite3
conn = sqlite3.connect('./db.sqlite3')
c = conn.cursor()
cursor = c.execute("SELECT config_Code, key, value from chatgpt_config")
email_config_dict = {}
for row in cursor:
  if row[0]=='email_config':
    email_config_dict.update({row[1]:row[2]})

EMAIL_BACKEND = email_config_dict['EMAIL_BACKEND']
EMAIL_HOST = email_config_dict['EMAIL_HOST']
EMAIL_PORT = email_config_dict['EMAIL_PORT']
EMAIL_HOST_USER = email_config_dict['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = email_config_dict['EMAIL_HOST_PASSWORD']
EMAIL_TIMEOUT = 10
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = email_config_dict['DEFAULT_FROM_EMAIL']
VERIFICATION_REDIRECT_URL = email_config_dict['VERIFICATION_REDIRECT_URL']
EMAIL_SUBJECT = email_config_dict['EMAIL_SUBJECT']

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
        'user': '50/min'    # 登录认证用户每分钟所有接口总计访问次数
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
# ****************SIMPLEUI配置  ******************** #
# ================================================= #

SIMPLEUI_LOGO = 'https://wiki.hichat.shop/assets/avatar-dd2fb972.jpg' 
SIMPLEUI_HOME_INFO = False # 隐藏右侧SimpleUI广告链接和使用分析
SIMPLEUI_ANALYSIS = False # 隐藏右侧SimpleUI广告链接和使用分析
# SIMPLEUI_HOME_INFO = True

SIMPLEUI_HOME_PAGE = '/user/dashboard/' # 指向新创建的控制面板
SIMPLEUI_HOME_TITLE = 'dashboard'
SIMPLEUI_HOME_ICON = 'fa fa-eye'

# ================================================= #
# ****************  聚合图床配置  ****************** #
# ================================================= #
"""
用于将chatgpt生成的图片转存到配置的图床中,暂未生效
"""
SUPERBED_TOKEN = os.environ.get("SUPERBED_TOKEN")
SUPERBED_URL = os.environ.get("SUPERBED_URL")

# ================================================= #
# **************** 缓冲文件数据配置  **************** #
# ================================================= #
FILE_UPLOAD_MAX_MEMORY_SIZE = 52428800  # 50 MB
DATA_UPLOAD_MAX_MEMORY_SIZE = 52428800  # 50 MB

