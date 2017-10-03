from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^status/$', views.getstatus, name='getstatus'),
    url(r'^update/$', views.update, name='update'),
    url(r'^logs/$', views.logs, name='logs'),
]
