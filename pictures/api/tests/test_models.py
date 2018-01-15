from django.test import TestCase

from api.models import Picture


class TestPictureModel(TestCase):
    def setUp(self):
        self.picture = picture(like_count= 23, tags='cute')
        self.picture.save()

    def test_picture_creation(self):
        self.assertEqual(picture.objects.count(), 1)

    def test_picture_representation(self):
        self.assertEqual(self.picture.like_count, str(self.id))