from django.contrib import admin

from solo.admin import SingletonModelAdmin

from ..models import IndexPage


@admin.register(IndexPage)
class IndexPageAdmin(SingletonModelAdmin):

    readonly_fields = ('updated_at', )
    fieldsets = (
        ('Основная информация', {
            'fields': (
                'title', 'short_description', 'description',
                ('updated_at', ),
            )
        }),
    )
