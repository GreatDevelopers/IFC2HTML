from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.IndexView, name='index'),
    url(r'^show/$', views.getfile, name='show'),

    #url(r'^getfile/$', views.getfile, name='getfile'),
    #url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

]
