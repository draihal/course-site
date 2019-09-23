from django.contrib import admin
from django.utils.safestring import mark_safe

from solo.admin import SingletonModelAdmin

from .models import (
    AboutUsPage, ContactsPage, Course,
    CourseCategory, MassMediaPublication, SiteConfiguration
)


@admin.register(AboutUsPage)
class AboutUsPageAdmin(SingletonModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

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
                ('title', 'slug'),
                'short_description', 'short_about_us',
                'main_image',  get_main_image_preview,
                ('updated_at', ),
            )
        }),
    )


@admin.register(ContactsPage)
class ContactsPageAdmin(SingletonModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('updated_at', )


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


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass


@admin.register(CourseCategory)
class CourseCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(MassMediaPublication)
class MassMediaPublicationAdmin(admin.ModelAdmin):
    pass

