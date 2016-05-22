# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from cms.sitemaps import CMSSitemap
from django.conf import settings
from django.conf.urls import *  # NOQA
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = i18n_patterns('',
    url(r'^admin/', include(admin.site.urls)),  # NOQA
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap',
        {'sitemaps': {'cmspages': CMSSitemap}}),
    url(r'^select2/', include('django_select2.urls')),

                            url(r'^filebrowser_filer/', include('ckeditor_filebrowser_filer.urls')),
                            url(r'^filer/', include('filer.urls')),

                            url(r'^', include('cms.urls')),
)

urlpatterns += [
    url(r'^taggit_autosuggest/', include('taggit_autosuggest.urls')),
    url(r'^djangocms_comments/', include('djangocms_comments.urls')),
]

# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns = patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',  # NOQA
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        ) + staticfiles_urlpatterns() + urlpatterns  # NOQA

if 'debug_toolbar' in settings.INSTALLED_APPS:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )

if 'silk' in settings.INSTALLED_APPS:
    urlpatterns += patterns('', url(r'^silk/', include('silk.urls', namespace='silk')))

from . import patch