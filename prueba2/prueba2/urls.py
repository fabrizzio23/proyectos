from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'principal.views.inicio'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/files_prueba2/(?P<path>.*)$','django.views.static.serve',
		{'document_root':settings.MEDIA_ROOT,}
	),
	url(r'^static/(?P<path>.*)$','django.views.static.serve',
		{'document_root':settings.STATIC_ROOT,}
	),
)
