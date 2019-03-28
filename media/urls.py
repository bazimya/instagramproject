
from django.conf.urls import url,include
from django.conf import settings
from django.conf.urls.static import static
from .import views

urlpatterns = [

    url(r'^$',views.welcome, name='instagram'),
    url(r'^profile',views.profile, name='profiles'),
    # url(r'^(?P<user_id>[0-9]+)/$',views.details,name='details'),
    url(r'^all/$',views.allimages,name='allimages'),
    url(r'^update/(\d+)/$',views.update_profile,name='update'),
    # url(r'^new/article$', views.new_article, name='new-article')
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
