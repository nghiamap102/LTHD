"""tourmanagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetCompleteView, \
    PasswordResetConfirmView

schema_view = get_schema_view(
    openapi.Info(
        title="Course API",
        default_version='v1',
        description="APIs for CourseApp",
        contact=openapi.Contact(email="1851050093nghia@ou.edu.vn"),
        license=openapi.License(name="Bededuxe@2021"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path('', include('tours.urls')),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('reset-password', include(''), name='password_reset'),
    # path('reset-password/done', PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('reset-password/confirm/<uidb64>[0-9A-Za-z]+)-<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('reset-password/complete/',PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
]
