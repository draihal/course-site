from rest_framework import serializers
from rest_framework.reverse import reverse

from pages import models
from users.models import Student, Teacher, Partner
from education.models import Group


class AboutUsPageSerializer(serializers.ModelSerializer):
    # main_image = serializers.ImageField(use_url=True)

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
    student_image = serializers.ImageField(use_url=True, source='student.avatar', read_only=True, )

    class Meta:
        model = models.Review
        exclude = ['updated_at', 'created_at', 'student', 'course']

    def get_url(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)


class TeachersForIndexPageSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)
    teacher_id = serializers.IntegerField(source='user.pk', read_only=True)
    avatar = serializers.ImageField(use_url=True)
    teacher_first_name = serializers.CharField(source='user.first_name', read_only=True)
    teacher_last_name = serializers.CharField(source='user.last_name', read_only=True)

    class Meta:
        model = Teacher
        fields = [
            'teacher_id', 'url', 'avatar',
            'teacher_first_name', 'teacher_last_name',
            'company', 'position', 'bio',
        ]

    def get_url(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)


class PartnersForIndexPageSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)
    id = serializers.IntegerField(source='user.pk', read_only=True)
    logo = serializers.ImageField(use_url=True)

    class Meta:
        model = Partner
        fields = ['id', 'url', 'logo', 'company', 'info', ]

    def get_url(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)


class IndexPageSerializer(serializers.ModelSerializer):
    number_of_students = serializers.SerializerMethodField(read_only=True)
    number_of_groups = serializers.SerializerMethodField(read_only=True)
    number_of_teachers = serializers.SerializerMethodField(read_only=True)
    random_three_teachers = serializers.SerializerMethodField(read_only=True)
    random_ten_partners = serializers.SerializerMethodField(read_only=True)
    random_two_reviews = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = models.IndexPage
        fields = ['title', 'short_description', 'description',
                  'number_of_students', 'number_of_groups', 'number_of_teachers',
                  'random_three_teachers', 'random_ten_partners', 'random_two_reviews',
                  ]

    def get_number_of_students(self, obj):
        return Student.get_number_of_students()

    def get_number_of_groups(self, obj):
        return Group.get_number_of_groups()

    def get_number_of_teachers(self, obj):
        return Teacher.get_number_of_teachers()

    def get_random_three_teachers(self, obj):
        random_three_teachers = Teacher.get_random_teachers(number_of_teachers=3)
        return TeachersForIndexPageSerializer(random_three_teachers, many=True).data

    def get_random_ten_partners(self, obj):
        random_ten_partners = Partner.get_random_partners(number_of_partners=10)
        return PartnersForIndexPageSerializer(random_ten_partners, many=True).data

    def get_random_two_reviews(self, obj):
        random_two_reviews = models.Review.get_random_reviews(number_of_reviews=2)
        return ReviewSerializer(random_two_reviews, many=True).data
