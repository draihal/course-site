from rest_framework import viewsets

from users.permissions import IsAdminUser, IsPartnerUser, IsStudentUser, IsTeacherUser, IsOwnerOrAdmin
from users.models import Partner, Student, Teacher
from users import serializers


class PartnerProfileViewSet(viewsets.ModelViewSet):
    queryset = Partner.objects.select_related('user').prefetch_related('courses')

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = (IsAdminUser | IsPartnerUser,)
        elif self.action == 'update' or self.action == 'partial_update':
            permission_classes = (IsOwnerOrAdmin,)
        elif self.action == 'destroy':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update' or self.action == 'partial_update':
            return serializers.PartnerProfileCreateOrUpdateSerializer
        return serializers.PartnerProfileSerializer


class StudentProfileViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.select_related('user').prefetch_related('group_set')

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = (IsAdminUser | IsStudentUser,)
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = (IsOwnerOrAdmin,)
        elif self.action == 'destroy' or self.action == 'list':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update' or self.action == 'partial_update':
            return serializers.StudentProfileCreateOrUpdateSerializer
        return serializers.StudentProfileSerializer


class TeacherProfileViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.select_related('user').prefetch_related('group_set')

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = (IsAdminUser | IsTeacherUser,)
        elif self.action == 'update' or self.action == 'partial_update':
            permission_classes = (IsOwnerOrAdmin,)
        elif self.action == 'destroy':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update' or self.action == 'partial_update':
            return serializers.TeacherProfileCreateOrUpdateSerializer
        return serializers.TeacherProfileSerializer
