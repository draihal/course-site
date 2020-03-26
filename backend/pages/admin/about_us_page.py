from django.contrib import admin
from django.utils.safestring import mark_safe

from solo.admin import SingletonModelAdmin

from ..models import AboutUsPage


@admin.register(AboutUsPage)
class AboutUsPageAdmin(SingletonModelAdmin):

    def get_main_image_preview(self):
        if self.pk:
            return mark_safe(
                f"""<a href="{self.main_image.url}" target="_blank">
                <img src="{self.main_image.url}" alt="main_image" style="max-width: 200px; max-height: 200px;" />
                </a>"""
            )
        return "-"

    get_main_image_preview.short_description = "Превью 200px"

    readonly_fields = ('updated_at', get_main_image_preview)
    fieldsets = (
        ('Основная информация', {
            'fields': (
                ('title',),
                'short_description', 'short_about_us',
                'main_image',  get_main_image_preview,
                ('updated_at', ),
            )
        }),
    )
