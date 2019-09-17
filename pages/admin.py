from django.contrib import admin

from .models import (
    AboutUsPage, ContactsPage, Course,
    CourseCategory, MassMediaPublication, SiteConfiguration
)


@admin.register(AboutUsPage)
class AboutUsPageAdmin(admin.ModelAdmin):
    pass


@admin.register(ContactsPage)
class ContactsPageAdmin(admin.ModelAdmin):
    pass


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass


@admin.register(CourseCategory)
class CourseCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(MassMediaPublication)
class MassMediaPublicationAdmin(admin.ModelAdmin):
    pass


@admin.register(SiteConfiguration)
class SiteConfigurationAdmin(admin.ModelAdmin):
    pass
