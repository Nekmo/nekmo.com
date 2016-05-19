import os
gettext = lambda s: s
DATA_DIR = os.path.dirname(os.path.dirname(__file__))
"""
Django settings for nekmocom project.

Generated by 'django-admin startproject' using Django 1.8.12.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

_ = lambda x: x

try:
    from ..secrets import settings as secrets
except ImportError:
    import warnings
    warnings.warn("Secrets is not available!")
    secrets = None


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*#kuxl=u1a=scg5o3*xupo3!v^y7!8uku56z$$=kgaza(d&3uv'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

ROOT_URLCONF = 'nekmocom.urls'

WSGI_APPLICATION = 'nekmocom.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'Europe/Madrid'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(DATA_DIR, 'media')
STATIC_ROOT = os.path.join(DATA_DIR, 'static')

SITE_ID = 1


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'nekmocom', 'templates'),],
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.i18n',
                'django.core.context_processors.debug',
                'django.core.context_processors.request',
                'django.core.context_processors.media',
                'django.core.context_processors.csrf',
                'django.core.context_processors.tz',
                'sekizai.context_processors.sekizai',
                'django.core.context_processors.static',
                'cms.context_processors.cms_settings',

                'aldryn_boilerplates.context_processors.boilerplate',
                'cms_bs3_theme.context_processors.settings',
                'nekmocom.context_processors.common',

            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'aldryn_boilerplates.template_loaders.AppDirectoriesLoader',
                'django.template.loaders.app_directories.Loader',
                'django.template.loaders.eggs.Loader',
            ],
        },
    },
]

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'aldryn_boilerplates.staticfile_finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

MIDDLEWARE_CLASSES = (
    # Minify HTML
    'htmlmin.middleware.HtmlMinifyMiddleware',
    'htmlmin.middleware.MarkRequestMiddleware',
    'cms.middleware.utils.ApphookReloadMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
)

INSTALLED_APPS = (
    'djangocms_admin_style',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'cms',
    'menus',
    'sekizai',
    'treebeard',
    'meta',

    'ckeditor_filebrowser_filer',


    'djangocms_text_ckeditor',
    'djangocms_style',
    'djangocms_column',
    'djangocms_file',
    'djangocms_googlemap',
    'djangocms_inherit',
    'djangocms_link',
    'djangocms_picture',
    'djangocms_teaser',
    'djangocms_video',
    'reversion',

    'cms_bs3_theme',
    'nekmocom',

    'aldryn_apphooks_config',
    'aldryn_boilerplates',
    'aldryn_categories',
    'aldryn_common',
    'aldryn_newsblog',
    'aldryn_people',
    'aldryn_reversion',
    'aldryn_translation_tools',
    'easy_thumbnails',
    'filer',
    'parler',
    'sortedm2m',
    'taggit',
    'djangocms_snippet',

    'cmsplugin_filer_file',
    'cmsplugin_filer_folder',
    'cmsplugin_filer_link',
    'cmsplugin_filer_teaser',
    'cmsplugin_filer_video',

    'bootstrap3',
    'aldryn_bootstrap3',

    'djangocms_comments',

    'djangocms_page_meta',

    # 'nektheme',
)

# activate django-tools DynamicSiteMiddleware:
USE_DYNAMIC_SITE_MIDDLEWARE = True


LANGUAGES = (
    # Customize this
    ('es', gettext('es')),
    ('en', gettext('en')),
)

CMS_LANGUAGES = {
    # Customize this
    1: [
        {
            'code': 'es',
            'public': True,
            'hide_untranslated': False,
            'redirect_on_fallback': True,
            'name': gettext('es'),
        },
        {
            'code': 'en',
            'public': True,
            'hide_untranslated': False,
            'redirect_on_fallback': True,
            'name': gettext('en'),
        },
    ],
    'default': {
        'fallbacks': ['es', 'en'],
        'redirect_on_fallback': True,
        'hide_untranslated': False,
        'public': True,
    },
}

# CMS_TEMPLATES = (
#     # Customize this
#     ('fullwidth.html', 'Fullwidth'),
#     ('sidebar_left.html', 'Sidebar Left'),
#     ('sidebar_right.html', 'Sidebar Right'),
#     ('tpl_home.html', 'Home Template'),
# )

CMS_TEMPLATES = (
    # ('cms_bs3_theme/page.html', 'BS3 Page'),
    ('cms_bs3_theme/fullwidth.html', 'BS3 Fullwidth'),
    ('cms_bs3_theme/sidebar_right.html', 'BS3 Sidebar Right'),
    ('cms_bs3_theme/sidebar_left.html', 'BS3 Sidebar Left'),
    ('cms_bs3_theme/feature.html', 'BS3 Feature'),
    ('cms_bs3_theme/landscape.html', 'BS3 Landscape'),
    ('nekmocom/home.html', 'BS3 Home'),
    ('sidebar_right.html', 'NekTheme Sidebar right'),
)

CMS_PERMISSION = True

ALDRYN_BOILERPLATE_NAME = 'bootstrap3'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}

MIGRATION_MODULES = {
    
}

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)
META_SITE_PROTOCOL = 'http'
META_USE_SITES = True

PARLER_LANGUAGES = {
    1: (
        {'code': 'es'},
        {'code': 'en'},
    ),
    'default': {
        'fallbacks': ['es', 'en'],
    }
}

BOOTSTRAP3 = {
    'horizontal_label_class': 'col-md-6',

    # Field class to use in horizontal forms
    'horizontal_field_class': 'col-md-18',
}

# CKEDITOR_SETTINGS = {
#     'language': '',
#     'skin': 'moono',
#     'toolbar': 'CMS',
#     'toolbar_HTMLField': [
#         ['Undo', 'Redo'],
#         ['cmsplugins', '-', 'ShowBlocks'],
#         ['Format', 'Styles'],
#         ['TextColor', 'BGColor', '-', 'PasteText', 'PasteFromWord'],
#         ['Maximize', ''],
#         '/',
#         ['Bold', 'Italic', 'Underline', '-', 'Subscript', 'Superscript', '-', 'RemoveFormat'],
#         ['JustifyLeft', 'JustifyCenter', 'JustifyRight'],
#         ['Link', 'Unlink'],
#         ['HorizontalRule'],
#         ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Table', 'FilerImage'],
#         ['Source']
#     ],
#     'extraPlugins': 'filerimage',
#     'removePlugins': 'image',
# }

CMS_PLACEHOLDER_CONF = {
    'post_content': {
        'default_plugins': [
            {
                'plugin_type': 'TextPlugin',
                'values': {
                    'body': '<p>Lorem ipsum dolor sit amet...</p>',
                },
            },
        ]
    },
}

CMS_STYLE_NAMES = (
    ('section-gray', _("Gray section")),
    ('container', _("Container")),
    ('hint', _("hint")),
)


SPAM_PROTECTION = {'default': {'BACKEND': 'djangocms_comments.spam.Akismet',
                               'TOKEN': getattr(secrets, 'AKISMET_API_KEY', ''), 'IS_TEST': True}}

BOOTSTRAP3_THEME = 'nekmocom'
BOOTSTRAP3_COLS = 24
BOOTSTRAP3_SIDEBAR_COLS = 6
BOOTSTRAP3_MENU_TEMPLATE = 'cms_bs3_theme/menus/fluid-static-top-default.html'

META_USE_GOOGLEPLUS_PROPERTIES = True
META_USE_TWITTER_PROPERTIES = True
META_USE_OG_PROPERTIES= True