from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse

from profiles.models import Profile


class TestTemplates(TestCase):
    def test_display_index_title(self):
        client = Client()
        response = client.get(reverse('profiles_index'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profiles/index.html")
        self.assertContains(response, "<title>Profiles</title>")

    def test_display_profile_titles(self):
        client = Client()
        user = User.objects.create(
            username="HeadlinesGazer",
            first_name="Jamie",
            last_name="Lal",
            email="jssssss33@acee9.live"
        )
        profile = Profile.objects.create(
            user=user,
            favorite_city="Buenos Aires"
        )
        response = client.get(reverse('profile', kwargs={'username': profile.user.username}))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profiles/profile.html")
        self.assertContains(response, "<title>HeadlinesGazer</title>")
