from django.conf.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('',views.album,name='album'),
    path('search/', views.search, name='search'),
    path('image/',views.image,name ='image'),
    path('location/(?P<location>\w+)/', views.location_image, name='location'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)