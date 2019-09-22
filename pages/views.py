from rest_framework import viewsets

from users.permissions import IsLoggedInUserOrAdmin, IsAdminUser, IsPartnerOrAdminUser
from pages.models import (
    AboutUsPage, ContactsPage, CourseCategory,
    Course, Event, MassMediaPublication, Review, SiteConfiguration
)
from pages.serializers import CourseShortSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseShortSerializer  # TODO change!
