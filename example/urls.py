from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^simple/', include('simple.urls')),
    url(r'^', include('simple.urls')),
)