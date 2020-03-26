from rest_framework import viewsets

from users.permissions import IsAdminUser, IsPartnerUser, IsStudentUser, IsTeacherUser, IsOwnerOrAdmin
from users.models import Partner, Student, Teacher
from users import serializers


class UserProfileViewSet(viewsets.ModelViewSet):
    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = (IsAdminUser | self.user_type_role,)
        elif self.action == 'update' or self.action == 'partial_update':
            permission_classes = (IsOwnerOrAdmin,)
        elif self.action == 'destroy':
            permission_classes = (IsAdminUser,)
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update', ]:
            return self.write_serializer
        return self.read_serializer


class PartnerProfileViewSet(UserProfileViewSet):
    queryset = Partner.objects.select_related('user').prefetch_related('courses')

    user_type_role = IsPartnerUser
    write_serializer = serializers.PartnerProfileCreateOrUpdateSerializer
    read_serializer = serializers.PartnerProfileSerializer


class StudentProfileViewSet(UserProfileViewSet):
    queryset = Student.objects.select_related('user').prefetch_related('group_set')

    user_type_role = IsStudentUser
    write_serializer = serializers.StudentProfileCreateOrUpdateSerializer
    read_serializer = serializers.StudentProfileSerializer


class TeacherProfileViewSet(UserProfileViewSet):
    queryset = Teacher.objects.select_related('user').prefetch_related('group_set')

    user_type_role = IsTeacherUser
    write_serializer = serializers.TeacherProfileCreateOrUpdateSerializer
    read_serializer = serializers.TeacherProfileSerializer
