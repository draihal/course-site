from django.contrib import admin

from ..models import Module


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ['name', 'group', ]
    list_per_page = 30
    search_fields = ['name', 'group', ]
    readonly_fields = ('updated_at', 'created_at')
    fieldsets = (
        ('Основная информация', {
            'fields': (
                ('name', 'group',),
                ('created_at', 'updated_at', ),
            )
        }),
    )
