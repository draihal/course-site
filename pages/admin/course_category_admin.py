from django.contrib import admin
from django.utils.safestring import mark_safe

from ..models import CourseCategory


@admin.register(CourseCategory)
class CourseCategoryAdmin(admin.ModelAdmin):
    def get_image_preview(self):
        if self.pk:
            return mark_safe(
                f"""<a href="{self.image.url}" target="_blank">
                <img src="{self.image.url}" alt="main_image" style="max-width: 200px; max-height: 200px;" />
                </a>"""
            )
        return "-"

    get_image_preview.short_description = "Превью 200px"

    list_display = ['name', 'updated_at', ]
    list_per_page = 30
    search_fields = ['name', ]
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('updated_at', get_image_preview)
    fieldsets = (
        ('Основная информация', {
            'fields': (
                ('name', 'slug'),
                'image',  get_image_preview,
                ('updated_at', ),
            )
        }),
    )
