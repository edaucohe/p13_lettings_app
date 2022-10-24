from django.test import Client, TestCase
from django.urls import reverse

from lettings.models import Address, Letting


class TestTemplates(TestCase):
    def test_display_index_title(self):
        client = Client()
        response = client.get(reverse('lettings_index'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "lettings/index.html")
        self.assertContains(response, "<title>Lettings</title>")

    def test_display_letting_titles(self):
        client = Client()
        address = Address.objects.create(
            number=7217,
            street="Bedford Street",
            city="Brunswick",
            state='GA',
            zip_code="31525",
            country_iso_code="USA"
        )
        letting = Letting.objects.create(
            title="Joshua Tree Green Haus /w Hot Tub",
            address=address
        )
        response = client.get(reverse('letting', kwargs={'letting_id': letting.id}))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "lettings/letting.html")
        self.assertContains(response, "<title>Joshua Tree Green Haus /w Hot Tub</title>")
