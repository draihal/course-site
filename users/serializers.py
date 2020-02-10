from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers

from users.models import CustomUser, Student, Teacher, Partner
from pages.serializers import CourseShortSerializer
from education.serializers import GroupShortSerializer


class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = ('email', 'first_name', 'last_name', 'password',
                  'phone_number', 'is_partner', 'is_student', 'is_teacher',)


class CustomUserSerializer(UserSerializer):

    class Meta:
        model = CustomUser
        fields = ('id', 'first_name', 'last_name', 'email', 'phone_number',)


class StudentProfileSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='user.pk', read_only=True)
    url = serializers.SerializerMethodField(read_only=True)
    avatar = serializers.ImageField(use_url=True)
    involved = GroupShortSerializer(many=True, read_only=True, source='group_set')

    class Meta:
        model = Student
        fields = [
            'id', 'url', 'avatar', 'first_name_lat',
            'last_name_lat', 'username', 'birth_date',
            'country', 'city', 'can_relocate', 'can_full_time',
            'can_part_time', 'can_remote', 'sex', 'company',
            'position',
            'involved',
        ]

    def get_url(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)


class StudentProfileCreateOrUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        exclude = ['created_at', 'updated_at', ]


class TeacherProfileSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)
    id = serializers.IntegerField(source='user.pk', read_only=True)
    avatar = serializers.ImageField(use_url=True)
    involved = GroupShortSerializer(many=True, read_only=True, source='group_set')

    class Meta:
        model = Teacher
        fields = [
            'id', 'url', 'avatar', 'bio',
            'username', 'company', 'position',
            'involved',
        ]

    def get_url(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)


class TeacherProfileCreateOrUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        exclude = ['created_at', 'updated_at', ]


class PartnerProfileSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)
    id = serializers.IntegerField(source='user.pk', read_only=True)
    courses = CourseShortSerializer(many=True, read_only=True)
    logo = serializers.ImageField(use_url=True)

    class Meta:
        model = Partner
        fields = ['id', 'url', 'logo', 'company', 'info', 'courses', ]

    def get_url(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)


class PartnerProfileCreateOrUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Partner
        exclude = ['created_at', 'updated_at', ]


class CustomUserWithProfileSerializer(UserSerializer):
    student_profile = StudentProfileSerializer(read_only=True, source='student')
    teacher_profile = TeacherProfileSerializer(read_only=True, source='teacher')
    partner_profile = PartnerProfileSerializer(read_only=True, source='partner')

    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'first_name', 'last_name',
                  'phone_number',
                  # 'is_partner', 'is_student', 'is_teacher',
                  'student_profile', 'teacher_profile', 'partner_profile']
