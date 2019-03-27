
from django.conf.urls import url,include

from .import views

urlpatterns = [

    url(r'^$',views.welcome, name='instagram'),
    url(r'^(?P<user_id>[0-9]+)/$',views.details,name='details'),
    url(r'^all/$',views.allimages,name='allimages')
]
