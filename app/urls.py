"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, re_path, include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Courses API",
      default_version='v1',
      description="API for courses site",
      contact=openapi.Contact(email="draihal.a@gmail.com"),
   ),
   # if False, includes only endpoints the current user has access to
   public=False,
   permission_classes=(permissions.AllowAny,),
)

admin.site.site_header = "Сайт курсов"
admin.site.site_title = "Сайт курсов"
admin.site.index_title = "Добро пожаловать в панель управления сайта курсов!"


# def trigger_error(request):
#     division_by_zero = 1 / 0


urlpatterns = [
    path('courses-admin/', admin.site.urls, name='admin'),
    re_path(r'^api/v1/swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('api/v1/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/v1/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/v1/', include('users.urls')),
    path('api/v1/', include('pages.urls')),
    path('api/v1/', include('education.urls')),
    # path('sentry-debug/', trigger_error),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
