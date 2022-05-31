from django.urls import path,re_path as url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('',views.album,name='album'),
    path('search/', views.search, name='search'),
    path('image/',views.image,name ='image'),
    url('^location/(?P<location>\w+)/$', views.location, name='location'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)