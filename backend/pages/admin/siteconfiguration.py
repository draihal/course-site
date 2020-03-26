from django.contrib import admin
from django.utils.safestring import mark_safe

from solo.admin import SingletonModelAdmin

from ..models import SiteConfiguration


@admin.register(SiteConfiguration)
class SiteConfigurationAdmin(SingletonModelAdmin):
    def get_logo_preview(self):
        if self.pk:
            return mark_safe(
                f"""<a href="{self.logo.url}" target="_blank">
                <img src="{self.logo.url}" alt="main_image" style="max-width: 200px; max-height: 200px;" />
                </a>"""
            )
        return "-"

    get_logo_preview.short_description = "Превью 200px"

    readonly_fields = ('updated_at', get_logo_preview)
    fieldsets = (
        ('Основная информация', {
            'fields': (
                ('title',),
                'short_description',
                'logo',  get_logo_preview,
                ('updated_at', ),
            )
        }),
    )
