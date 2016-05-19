from django.contrib import admin

from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
urlpatterns = [
    # Examples:
    # url(r'^$', 'mydiscovery.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
#    url(r'(?P<routeid>[^/]+)', include('clarito.urls')),
#    url(r'^hith/', include('clarito.urls')),
#    url(r'^hith/$', 'clarito.views.joinroute', name='joinroute'), 
    url(r'^(?P<routeid>[^/]+)/(?P<routename>[^/]+)/$', 'clarito.views.joinroute', name='joinroute'),
    url(r'^customerjoin/(?P<routeid>[^/]+)/(?P<routename>[^/]+)/$', 'clarito.views.customerjoin', name='customerjoin'),
   #url(r'^admin/', include(admin.site.urls)),
]
