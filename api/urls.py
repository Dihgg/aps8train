from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.update, name='update'),
    url(r'^status/$', views.status, name='status'),
    url(r'^update/$', views.update, name='update'),
    url(r'^logs/$', views.logs, name='logs'),
]
