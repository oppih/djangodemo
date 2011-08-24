from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('polls.views',
    # Examples:
    # url(r'^$', 'djangodemo.views.home', name='home'),
    # url(r'^djangodemo/', include('djangodemo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^polls/$', 'index'),
    (r'^polls/(?P<poll_id>\d+)/$','detail'),
    (r'^polls/(?P<poll_id>\d+)/results/$','results'),
    (r'^polls/(?P<poll_id>\d+)/vote/$','vote'),
)

urlpatterns += patterns('',
    (r'^admin/', include(admin.site.urls)),
    )
