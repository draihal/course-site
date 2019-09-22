from rest_framework import viewsets
from rest_framework import mixins

from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from users.permissions import IsLoggedInUserOrAdmin, IsAdminUser
#
# from users.models import CustomUser
# from users.serializers import UserSerializer
#
#
# class StudentUserViewSet(viewsets.ModelViewSet):
#     queryset = CustomUser.objects.all()
#     serializer_class = UserSerializer
#
#     def get_permissions(self):
#         permission_classes = []
#         if self.action == 'create':
#             permission_classes = [AllowAny]
#         elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
#             permission_classes = [IsLoggedInUserOrAdmin]
#         elif self.action == 'list' or self.action == 'destroy':
#             permission_classes = [IsAdminUser]
#         return [permission() for permission in permission_classes]

from users.models import Partner, Student, Teacher
from users.serializers import PartnerProfileSerializer, StudentProfileSerializer, TeacherProfileSerializer


class PartnerProfileViewSet(viewsets.ModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerProfileSerializer

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [AllowAny]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsLoggedInUserOrAdmin]
        elif self.action == 'destroy':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


class StudentProfileViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentProfileSerializer


class TeacherProfileViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherProfileSerializer
