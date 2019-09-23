from django.contrib import admin

from ..models import Grade


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ['lesson', 'teacher', 'student', 'status', ]
    list_per_page = 30
    search_fields = ['lesson', 'teacher', 'student', ]
    readonly_fields = ('updated_at', 'created_at')
    fieldsets = (
        ('Основная информация', {
            'fields': (
                'lesson', 'teacher', 'student',
                'status', 'grade',
                ('created_at', 'updated_at', ),
            )
        }),
    )
