from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^lookforjob/$', views.lookforjob_list, name='lookforjob_list'),
    url(r'^lookforjob/(?P<pk>[0-9]+)/$', views.lookforjob_detail, name='lookforjob_detail'),
    url(r'^lookforjob/new$', views.lookforjob_new, name='lookforjob_new'),
    url(r'^lookforjob/(?P<pk>[0-9]+)/edit/$', views.lookforjob_edit, name='lookforjob_edit'),
]