from django.conf.urls import path
from .templates import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('',views.album,name='album'),
    path('search/', views.search, name='search'),
    path('image/',views.image,name ='image'),
    path('location/(<location>\)/', views.location_image, name='location'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)