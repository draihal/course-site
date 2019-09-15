from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from django.utils.translation import ugettext_lazy as _

from .models import CustomUser


class UserAdmin(UserAdmin):

    list_display = (
        'username', 'email',
        'last_login', 'date_joined',
        'is_staff')
    list_filter = ('is_staff', )

    fieldsets = (
        (_('Info'), {'fields': (
            'username', 'email',
            'password',)}),

        (_('Permissions'), {'fields': (
            'is_active', 'is_staff', 'is_superuser')}),
        (_('Important dates'), {'fields': (
            'last_login', 'date_joined', )}),
        (_('Groups'), {'fields': ('groups',)}),
        #('Perm', {'fields': ('user_permissions',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1',
                       'password2')}
         ),
    )
    search_fields = ('email', 'username')
    ordering = ('username',)
    readonly_fields = ('last_login', 'date_joined', )

    filter_horizontal = ()


admin.site.register(CustomUser, UserAdmin)
