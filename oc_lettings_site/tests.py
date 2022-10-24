from django.test import Client, TestCase
from django.urls import reverse


class TestTemplates(TestCase):
    def test_display_index_title(self):
        client = Client()
        response = client.get(reverse('index'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertContains(response, "<title>Holiday Homes</title>")

    def test_dummy(self):
        assert 1
