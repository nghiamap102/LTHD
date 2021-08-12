from django.contrib import admin
from django.urls import path,include
from . import  views
from rest_framework.routers import DefaultRouter
from .admin import admin_site

router = DefaultRouter()
router.register('tours', views.ToursTotalViewSet)
router.register('hotel', views.HotelViewSet)
router.register('users', views.UserViewSet)
router.register('tousdetail', views.ToursDetailViewSet)
# router.register('employee', views.UserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/',admin_site.urls),
    path('',views.index, name= 'index'),
    # path('tour/' ,admin_site.urls)
]
