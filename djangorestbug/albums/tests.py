from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase


class CreatePatientTestCase(APITestCase):

    def test_create_album(self):
        post_data = {'title': 'The Wall', 'artist': 'Pink Floyd'}
        response = self.client.post(reverse('album-list'), post_data)
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['title'] == 'The Wall'
        assert response.data['artist'] == 'Pink Floyd'
        assert 'id' in response.data
