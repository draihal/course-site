from rest_framework import viewsets, mixins

from users.permissions import IsLoggedInUserOrAdmin, IsAdminUser, IsTeacherUser, IsStudentUser
from pages import models
from pages import serializers


class AboutUsPageViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = serializers.AboutUsPageSerializer

    def get_object(self):
        obj = models.AboutUsPage.get_solo()
        self.check_object_permissions(self.request, obj)
        return obj

    def list(self, *args, **kwargs):
        return self.retrieve(*args, **kwargs)


# class AboutUsPageViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = models.AboutUsPage.objects.get()
#     serializer_class = AboutUsPageSerializer

#
# class SiteConfigurationViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = models.SiteConfiguration.objects.get()
#     serializer_class = SiteConfigurationSerializer


class SiteConfigurationViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = serializers.SiteConfigurationSerializer

    def get_object(self):
        obj = models.SiteConfiguration.get_solo()
        self.check_object_permissions(self.request, obj)
        return obj

    def list(self, *args, **kwargs):
        return self.retrieve(*args, **kwargs)


# class ContactsPageViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = models.ContactsPage.objects.get()
#     serializer_class = ContactsPageSerializer


class ContactsPageViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = serializers.ContactsPageSerializer

    def get_object(self):
        obj = models.ContactsPage.get_solo()
        self.check_object_permissions(self.request, obj)
        return obj

    def list(self, *args, **kwargs):
        return self.retrieve(*args, **kwargs)


class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Course.objects.all()
    lookup_field = 'slug'
    serializer_class = serializers.CourseSerializer


class CourseCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.CourseCategory.objects.all()
    lookup_field = 'slug'
    serializer_class = serializers.CourseCategorySerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = models.Event.objects.all()
    lookup_field = 'slug'
    serializer_class = serializers.EventSerializer

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [IsTeacherUser]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsLoggedInUserOrAdmin]
        elif self.action == 'destroy':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


class MassMediaPublicationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.MassMediaPublication.objects.all()
    lookup_field = 'slug'
    serializer_class = serializers.MassMediaPublicationSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [IsStudentUser]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsAdminUser]
        elif self.action == 'destroy':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]
