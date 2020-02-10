from django.contrib import admin

from ..models import Homework


@admin.register(Homework)
class HomeworkAdmin(admin.ModelAdmin):
    list_display = ['lesson', 'student', ]
    list_per_page = 30
    search_fields = ['lesson', 'student', ]
    readonly_fields = ('updated_at', 'created_at')
    fieldsets = (
        ('Основная информация', {
            'fields': (
                'lesson', 'student', 'student_homework',
                ('created_at', 'updated_at', ),
            )
        }),
    )
