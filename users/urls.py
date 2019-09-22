from django.urls import path, include

from djoser import views as djoser_views
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views

from users.views import PartnerProfileViewSet, StudentProfileViewSet, TeacherProfileViewSet

from djoser import views as djsoer_views


router = routers.DefaultRouter()
router.register('profile/partner', PartnerProfileViewSet, 'partner-profile')
router.register('profile/student', StudentProfileViewSet, 'student-profile')
router.register('profile/teacher', TeacherProfileViewSet, 'teacher-profile')


urlpatterns = [
    # path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    # path('token/verify/', jwt_views.TokenVerifyView.as_view(), name='token_verify'),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),


    # path('user/view/', djoser_views.UserView.as_view(), name='user-view'),
    # path('user/delete/', djoser_views.UserDeleteView.as_view(), name='user-delete'),
    # path('user/create/', djoser_views.UserCreateView.as_view(), name='user-create'),


    path('', include(router.urls)),
]
