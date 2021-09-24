from django.contrib import admin
from django.urls import path,include
from . import  views
from rest_framework.routers import DefaultRouter
from .admin import admin_site

router = DefaultRouter()
router.register('tours', views.TourTotalViewSet, basename='tours')
router.register('hotel', views.HotelViewSet, basename='hotel')
router.register('users', views.UserViewSet, basename='users')
router.register('cmt', views.CmtViewSet, basename='cmt')
router.register('tousdetail', views.ToursDetailViewSet, basename='tousdetail')
# router.register('employee', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/',admin_site.urls),
    # path('',views.index, name= 'index'),
    # path('list_tour/',views.list_tour,name ='list_tour'),
    # path('tour_detail/',views.tour_detail , name = 'tour_detail'),
    # path('booking/' , views , name=''booking ),
    # path('login/',views.login , name = 'login'),
    # path('contact/',views.contact , name= 'contact' ),
    # path('tour/' ,admin_site.urls)
]
