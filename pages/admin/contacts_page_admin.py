from django.contrib import admin

from solo.admin import SingletonModelAdmin

from ..models import ContactsPage


@admin.register(ContactsPage)
class ContactsPageAdmin(SingletonModelAdmin):
    readonly_fields = ('updated_at', )
