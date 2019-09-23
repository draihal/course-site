from django.contrib import admin

from ..models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['course', 'student', 'created_at', 'updated_at', ]
    list_filter = ['course', ]
    list_per_page = 30
    search_fields = ['course', ]
    readonly_fields = ('updated_at', 'created_at')
    fieldsets = (
        ('Основная информация', {
            'fields': (
                'student', 'course', 'text',
                ('created_at', 'updated_at', ),
            )
        }),
    )
