from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe

from .models import CustomUser, Partner, Student, Teacher


@admin.register(CustomUser)
class UserAdmin(UserAdmin):

    list_display = ('first_name', 'email', 'phone_number', 'last_login',
                    'date_joined', 'is_student', 'is_teacher', 'is_partner',
                    'is_staff')
    list_filter = ('is_student', 'is_teacher', 'is_partner', 'is_staff')

    fieldsets = (
        ('Персональная информация', {
            'fields': (('first_name', 'last_name'), ('email', 'phone_number'),
                       'password')
        }),
        ('Разрешения', {
            'fields': (('is_student', 'is_teacher', 'is_partner'),
                       ('is_active', 'is_staff', 'is_superuser'))
        }),
        ('Даты', {
            'fields': ('last_login', 'date_joined')
        }),
        ('Группы и разрешения', {
            'fields': ('groups', 'user_permissions')
        }),
    )
    add_fieldsets = ((None, {
        'classes': ('wide', ),
        'fields': ('first_name', 'email', 'phone_number', 'password1',
                   'password2')
    }), )
    search_fields = ('email', 'first_name', 'phone_number')
    ordering = ('is_staff', )
    readonly_fields = ('last_login', 'date_joined')
    list_per_page = 30
    filter_horizontal = ()


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    pass


def get_logo_preview(obj):
    if obj.pk:
        return mark_safe(
            f"""<a href="{obj.logo.url}" target="_blank">
            <img src="{obj.logo.url}" alt="{obj.company}" style="max-width: 200px; max-height: 200px;" />
            </a>"""
        )
    return "Выберете фотографию и сохраните прежде чем увидеть предварительный просмотр."


get_logo_preview.short_description = "Превью 200px"


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = [
        'user', 'company', 'updated_at',
    ]
    list_per_page = 30
    readonly_fields = ('updated_at', 'created_at', get_logo_preview)
    fieldsets = (
        ('Основная информация', {
            'fields': (
                'user', 'company', 'info', 'courses',
                'logo',  get_logo_preview,
                ('created_at', 'updated_at'),
            )
        }),
    )
    search_fields = ('company', )
    ordering = ('company', )
