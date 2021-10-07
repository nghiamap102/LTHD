from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .admin import admin_site

router = DefaultRouter()
router.register('tours', views.TourTotalViewSet, basename='tours')
router.register('hotel', views.HotelViewSet, basename='hotel')
router.register('users', views.UserViewSet, basename='users')
router.register('cmt', views.CmtViewSet, basename='cmt')
router.register('tour_detail', views.ToursDetailViewSet, basename='tour_detail')
router.register('blog', views.BlogViewSet, basename='blog')
router.register('booking_detail', views.BookingDetailViewSet, basename='booking_detail')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin_site.urls),
    path('oauth2-info/', views.AuthInfo.as_view())
]
