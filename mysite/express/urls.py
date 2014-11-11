from django.conf.urls import patterns, url

from express import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<diner_id>\d+)$', views.order, name='order'),
    # url(r'^(?P<file_name>[a-zA-Z._\-/\d]+).js$', views.js_file, name='js_file'),
    # url(r'^(?P<file_name>[a-zA-Z._\-/\d]+).css$', views.css_file, name='css_file'),
)
