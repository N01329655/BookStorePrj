

# my imports
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve
from django.test import TestCase
from .views import SignupPageView
from .forms import CustomUserCreationForm


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


class SignupPageTest(TestCase):

    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'registration/signup.html')
        self.assertContains(self.response, 'Sign up')
        self.assertNotContains(self.response, 'This text  should not be displayed ')

    def test_signup_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, CustomUserCreationForm)
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_singup_view(self):
        view = resolve('/accounts/signup/')
        self.assertEqual(view.func.__name__, SignupPageView.as_view().__name__)

