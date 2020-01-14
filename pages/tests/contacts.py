from django.test import TestCase

from ..models.contacts import ContactsPage


class ContactsPageTest(TestCase):

    # first() because ContactsPage django singleton
    def test__str__(self):
        self.assertEqual(ContactsPage.objects.first().__str__(), 'Страница контактов')
