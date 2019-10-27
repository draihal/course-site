from django.contrib import admin

from ..models import Group


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'date_start', 'date_end', ]
    list_per_page = 30
    list_filter = ['category', ]
    search_fields = ['name', 'category', ]
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('updated_at', 'created_at')
    fieldsets = (
        ('Основная информация', {
            'fields': (
                ('name', 'slug',), 'category',
                'price', ('date_start', 'date_end'),
                'teachers', 'students',
                ('created_at', 'updated_at', ),
            )
        }),
    )
