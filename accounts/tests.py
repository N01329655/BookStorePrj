from django.test import TestCase

# my imports
from django.contrib.auth import get_user_model



class CustomUserTest(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='will',
            email='email',
            password='testcase'
        )
        self.assertEqual(user.username, 'will')
        self.assertEqual(user.email, 'email')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_superuser(
            username='user',
            email='email',
            password='testpassword'
        )
        self.assertEqual(user.username, 'user')
        self.assertEqual(user.email, 'email')
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)