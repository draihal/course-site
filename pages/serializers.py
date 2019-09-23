from rest_framework import serializers

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

    class Meta:
        model = models.SiteConfiguration
        exclude = ['updated_at', ]


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
