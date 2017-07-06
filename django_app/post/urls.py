from django.conf.urls import url

from .views import post_view

app_name = 'post'
urlpatterns = [
    url(r'^$', post_view.post_list, name='post_list'),
    url(r'^create/$', post_view.post_create, name='post_create'),
    url(r'^order/(?P<post_pk>\d+)/$', post_view.order, name='order'),
]
