from django.contrib import admin

from ..models import Lesson


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['name', 'group', 'number', 'datetime', ]
    list_per_page = 30
    list_filter = ['datetime', ]
    search_fields = ['name', 'group', ]
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('updated_at', 'created_at')
    fieldsets = (
        ('Основная информация', {
            'fields': (
                ('name', 'slug',), 'module',
                'group', 'number', 'description', 'poll_url',
                'datetime', 'url_translation',
                'homework_title', 'homework_description', 'homework_date',
                ('created_at', 'updated_at', ),
            )
        }),
    )
