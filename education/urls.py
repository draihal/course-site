from django.urls import path, include

from rest_framework import routers

from education import views


app_name = 'education'


router = routers.DefaultRouter()
router.register('education/grades', views.GradeViewSet, 'grades')
router.register('education/homework', views.HomeworkViewSet, 'homework')
router.register('education/groups', views.GroupViewSet, 'groups')
router.register('education/lessons', views.LessonViewSet, 'lessons')
router.register('education/modules', views.ModuleViewSet, 'modules')
router.register('education/payments', views.PaymentViewSet, 'payments')


urlpatterns = [
    path('', include(router.urls)),
]