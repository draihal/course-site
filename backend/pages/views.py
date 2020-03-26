from django.db import ProgrammingError
from rest_framework import viewsets, mixins

from users.permissions import IsAdminUser, IsTeacherUser, IsStudentUser
from pages import models
from pages import serializers


class SoloPageViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    def get_object(self):
        obj = self.model_solo
        self.check_object_permissions(self.request, obj)
        return obj

    def list(self, *args, **kwargs):
        return self.retrieve(*args, **kwargs)


class AboutUsPageViewSet(SoloPageViewSet):
    serializer_class = serializers.AboutUsPageSerializer

    try:
        model_solo = models.AboutUsPage.get_solo()  # objects.get() #get_solo()  #objects.first() objects.filter(pk='1')
    except ProgrammingError as e:
        model_solo = models.AboutUsPage.objects.all()


class SiteConfigurationViewSet(SoloPageViewSet):
    serializer_class = serializers.SiteConfigurationSerializer

    try:
        model_solo = models.SiteConfiguration.get_solo()
    except ProgrammingError as e:
        model_solo = models.SiteConfiguration.objects.all()


class ContactsPageViewSet(SoloPageViewSet):
    serializer_class = serializers.ContactsPageSerializer

    try:
        model_solo = models.ContactsPage.get_solo()
    except ProgrammingError as e:
        model_solo = models.ContactsPage.objects.all()


class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Course.objects.all()
    lookup_field = 'slug'
    serializer_class = serializers.CourseSerializer


class CourseCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.CourseCategory.objects.prefetch_related('course_set')
    lookup_field = 'slug'
    serializer_class = serializers.CourseCategorySerializer


class MassMediaPublicationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.MassMediaPublication.objects.all()
    lookup_field = 'slug'
    serializer_class = serializers.MassMediaPublicationSerializer


class PagesViewSet(viewsets.ModelViewSet):
    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = (IsAdminUser | self.user_type_role,)
        elif self.action in ['update', 'partial_update']:
            permission_classes = (IsAdminUser | self.user_type_role,)
        elif self.action == 'destroy':
            permission_classes = (IsAdminUser,)
        return [permission() for permission in permission_classes]


class EventViewSet(PagesViewSet):
    queryset = models.Event.objects.select_related('speaker', 'course', 'speaker__user')
    lookup_field = 'slug'
    serializer_class = serializers.EventSerializer

    user_type_role = IsTeacherUser


class ReviewViewSet(PagesViewSet):
    queryset = models.Review.objects.select_related('student', 'course', 'student__user')
    serializer_class = serializers.ReviewSerializer

    user_type_role = IsStudentUser


class IndexViewSet(SoloPageViewSet):
    serializer_class = serializers.IndexPageSerializer

    try:
        model_solo = models.IndexPage.get_solo()
    except ProgrammingError as e:
        model_solo = models.IndexPage.objects.all()
