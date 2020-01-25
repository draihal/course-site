from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe

from .models import CustomUser, Partner, Student, Teacher


@admin.register(CustomUser)
class UserAdmin(UserAdmin):

    list_display = ('first_name', 'email', 'phone_number', 'updated_at',
                    'created_at', 'is_student', 'is_teacher', 'is_partner',
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
            'fields': ('updated_at', 'created_at')
        }),
        ('Группы и разрешения', {
            'fields': ('groups', 'user_permissions')
        }),
    )
    add_fieldsets = ((None, {
        'classes': ('wide', ),
        'fields': ('first_name', 'last_name', 'email', 'phone_number',
                   'password1', 'password2', 'is_student', 'is_teacher', 'is_partner')
    }), )
    search_fields = ('email', 'first_name', 'phone_number')
    ordering = ('is_staff', )
    readonly_fields = ('updated_at', 'created_at')
    list_per_page = 30
    filter_horizontal = ()


def get_image_preview(obj):
    if obj.pk:
        return mark_safe(
            f"""<a href="{obj.avatar.url}" target="_blank">
            <img src="{obj.avatar.url}" alt="avatar" style="max-width: 200px; max-height: 200px;" />
            </a>"""
        )
    return "-"


get_image_preview.short_description = "Превью 200px"


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        qs = super(StudentAdmin, self).get_queryset(request)
        qs = qs.select_related('user')
        return qs

    list_display = ['user', 'username', 'updated_at', ]
    list_per_page = 30
    readonly_fields = ('updated_at', 'created_at', get_image_preview)
    fieldsets = (
        ('Основная информация', {
            'fields': (
                'user', ('first_name_lat', 'last_name_lat',),
                'username', 'birth_date', 'sex',
                ('country', 'city'),
                ('can_relocate', 'can_full_time', 'can_part_time', 'can_remote',),
                ('company', 'position',),
                'avatar',  get_image_preview,
                ('created_at', 'updated_at'),
            )
        }),
    )


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        qs = super(TeacherAdmin, self).get_queryset(request)
        qs = qs.select_related('user')
        return qs

    list_display = ['user', 'username', 'updated_at', ]
    list_per_page = 30
    readonly_fields = ('updated_at', 'created_at', get_image_preview)
    fieldsets = (
        ('Основная информация', {
            'fields': (
                'user', ('first_name_lat', 'last_name_lat',),
                'username', 'birth_date', 'sex', 'bio',
                ('country', 'city'),
                ('company', 'position',),
                'avatar',  get_image_preview,
                ('created_at', 'updated_at'),
            )
        }),
    )


def get_logo_preview(obj):
    if obj.pk:
        return mark_safe(
            f"""<a href="{obj.logo.url}" target="_blank">
            <img src="{obj.logo.url}" alt="{obj.company}" style="max-width: 200px; max-height: 200px;" />
            </a>"""
        )
    return "-"


get_logo_preview.short_description = "Превью 200px"


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        qs = super(PartnerAdmin, self).get_queryset(request)
        qs = qs.select_related('user')
        if request.resolver_match.func.__name__ == 'change_view':
            qs = qs.prefetch_related('courses')
        return qs

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
