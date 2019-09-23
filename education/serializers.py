from rest_framework import serializers

from education.models import Group, Grade, Lesson, Module, Payment


class GradeSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Grade
        exclude = ['updated_at', 'created_at', ]

    def get_url(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)


class GroupShortSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Group
        fields = ['id', 'url', 'name', 'category', ]

    def get_url(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)


class GroupSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Group
        lookup_field = 'slug'
        exclude = ['updated_at', 'created_at', ]

    def get_url(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)


class LessonSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Lesson
        lookup_field = 'slug'
        exclude = ['updated_at', 'created_at', ]

    def get_url(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)


class ModuleSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Module
        exclude = ['updated_at', 'created_at', ]

    def get_url(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)


class PaymentSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Payment
        exclude = ['updated_at', 'created_at', ]

    def get_url(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)

