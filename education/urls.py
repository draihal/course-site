from django.urls import path, include

from rest_framework import routers

from education.views import GroupViewSet


app_name = 'education'


router = routers.DefaultRouter()
router.register('group', GroupViewSet, 'group')


urlpatterns = [
    path('', include(router.urls)),
]