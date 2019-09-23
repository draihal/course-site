from rest_framework import viewsets, mixins

from users.permissions import IsLoggedInUserOrAdmin, IsAdminUser, IsPartnerOrAdminUser
from pages import models
from pages.serializers import CourseShortSerializer, AboutUsPageSerializer, SiteConfigurationSerializer, ContactsPageSerializer


class AboutUsPageViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = AboutUsPageSerializer

    def get_object(self):
        obj = models.AboutUsPage.get_solo()
        self.check_object_permissions(self.request, obj)
        return obj

    def list(self, *args, **kwargs):
        return self.retrieve(*args, **kwargs)


class CourseViewSet(viewsets.ModelViewSet):
    queryset = models.Course.objects.all()
    serializer_class = CourseShortSerializer  # TODO change!


# class AboutUsPageViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = models.AboutUsPage.objects.get()
#     serializer_class = AboutUsPageSerializer

#
# class SiteConfigurationViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = models.SiteConfiguration.objects.get()
#     serializer_class = SiteConfigurationSerializer


class SiteConfigurationViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = SiteConfigurationSerializer

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
    serializer_class = ContactsPageSerializer

    def get_object(self):
        obj = models.ContactsPage.get_solo()
        self.check_object_permissions(self.request, obj)
        return obj

    def list(self, *args, **kwargs):
        return self.retrieve(*args, **kwargs)
