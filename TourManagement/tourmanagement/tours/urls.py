from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
# from .admin import admin_site

router = DefaultRouter()
router.register('user', views.UserViewSet, basename='user')
router.register('departure', views.DepartureViewSet, basename='departure')
router.register('tour_detail', views.TourViewSet, basename='tour_detail')
router.register('blog', views.BlogViewSet, basename='blog')
router.register('cmt_tour', views.CmtTourViewSet, basename='cmt_tour')
router.register('cmt_blog', views.CmtBlogViewSet, basename='cmt_blog')
router.register('like', views.LikeViewSet, basename='like')
router.register('rating', views.RatingViewSet, basename='rating')
router.register('destination', views.DestinationViewSet, basename='destination')
router.register('staff', views.StaffViewSet, basename='staff')

router.register('transport', views.TransportViewSet, basename='transport')
router.register('booking', views.BookingViewSet, basename='booking')
router.register('hotel', views.HotelViewSet, basename='hotel')
router.register('img_detail', views.ImgDetailViewSet, basename='img_detail')
router.register('tag_blog', views.TagBlogViewSet, basename='tag_blog')
router.register('tag_country', views.TagCountryViewSet, basename='tag_country')
router.register('tag_tour_detail', views.TagTourDetailViewSet, basename='tag_tour_detail')
router.register('view', views.IncViewsViewSet, basename='view')


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('get_code/', views.VerifyEmail,name = "verify"),
    # path('emailVerification/<uidb64>/<token>', views.activate, name='emailActivate'),
    path('oauth2-info/', views.AuthInfo.as_view()),
    path('accounts/',include('django.contrib.auth.urls')),
    # path('index/', views.index, name="index"),

]
