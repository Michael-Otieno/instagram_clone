from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post,Profile

# Create your tests here.
class ProfileTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.profile = Profile(id=1,profile_pic='path/to/photo',user = self.user,biography='test bio')

    #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

     #Testing save method
    def test_save_profile(self):
        self.profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

        #Testing updtae method
    def test_update_profile(self):
        self.profile.save_profile()
        self.profile = Profile.objects.get(pk = 1)
        self.profile.update_bio('updated bio')
        self.updated_profile = Profile.objects.get(pk = 1)
        self.assertEqual(self.updated_profile.biography,"updated bio")

