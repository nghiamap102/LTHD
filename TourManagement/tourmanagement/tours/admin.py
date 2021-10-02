from django.contrib import admin
from django.contrib.auth.models import Permission
from django.template.response import TemplateResponse
from django.utils.html import mark_safe
from django import forms
from django.db.models import Count
from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.urls import path


class ToursTagInline(admin.TabularInline):
    model = ToursTotal.tags.through

class TourDetailInline(admin.TabularInline):
    model = ToursDetail

class ToursDetailHotelInline(admin.TabularInline):
    model = ToursDetail.hotel.through


class ToursDetailTransportInline(admin.TabularInline):
    model = ToursDetail.transport.through

class TourDetailInline(admin.StackedInline):
    model = ToursDetail


class CmtInLine(admin.StackedInline):
    model = Comment

class TourDetailImgDetailInline(admin.StackedInline):
    model = ImgDetail



class CmtAdmin(admin.ModelAdmin):
    # list_display = [field.name for field in Comment._meta.fields]
    list_display = ["id" , "customer","tourdetail","created_date"]
    list_filter = ["customer","tourdetail","created_date"]
    search_fields = ["customer","tourdetail","created_date"]

class News(admin.ModelAdmin):
    list_display = ['id','name','created_date','active']
    search_fields = ['id','name']
    readonly_fields = ['picture']

class TourTotalAdmin(admin.ModelAdmin):

    list_display = ['id', 'name', 'created_date', 'active', 'image','count']
    search_fields = ['id', 'name','tags']
    list_filter = ['name', 'active','tags']
    readonly_fields = ['picture','count']
    inlines = [ToursTagInline,TourDetailInline ]

    def count(self,obj):
        return obj.details.count()

    def picture(self, tours):
        return mark_safe(
            "<img src = /{img_url} alt = '{alt}' width='120px'/>"
                .format(img_url=tours.imageTours.name, alt=tours.name))


class TourDetailForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = ToursTotal
        fields = '__all__'


class TourDetailAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'timestart', 'timefinish', 'price','image']
    search_fields = ['id', 'name', 'price']
    list_filter = ['id', 'name', 'price']
    inlines = [ ToursDetailHotelInline,TourDetailImgDetailInline]

    def picture(self, toursdetail):
        return mark_safe(
            "<img src = /static/{img_url} alt = '{alt}' width='120px'/>"
                .format(img_url=toursdetail.imageHotel.name, alt=toursdetail.name))


class ToursAppAdmin(admin.AdminSite):
    site_header = 'HE THONG QUAN LI DU LỊCH'

    def get_urls(self):
        return [
                   path('tours_stats/', self.tours_stats)
               ] + super().get_urls()

    def tours_stats(self, request):
        tours_detail_count = ToursDetail.objects.count()  # đếm số tour chi tiết
        stats = ToursTotal.objects.annotate(tours_detail_count=Count('tours')).values("id", "name",
                                                                                      "tours_detail_count")
        return TemplateResponse(request, 'admin/course-stats.html', {
            'tours_detail_count': tours_detail_count,
            'stats': stats
        })

class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "first_name", "last_name", "username","is_superuser","is_staff" ,"date_joined","is_active"]


admin_site = ToursAppAdmin('myqldl')

admin_site.register(User,UserAdmin)
admin_site.register(ToursTotal, TourTotalAdmin)
admin_site.register(ToursDetail, TourDetailAdmin)
admin_site.register(Hotel)
admin_site.register(Tag)
admin_site.register(ImgDetail)
admin_site.register(Comment,CmtAdmin)
admin_site.register(Transport)
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
