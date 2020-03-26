from rest_framework import viewsets

from users.permissions import IsAdminUser, IsTeacherUser, IsStudentUser
from education import models
from education import serializers


class EducationAppViewSet(viewsets.ModelViewSet):
    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = (IsAdminUser | self.user_type_role,)
        elif self.action in ['retrieve', 'update', 'partial_update']:
            permission_classes = (IsAdminUser | self.user_type_role,)
        elif self.action in ['destroy', 'list']:
            permission_classes = (IsAdminUser,)
        return [permission() for permission in permission_classes]


class HomeworkViewSet(EducationAppViewSet):
    queryset = models.Homework.objects.all()
    serializer_class = serializers.HomeworkSerializer

    user_type_role = (IsTeacherUser | IsStudentUser)


class GradeViewSet(EducationAppViewSet):
    queryset = models.Grade.objects.all()
    serializer_class = serializers.GradeSerializer

    user_type_role = (IsTeacherUser | IsStudentUser)


class GroupViewSet(EducationAppViewSet):
    queryset = models.Group.objects.prefetch_related('students', 'students__user', 'teachers', 'teachers__user')
    lookup_field = 'slug'
    serializer_class = serializers.GroupSerializer

    user_type_role = (IsTeacherUser | IsStudentUser)


class LessonViewSet(EducationAppViewSet):
    queryset = models.Lesson.objects.all()
    lookup_field = 'slug'
    serializer_class = serializers.LessonSerializer

    user_type_role = (IsTeacherUser | IsStudentUser)


class ModuleViewSet(EducationAppViewSet):
    queryset = models.Module.objects.all()
    serializer_class = serializers.ModuleSerializer

    user_type_role = (IsTeacherUser | IsStudentUser)


class PaymentViewSet(EducationAppViewSet):
    queryset = models.Payment.objects.all()
    serializer_class = serializers.PaymentSerializer

    user_type_role = (IsTeacherUser | IsStudentUser)
