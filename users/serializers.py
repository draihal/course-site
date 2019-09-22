from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers

from users.models import CustomUser, Student, Teacher, Partner


class StudentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        # fields = '__all__'
        exclude = ['updated_at', 'user']


class TeacherProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        # fields = '__all__'
        exclude = ['updated_at', 'user']


class PartnerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        # fields = '__all__'
        exclude = ['updated_at', 'user']


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

class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = ('email', 'first_name', 'last_name', 'password',
                  'phone_number', 'is_partner', 'is_student', 'is_teacher',)


class CustomUserSerializer(UserSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'first_name', 'last_name', )
        # read_only_fields = (CustomUser.USERNAME_FIELD,)
