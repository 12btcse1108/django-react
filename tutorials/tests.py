from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Tutorial
# Create your tests here.

class TutorialTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
        username = 'nitin',
        email = 'nitinverma1394@gmail.com',
        password = 'flipkart@123'
        )

        self.tutorial = Tutorial.objects.create(
            title = 'Python',
            body = 'top used language in the world',
            author = self.user,
        )
