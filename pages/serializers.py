from rest_framework import serializers

from pages import models


class AboutUsPageSerializer(serializers.ModelSerializer):
    main_image = serializers.ImageField(use_url=True)

    class Meta:
        model = models.AboutUsPage
        fields = ['title', 'slug', 'main_image', 'short_description', 'short_about_us']


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
