from django.urls import path, include

from rest_framework import routers

from users.views import PartnerProfileViewSet, StudentProfileViewSet, TeacherProfileViewSet


app_name = 'users'


router = routers.DefaultRouter()
router.register('profile/partner', PartnerProfileViewSet, 'partner-profile')
router.register('profile/student', StudentProfileViewSet, 'student-profile')
router.register('profile/teacher', TeacherProfileViewSet, 'teacher-profile')


urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
    path('', include(router.urls)),
]
