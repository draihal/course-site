from rest_framework import serializers
from rest_framework.reverse import reverse

from pages import models


class AboutUsPageSerializer(serializers.ModelSerializer):
    main_image = serializers.ImageField(use_url=True)

    class Meta:
        model = models.AboutUsPage
        exclude = ['updated_at', ]


class ContactsPageSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ContactsPage
        exclude = ['updated_at', ]


class SiteConfigurationSerializer(serializers.ModelSerializer):
    logo = serializers.ImageField(use_url=True)
    page_about_us = serializers.SerializerMethodField(read_only=True)
    page_contacts = serializers.SerializerMethodField(read_only=True)
    page_categories = serializers.SerializerMethodField(read_only=True)
    page_courses = serializers.SerializerMethodField(read_only=True)
    page_events = serializers.SerializerMethodField(read_only=True)
    page_publications = serializers.SerializerMethodField(read_only=True)
    page_reviews = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = models.SiteConfiguration
        # exclude = ['updated_at', ]
        fields = [
            'title', 'logo', 'short_description',
            'page_about_us', 'page_contacts', 'page_categories',
            'page_courses', 'page_events', 'page_publications',
            'page_reviews'
        ]

    def get_page_about_us(self, obj):
        return reverse('pages:about-us-list',)

    def get_page_contacts(self, obj):
        return reverse('pages:contacts-list',)

    def get_page_categories(self, obj):
        return reverse('pages:categories-list',)

    def get_page_courses(self, obj):
        return reverse('pages:courses-list',)

    def get_page_events(self, obj):
        return reverse('pages:events-list',)

    def get_page_publications(self, obj):
        return reverse('pages:publications-list',)

    def get_page_reviews(self, obj):
        return reverse('pages:reviews-list',)


class CourseShortSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = models.Course
        fields = ['id', 'name', 'url']

    def get_url(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)


class CourseSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)
    image = serializers.ImageField(use_url=True)
    certificate_sample = serializers.ImageField(use_url=True)

    class Meta:
        model = models.Course
        exclude = ['updated_at', ]
        lookup_field = 'slug'

    def get_url(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)


class CourseCategorySerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)
    image = serializers.ImageField(use_url=True)
    courses = CourseShortSerializer(many=True, read_only=True, source='course_set')

    class Meta:
        model = models.Course
        fields = ['id', 'name', 'slug', 'image', 'url', 'courses', ]
        lookup_field = 'slug'

    def get_url(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)


class EventSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)
    course = CourseShortSerializer(read_only=True,)
    user_id = serializers.IntegerField(source='speaker.user.pk', read_only=True)
    speaker_first_name = serializers.CharField(source='speaker.user.first_name', read_only=True)
    speaker_last_name = serializers.CharField(source='speaker.user.last_name', read_only=True)
    speaker_bio = serializers.CharField(source='speaker.bio', read_only=True)

    class Meta:
        model = models.Event
        exclude = ['updated_at', 'created_at', ]
        lookup_field = 'slug'

    def get_url(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)


class MassMediaPublicationSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)
    main_image = serializers.ImageField(use_url=True)

    class Meta:
        model = models.MassMediaPublication
        exclude = ['updated_at', 'created_at']
        lookup_field = 'slug'

    def get_url(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)


class ReviewSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)
    course_info = CourseShortSerializer(read_only=True, source='course')
    user_id = serializers.IntegerField(source='student.user.pk', read_only=True)
    student_first_name = serializers.CharField(source='student.user.first_name', read_only=True)
    student_last_name = serializers.CharField(source='student.user.last_name', read_only=True)

    class Meta:
        model = models.Review
        exclude = ['updated_at', 'created_at', ]

    def get_url(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)
