from django.urls import path, include

from rest_framework import routers

from pages.views import CourseViewSet, AboutUsPageViewSet, SiteConfigurationViewSet, ContactsPageViewSet


app_name = 'pages'


router = routers.DefaultRouter()
router.register('pages/about-us', AboutUsPageViewSet, 'about-us')
router.register('pages/site-configuration', SiteConfigurationViewSet, 'site-configuration')
router.register('pages/contacts', ContactsPageViewSet, 'contacts')
router.register('pages/courses', CourseViewSet, 'courses')
# router.register('pages/categories', CourseCategoryViewSet, 'course-category')


urlpatterns = [
    path('', include(router.urls)),
]
