from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^home/$', views.index, name='index'),
    url(r'^status/$', views.getstatus, name='getstatus'),
    url(r'^update-lines/$', views.update_lines, name='update_lines'),
    url(r'^logs/$', views.logs, name='logs'),
]
