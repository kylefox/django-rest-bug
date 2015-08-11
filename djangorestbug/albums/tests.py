from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase


class CreateAlbumTestCase(APITestCase):

    def test_create_album(self):
        post_data = {'title': 'The Wall', 'artist': 'Pink Floyd'}
        response = self.client.post(reverse('album-list'), post_data)

        # Make sure the create worked.
        assert response.status_code == status.HTTP_201_CREATED

        # We expect these attributes to be present in the response.
        assert response.data['title'] == 'The Wall'
        assert response.data['artist'] == 'Pink Floyd'

        # We expect the id to be present in the response data.
        # HOWEVER, when `serializer.data` is called inside the view's
        # perform_create() method, internally `serializer.data` is reset
        # to the intial data (ex: response.data.keys() == ['title', 'artist'])
        assert 'id' in response.data, "Key `id` isn't in `response.data`"
