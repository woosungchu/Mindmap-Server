from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from maps.models import Map, Node
from django.contrib.auth.models import User

"""
#status code
http://www.django-rest-framework.org/api-guide/status-codes/

#url namespaces
http://www.django-rest-framework.org/api-guide/routers/#defaultrouter
"""

class BaseTestCase(APITestCase):
    def setUp(self):

        #author
        self.username = "mapper"
        self.password = "secret_password"
        self.email = "mapper@testuser.com"
        self.author = User.objects.create_user(self.username,self.email,self.password)

        #map
        self.title = "Titled Title!"
        self.data = {
            'title': self.title
        }
        self.map = Map.objects.create(author=self.author, title=self.title)

        #node
        self.type = 'N'
        self.content = 'test content'
        self.nodedata = {
            'map' : self.map.id,
            'type' : self.type,
            'content' : self.content
        }
        self.node = Node.objects.create(map=self.map, type=self.type, content=self.content)

        #token
        self.api_authentication()

    def api_authentication(self):
        url = reverse('login')
        response = self.client.post(url, {'username': self.username,'password': self.password}, format='json')
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + response.data['token'])

    def get_hacker_token(self):
        hacker_name = "hacker"
        hacker_email = "hacker@hacker.com"
        hacker_pw = "hacker123"
        hacker = User.objects.create_user(hacker_name, hacker_email,hacker_pw)

        url = reverse('login')
        response = self.client.post(url, {'username': hacker_name,'password': hacker_pw}, format='json')

        return response.data['token']

class MapsTests(BaseTestCase):

    def test_maps_list(self):
        """
        Ensure we can get list of map
        """
        url = reverse('api:map-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_maps_create(self):
        """
        Ensure we can create map
        """
        url = reverse('api:map-list')
        response = self.client.post(url, self.data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_maps_detail(self):
        """
        Ensure we can get detail of map
        """
        url = reverse('api:map-detail',kwargs={'pk':self.map.id})
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.map.title)

    def test_node_update(self):
        """
        update map
        """
        updated_title = 'updated_title'
        url = reverse('api:map-detail',kwargs={'pk':self.map.id})
        self.data['title'] = updated_title
        response = self.client.put(url, self.data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], updated_title)

    def test_map_get_permission(self):
        """
        unauthorized user also can read map
        """
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + self.get_hacker_token())

        url = reverse('api:map-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_map_put_permission(self):
        """
        user who is not owner cannot update map
        """
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + self.get_hacker_token())

        updated_title = 'updated_title'
        url = reverse('api:map-detail',kwargs={'pk':self.map.id})
        self.data['title'] = updated_title
        response = self.client.put(url, self.data, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_filter_map(self):
        """
        filter maps with author
        """
        url = reverse('api:map-list')
        response = self.client.get(url, {'author':self.author.id}, format='json')
        self.assertEqual(response.data[0]['author']['id'], self.author.id)

#NODES
class NodesTests(BaseTestCase):
    """
    - add new node to certain map
    - remove the node from map
    """

    def test_node_create(self):
        """
        get all nodes of specific map
        """
        url = reverse('api:node-list')
        response = self.client.post(url, self.nodedata, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_node_remove(self):
        """
        remove node from specific node
        """
        url = reverse('api:node-detail',kwargs={'pk':self.node.id})
        response = self.client.delete(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_node_update(self):
        """
        update node
        """
        updated_content = 'updated_content'
        url = reverse('api:node-detail',kwargs={'pk':self.node.id})
        self.nodedata['content'] = updated_content
        response = self.client.put(url, self.nodedata, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['content'], updated_content)

    def test_node_put_permission(self):
        """
        block trying to access node from hacker who is not owner
        """
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + self.get_hacker_token())

        url = reverse('api:node-detail',kwargs={'pk':self.node.id})
        response = self.client.delete(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
