from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

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

    filter_horizontal = ()


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    pass


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    pass


# admin.site.register(CustomUser, UserAdmin)
