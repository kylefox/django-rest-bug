Demonstrates a bug where merely accessing `serializer.data` causes its internal value to change.

In short, when POSTing to create we expect the full serialized version of the object to be returned in `response.data`. However, if `serialize.data` is used inside the viewset's `perform_create()` method, it causes `response.data` to be whatever the initial POST data was.

Even if `serializer.data` is not "safe", I think it's wrong for the internal data to change simply by accessing a property. Typically you don't expect property access to have side effects.

## Setup

```
git clone git@github.com:kylefox/django-rest-bug.git
cd django-rest-bug
pip install -q -r requirements.txt
python manage.py test
```

## Relevant Code Snippets

```python
# models.py
class Album(models.Model):

    title = models.CharField(max_length=250)
    artist = models.CharField(max_length=250)


# serializers.py  
class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ('id', 'title', 'artist')


# views.py
class AlbumViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):

    serializer_class = AlbumSerializer
    queryset = Album.objects.all()

    def perform_create(self, serializer):

        # If `serializer.data` is present, it will screw up `response.data`
        # (Comment line below to watch tests pass)
        serializer.data

        serializer.save()


# tests.py
class CreateAlbumTestCase(APITestCase):

    def test_create_album(self):
        post_data = {'title': 'The Wall', 'artist': 'Pink Floyd'}
        response = self.client.post(reverse('album-list'), post_data)

        # THIS ASSERTION FAILS WHEN `serializer.data` IS CALLED IN `perform_create()`
        assert 'id' in response.data, "Key `id` isn't in `response.data`"

```
