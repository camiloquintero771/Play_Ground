from django.test import TestCase
from .models import Profile
from django.contrib.auth.models import User


class ProfileTestCase(TestCase):
    def setUp(self):
        User.objects.create_user('xilena', 'maraxilena@gmail.com',
                                 'ianymara2020')

    def test_profile_exists(self):
        validate = Profile.objects.get(user__username='xilena')
        self.assertIsInstance(validate, Profile)
