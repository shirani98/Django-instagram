from django.test import TestCase
from . models import Post
from accounts.models import MyUser
from django.urls import reverse
# Create your tests here.


class MyTest(TestCase):
    def setUp(self):
        self.user = MyUser.objects.create_user(
            username="test", email="test@test.com", password="testpassword")
        self.post = Post.objects.create(user=self.user, body="test body section",
                                        image="media/115-1150152_default-profile-picture-avatar-png-green.jpg")

    def test_create_post(self):
        response = self.client.post(reverse('accounts:addpost'), {
            "body": "test body section",
            "image": "media/115-1150152_default-profile-picture-avatar-png-green.jpg",
            "user": self.user,
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().body, "test body section")
