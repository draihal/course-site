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
        fields = ('id', 'first_name', 'last_name', )
        # read_only_fields = (CustomUser.USERNAME_FIELD,)


class StudentProfileSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)
    id = serializers.IntegerField(source='user.pk', read_only=True)
    avatar = serializers.ImageField(use_url=True)
    involved = GroupShortSerializer(many=True, read_only=True, source='group_set')

    class Meta:
        model = Student
        fields = [
            'id', 'user', 'url', 'avatar', 'first_name_lat',
            'last_name_lat', 'username', 'birth_date',
            'country', 'city', 'relocate', 'full_time',
            'part_time', 'remote', 'remote', 'sex', 'company',
            'position', 'involved',
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
    user = CustomUserSerializer(read_only=True,)
    # first_name = CustomUserSerializer(source='user.first_name', read_only=True,)
    # last_name = CustomUserSerializer(source='user.last_name', read_only=True, )

    class Meta:
        model = Teacher
        fields = [
            'id', 'user', 'url', 'avatar', 'bio',
            # 'first_name', 'last_name',
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

    # def create(self, validated_data):
    #     return Partner.objects.create(updated_at=, **validated_data)


# class CustomUserCreateSerializer(UserCreateSerializer):
#     class Meta:
#         fields = tuple(CustomUser.REQUIRED_FIELDS) + (
#             CustomUser.USERNAME_FIELD,
#             CustomUser._meta.pk.name,
#             'password',
#             'last_name',
#             'is_partner',
#             'is_student',
#             'is_teacher',
#         )
