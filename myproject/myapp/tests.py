from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from .models import Item

class TaskAPITestCase(APITestCase):

    def setUp(self):

        # Testing data
        self.client = APIClient()
        self.task_data = {'name': 'Test Task', 'description': 'Test Description'}

    # --------Creation Test------------
    def test_api_can_create_a_task(self):
        response = self.client.post(
            reverse('task-create'),
            self.task_data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'Test Task')

    # ---------Getting Test------------
    def test_api_can_get_a_task(self):
        response = self.client.post(
            reverse('task-create'),
            self.task_data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.client.get(
           reverse('task-detail', kwargs={'pk': response.data['id']}),
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test Task')

    # ----------Updating Test------------
    def test_api_can_update_a_task(self):
        response = self.client.post(
            reverse('task-create'),
            self.task_data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        change_task = {'name': 'Changed Title'}
        response = self.client.get(
           reverse('task-detail', kwargs={'pk': response.data['id']}), change_task,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test Task')

    #----------Deleting Task----------------
    def test_api_can_delete_a_task(self):
        response = self.client.post(
            reverse('task-create'),
            self.task_data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.delete(
           reverse('task-detail', kwargs={'pk': response.data['id']}),
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
    