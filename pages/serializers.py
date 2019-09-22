from rest_framework import serializers

from pages.models import Course


class CourseShortSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Course
        # fields = '__all__'
        fields = ['id', 'name', 'url']

    def get_url(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)
