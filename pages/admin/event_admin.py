from django.contrib import admin

from ..models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'speaker', 'course', 'type_of_event', 'datetime', ]
    list_filter = ['course', 'type_of_event', 'datetime', ]
    list_per_page = 30
    search_fields = ['name', 'speaker', 'course', 'type_of_event', ]
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('updated_at', 'created_at')
    fieldsets = (
        ('Основная информация', {
            'fields': (
                ('name', 'slug'), 'speaker',
                'course', 'type_of_event', 'datetime',
                'url',
                ('created_at', 'updated_at', ),
            )
        }),
    )
