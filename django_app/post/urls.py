from django.conf.urls import url

from .views import post_view

app_name = 'post'
urlpatterns = [
    url(r'^$', post_view.post_list, name='post_list')
]
