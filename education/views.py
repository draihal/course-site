from rest_framework import viewsets

from users.permissions import IsLoggedInUserOrAdmin, IsAdminUser, IsPartnerOrAdminUser
from education import models
from education import serializers


class GroupViewSet(viewsets.ModelViewSet):
    queryset = models.Group.objects.all()
    serializer_class = serializers.GroupShortSerializer  # TODO change!

