# pictures-api/pictures/api/tests/test_views.py

from django.shortcuts import reverse

from rest_framework.test import APITestCase

from api.models import Picture


class TestNoteApi(APITestCase):
    def setUp(self):
        # create picture
        self.picture = picture(name="The Space Between Us", year_of_release=2017)
        self.picture.save()

    def test_picture_creation(self):
        response = self.client.post(reverse('pictures'), {
            'name': 'Bee picture',
            'year_of_release': 2007
        })

        # assert new picture was added
        self.assertEqual(picture.objects.count(), 2)

        # assert a created status code was returned
        self.assertEqual(201, response.status_code)

    def test_getting_pictures(self):
        response = self.client.get(reverse('pictures'), format="json")
        self.assertEqual(len(response.data), 1)

    def test_updating_picture(self):
        response = self.client.put(reverse('detail', kwargs={'pk': 1}), {
            'name': 'The Space Between Us updated',
            'year_of_release': 2017
        }, format="json")

        # check info returned has the update
        self.assertEqual('The Space Between Us updated', response.data['name'])

    def test_deleting_picture(self):
        response = self.client.delete(reverse('detail', kwargs={'pk': 1}))

        self.assertEqual(204, response.status_code)