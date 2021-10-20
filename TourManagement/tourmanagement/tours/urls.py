from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .admin import admin_site

router = DefaultRouter()
router.register('user', views.UserViewSet, basename='user')
router.register('tour', views.TourTotalViewSet, basename='tour')
router.register('tour_detail', views.ToursDetailViewSet, basename='tour_detail')
router.register('blog', views.BlogViewSet, basename='blog')
router.register('cmt_tour', views.CmtTourViewSet, basename='cmt_tour')
router.register('cmt_blog', views.CmtBlogViewSet, basename='cmt_blog')
router.register('like', views.LikeViewSet, basename='like')
router.register('rating', views.RatingViewSet, basename='rating')
router.register('tags', views.TagViewSet, basename='tags')
router.register('transport', views.TransportViewSet, basename='transport')
router.register('booking', views.BookingDetailViewSet, basename='booking')
router.register('static', views.StaticViewSet, basename='static')

router.register('hotel', views.HotelViewSet, basename='hotel')
router.register('img_detail', views.ImgDetailViewSet, basename='img_detail')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin_site.urls),
    path('oauth2-info/', views.AuthInfo.as_view())
]
