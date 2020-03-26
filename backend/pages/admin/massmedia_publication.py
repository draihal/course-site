from django.contrib import admin
from django.utils.safestring import mark_safe

from ..models import MassMediaPublication


@admin.register(MassMediaPublication)
class MassMediaPublicationAdmin(admin.ModelAdmin):
    def get_main_image_preview(self):
        if self.pk:
            return mark_safe(
                f"""<a href="{self.main_image.url}" target="_blank">
                <img src="{self.main_image.url}" alt="main_image" style="max-width: 200px; max-height: 200px;" />
                </a>"""
            )
        return "-"

    get_main_image_preview.short_description = "Превью 200px"

    list_display = ['name', 'mass_media_name', 'date_of_publish', ]
    list_filter = ['date_of_publish', ]
    list_per_page = 30
    search_fields = ['name', 'mass_media_name', ]
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('updated_at', 'created_at', get_main_image_preview)
    fieldsets = (
        ('Основная информация', {
            'fields': (
                ('name', 'slug'), 'mass_media_name',
                'publication_url', 'date_of_publish',
                'main_image', get_main_image_preview,
                ('created_at', 'updated_at', ),
            )
        }),
    )
