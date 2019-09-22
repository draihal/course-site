from django.urls import path, include

from rest_framework import routers

from pages.views import CourseViewSet


app_name = 'pages'


router = routers.DefaultRouter()
router.register('pages/course', CourseViewSet, 'course')


urlpatterns = [
    path('', include(router.urls)),
]