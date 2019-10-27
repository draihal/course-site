from django.contrib import admin

from ..models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['datetime', 'module', 'student', ]
    list_per_page = 30
    search_fields = ['student', ]
    readonly_fields = ('updated_at', 'created_at')
    fieldsets = (
        ('Основная информация', {
            'fields': (
                ('datetime', 'invoice',),
                'module', 'student',
                ('created_at', 'updated_at', ),
            )
        }),
    )

