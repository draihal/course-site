import pytest

from django.test import TestCase

from .. import factories


@pytest.mark.django_db
class ContactsPageTest(TestCase):
    def setUp(self):
        self.contacts_page = factories.ContactsPageFactory()

    def test__str__(self):
        assert self.contacts_page.__str__() == 'Страница контактов'
