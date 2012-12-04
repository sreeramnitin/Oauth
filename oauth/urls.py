from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'auth/$','myapp.views.auth'),
    url(r'^$','myapp.views.index'),
	url(r'agiliq/$','myapp.views.agiliq')
    # Examples:
    # url(r'^$', 'oauth.views.home', name='home'),
    # url(r'^oauth/', include('oauth.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
