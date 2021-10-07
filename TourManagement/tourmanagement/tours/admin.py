from django.contrib import admin
from django.contrib.auth.models import Permission
from django.template.response import TemplateResponse
from django.utils.html import mark_safe
from django import forms
from django.db.models import Count
from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.urls import path

from .serializers import TagSerializers


class TourDetailImgDetailInline(admin.StackedInline):
    model = ImgDetail


class TourDetailStackInLine(admin.StackedInline):
    model = TourDetail


class TransportInline(admin.StackedInline):
    model = Transport


class HotelInline(admin.StackedInline):
    model = Hotel


class BlogInline(admin.StackedInline):
    model = Blog


class TourTotalAdmin(admin.ModelAdmin):
    tags = TagSerializers(many=True)
    list_display = ['id', 'name', 'image', 'count', 'tags', 'content', 'active']
    search_fields = ['id', 'name', 'tags']
    list_filter = ['name', 'active', 'tags']
    readonly_fields = ['picture', 'count']

    inlines = [TourDetailStackInLine]

    def count(self, obj):
        return obj.detail.count()

    def picture(self, tours):
        return mark_safe(
            "<img src = /{img_url} alt = '{alt}' width='120px'/>"
                .format(img_url=tours.image.name, alt=tours.name))


class TourDetailAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'time_start', 'duration', 'price', 'tour', 'discount', 'status', 'active']
    search_fields = ['status', 'discount', 'time_start', 'price', 'tour']
    list_filter = ['status', 'discount', 'time_start', 'price', 'tour']

    inlines = [TourDetailImgDetailInline, BlogInline]

    def picture(self, tour_detail):
        return mark_safe(
            "<img src = /static/{img_url} alt = '{alt}' width='120px'/>"
                .format(img_url=tour_detail.image.name, alt=tour_detail.name))


class TourAppAdmin(admin.AdminSite):
    site_header = 'HE THONG QUAN LI DU LỊCH'

    def get_urls(self):
        return [
                   path('tours_stats/', self.tours_stats)
               ] + super().get_urls()

    def tours_stats(self, request):
        tours_detail_count = TourTotal.objects.count()  # đếm số tour chi tiết
        stats = TourTotal.objects.annotate(tours_detail_count=Count('tours')).values("id", "name",
                                                                                     "tours_detail_count")
        return TemplateResponse(request, 'admin/course-stats.html', {
            'tours_detail_count': tours_detail_count,
            'stats': stats
        })


class CmtAdmin(admin.ModelAdmin):
    # list_display = [field.name for field in Comment._meta.fields]
    list_display = ["id", "customer", "tour_detail", "created_date"]
    list_filter = ["customer", "tour_detail", "created_date"]
    search_fields = ["customer", "tour_detail", "created_date"]


class BookingAdmin(admin.ModelAdmin):
    list_display = ['customer', 'tour', 'adult', 'children', 'status', 'total', 'created_date']
    list_filter = ['created_date']
    search_fields = ['tour']

class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "first_name", "last_name", "username", "is_superuser", "is_staff", "date_joined", "is_active"]


admin_site = TourAppAdmin('myqldl')

admin_site.register(User, UserAdmin)
admin_site.register(TourTotal, TourTotalAdmin)
admin_site.register(TourDetail, TourDetailAdmin)
admin_site.register(Comment, CmtAdmin)
admin_site.register(Booking)
admin_site.register(Hotel)
admin_site.register(Tag)
admin_site.register(ImgDetail)
admin_site.register(Transport)
admin_site.register(Blog)
admin_site.register(Permission)

# admin.site.register(User)
# admin.site.register(ToursTotal, TourTotalAdmin)
# admin.site.register(ToursDetail, TourDetailAdmin)
# admin.site.register(Hotel)
# admin.site.register(Tag)
# admin.site.register(Permission)
# admin.site.register(Employee)
# admin.site.register(News)
# admin.site.register(Feedback)
# admin.site.register(Static)
