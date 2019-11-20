from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^register_user$', views.add_user),
    url(r'^login_user$', views.login),
    url(r'^logout$', views.logout)
]