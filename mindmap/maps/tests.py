from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from maps.models import Map

class MapsTests(APITestCase):
    def test_maps_list(self):
        """
        Ensure we can get list of map
        """
        url = reverse('map-list')
        #data = {'name': 'DabApps'}
        response = self.client.get(url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        #self.assertEqual(Account.objects.count(), 1)
        #self.assertEqual(Account.objects.get().name, 'DabApps')
