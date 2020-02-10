from rest_framework import serializers

from education.models import Group, Grade, Lesson, Module, Payment, Homework


class GradeSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Grade
        exclude = ['updated_at', 'created_at', ]

    def get_url(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)


class HomeworkSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Homework
        exclude = ['updated_at', 'created_at', ]

    def get_url(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)


class GroupShortSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Group
        fields = ['id', 'url', 'name', 'slug', ]

    def get_url(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)


class LessonSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)
    homework = HomeworkSerializer(many=True, read_only=True, source='homework_set')
    grade = GradeSerializer(many=True, read_only=True, source='grade_set')

    class Meta:
        model = Lesson
        lookup_field = 'slug'
        exclude = ['updated_at', 'created_at', ]

    def get_url(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)


class ModuleSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)
    lessons = LessonSerializer(many=True, read_only=True, source='lesson_set')

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


class GroupSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)
    module = ModuleSerializer(many=True, read_only=True, source='module_set')

    class Meta:
        model = Group
        lookup_field = 'slug'
        # exclude = ['students', 'teachers', 'updated_at', 'created_at', ]
        fields = [
            'id', 'url', 'name', 'slug',
            'date_start', 'date_end', 'module',
        ]

    def get_url(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)
