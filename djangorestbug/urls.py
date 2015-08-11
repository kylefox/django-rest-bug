from django.conf.urls import include, url

from rest_framework import routers

from djangorestbug.albums.views import AlbumViewSet


router = routers.DefaultRouter()

router.register(prefix=r'albums', viewset=AlbumViewSet, base_name='album')

urlpatterns = [
    url(r'^api/', include(router.urls)),
]
