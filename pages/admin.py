from django.contrib import admin
from django.utils.safestring import mark_safe

from solo.admin import SingletonModelAdmin

from .models import (
    AboutUsPage, ContactsPage, Course, Event, Review,
    CourseCategory, MassMediaPublication, SiteConfiguration
)


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
                ('title', 'slug'),
                'short_description', 'short_about_us',
                'main_image',  get_main_image_preview,
                ('updated_at', ),
            )
        }),
    )


@admin.register(ContactsPage)
class ContactsPageAdmin(SingletonModelAdmin):
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
    def get_image_preview(self):
        if self.pk:
            return mark_safe(
                f"""<a href="{self.image.url}" target="_blank">
                <img src="{self.image.url}" alt="main_image" style="max-width: 200px; max-height: 200px;" />
                </a>"""
            )
        return "-"

    get_image_preview.short_description = "Превью 200px"

    list_display = ['name', 'category', 'updated_at']
    list_filter = ['category', ]
    list_per_page = 30
    search_fields = ['name', 'category', ]
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('updated_at', get_image_preview)
    fieldsets = (
        ('Основная информация', {
            'fields': (
                ('name', 'slug'), 'category',
                'image',  get_image_preview,
                'description', 'necessary_knowledge', 'study_process',
                'graduation_project', 'after_training', 'certificate_sample',
                ('updated_at', ),
            )
        }),
    )


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


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'speaker', 'course', 'type_of_event', 'datetime', ]
    list_filter = ['course', 'type_of_event', 'datetime', ]
    list_per_page = 30
    search_fields = ['name', 'speaker', 'course', 'type_of_event', ]
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('updated_at', 'created_at')
    fieldsets = (
        ('Основная информация', {
            'fields': (
                ('name', 'slug'), 'speaker',
                'course', 'type_of_event', 'datetime',
                'url',
                ('created_at', 'updated_at', ),
            )
        }),
    )


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


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['course', 'student', 'created_at', 'updated_at', ]
    list_filter = ['course', ]
    list_per_page = 30
    search_fields = ['course', ]
    readonly_fields = ('updated_at', 'created_at')
    fieldsets = (
        ('Основная информация', {
            'fields': (
                'student', 'course', 'text',
                ('created_at', 'updated_at', ),
            )
        }),
    )
