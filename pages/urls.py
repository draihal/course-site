from django.urls import path, include

from rest_framework import routers

from pages import views


app_name = 'pages'


router = routers.DefaultRouter()
router.register('pages/about-us', views.AboutUsPageViewSet, 'about-us')
router.register('pages', views.SiteConfigurationViewSet, 'site-configuration')
router.register('pages/contacts', views.ContactsPageViewSet, 'contacts')
router.register('pages/courses', views.CourseViewSet, 'courses')
router.register('pages/categories', views.CourseCategoryViewSet, 'categories')
router.register('pages/events', views.EventViewSet, 'events')
router.register('pages/publications', views.MassMediaPublicationViewSet, 'publications')
router.register('pages/reviews', views.ReviewViewSet, 'reviews')


urlpatterns = [
    path('', include(router.urls)),
]
