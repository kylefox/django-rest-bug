from rest_framework import viewsets, mixins

from .models import Album
from .serializers import AlbumSerializer


class AlbumViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):

    serializer_class = AlbumSerializer
    queryset = Album.objects.all()

    def perform_create(self, serializer):

        # If `serializer.data` is present, it will screw up `response.data`
        # (Comment line below to watch tests pass)
        serializer.data

        serializer.save()
