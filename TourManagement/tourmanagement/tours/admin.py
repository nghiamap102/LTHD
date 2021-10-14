from django.contrib import admin
from django.template.response import TemplateResponse
from django.utils.html import mark_safe
from .models import *
from django.urls import path
from .serializers import TagSerializers
from rest_framework import serializers


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


class TourAppAdmin(admin.AdminSite):
    site_header = 'HE THONG QUAN LI DU LỊCH'

    def get_urls(self):
        return [
                   path('tours_stats/', self.tours_stats)
               ] + super().get_urls()

    def tours_stats(self, request):
        # tours_detail_count = TourTotal.objects.count()  # đếm số tour chi tiết
        # stats = TourTotal.objects.annotate(tours_detail_count=Count('tours')).values("id", "name",
        #                                                                              "tours_detail_count")
        return TemplateResponse(request, 'admin/course-stats.html', {
            # 'tours_detail_count': tours_detail_count,
            # 'stats': stats
        })


class TourTotalAdmin(admin.ModelAdmin):
    tags = TagSerializers(many=True)
    count_detail = serializers.SerializerMethodField('count_detail')

    def count_detail(self, tour):
        return tour.detail.count()

    list_display = ['id', 'name', 'image', 'tags', 'content', 'active', 'count_detail']
    inlines = [TourDetailStackInLine]


class TourDetailAdmin(admin.ModelAdmin):
    list_display = [f.name for f in TourDetail._meta.fields]
    list_filter = ['created_date']
    search_fields = ['name', 'duration']
    inlines = [TourDetailImgDetailInline, BlogInline]

    # def picture(self, tour_detail):
    #     return mark_safe(
    #         "<img src = /static/{img_url} alt = '{alt}' width='120px'/>"
    #             .format(img_url=tour_detail.image.name, alt=tour_detail.name))


class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "first_name", "last_name", "username", "is_superuser", "is_staff", 'active_staff',
                    "date_joined", "is_active"]


class BlogAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Blog._meta.fields]


class LikeAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Like._meta.fields]


class CmtBlogAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CommentBlog._meta.fields]


class BookingAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Booking._meta.fields]


class CmtTourAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CommentTourDetail._meta.fields]


# class BookingAdmin(admin.ModelAdmin):
#     list_display = ['customer', 'tour', 'adult', 'children', 'status', 'total', 'created_date']
#     list_filter = ['created_date']
#     search_fields = ['tour']

admin_site = TourAppAdmin('myqldl')

admin_site.register(User, UserAdmin)
admin_site.register(TourTotal, TourTotalAdmin)
admin_site.register(TourDetail, TourDetailAdmin)
admin_site.register(CommentTourDetail, CmtTourAdmin)
admin_site.register(CommentBlog, CmtBlogAdmin)
admin_site.register(Booking,BookingAdmin)
admin_site.register(Hotel)
admin_site.register(Tag)
admin_site.register(ImgDetail)
admin_site.register(Transport)
admin_site.register(Blog, BlogAdmin)
admin_site.register(Rating)
admin_site.register(Like, LikeAdmin)

# admin_site.register(Point)
# admin_site.register(Permission)


# admin.site.register(User)
# admin.site.register(ToursTotal, TourTotalAdmin)
# admin.site.register(ToursDetail, TourDetailAdmin)
# admin.site.register(Hotel)
# admin.site.register(Permission)
# admin.site.register(Employee)
# admin.site.register(News)
# admin.site.register(Feedback)
# admin.site.register(Static)
