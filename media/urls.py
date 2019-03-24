
from django.conf.urls import url,include

from .import views

urlpatterns = [

    url(r'^',views.welcome, name='index'),
    url(r'^(?P<user_id>[0-9]+)/$',views.details,name='user_detail')
]
