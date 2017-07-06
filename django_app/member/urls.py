from django.conf.urls import url

from member import views

app_name = 'member'
urlpatterns = [
    url(r'^create/$', views.create_user, name='create_user'),
    url(r'^login/$', views.login, name='login'),
]
