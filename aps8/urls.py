from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

# Examples:
# url(r'^$', 'aps8.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^api/', include('api.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
