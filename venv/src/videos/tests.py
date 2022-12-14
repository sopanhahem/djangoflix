from django.test import TestCase

from .models import Video

class VideoModelTestCase(TestCase):
    def setUp(self):
        Video.objects.create(title='This is my title')

    def test_valid_title(self):
        title='This is my title'
        qs = Video.objects.filter(title=title)
        self.assertEqual(qs.count(), 1)


# Create your tests here.
