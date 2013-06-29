from django.conf.urls import patterns, include, url

from DisasterViz import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'CodeCamp.views.home', name='home'),
    # url(r'^CodeCamp/', include('CodeCamp.foo.urls')),
    url(r'^$',views.index),
    url(r'^Nepal_Zones.svg',views.image),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
