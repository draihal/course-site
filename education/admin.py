from django.contrib import admin

from .models import Grade, Group, Lesson, Module, Payment


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

