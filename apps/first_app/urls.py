from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^reset$', views.reset),
    url(r'^add_user$', views.add_user),
    url(r'^add_message$', views.add_message),
    url(r'^one_user/(?P<user_id>\d+)$', views.one_user),
    url(r'^delete/(?P<mess_id>\d+)$', views.destroy),
]