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


class ToursDetailHotelInline(admin.TabularInline):
    model = ToursDetail.hotel.through

class ToursDetailTransportInline(admin.TabularInline):
    model = ToursDetail.transport.through

class TourTotalAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_date', 'count', 'active', 'get_tags']
    search_fields = ['id', 'name', 'tags__name']
    list_filter = ['name', 'active', 'tags__name']
    readonly_fields = ['picture']
    inlines = [ToursTagInline, ]

    def picture(self, tours):
        return mark_safe(
            "<img src = /static/{img_url} alt = '{alt}' width='120px'/>"
                .format(img_url=tours.imageTours.name, alt=tours.name))

class TourDetailForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = ToursTotal
        fields = '__all__'


class TourDetailAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'timestart', 'timefinish', 'vat', 'price', 'get_hotels']
    search_fields = ['id', 'name', 'price']
    list_filter = ['id', 'name', 'price', 'hotel__name']
    inlines = [ToursDetailHotelInline,ToursDetailHotelInline]
    readonly_fields = ['picture']

    def picture(self, toursdetail):
        return mark_safe(
            "<img src = /static/{img_url} alt = '{alt}' width='120px'/>"
                .format(img_url=toursdetail.imageHotel.name, alt=toursdetail.name))


class TourDetailInline(admin.StackedInline):
    model = ToursDetail
    fk_name = 'tours'

class TourInline(admin.StackedInline):
    inlines = (TourDetailInline)


class ToursAppAdmin(admin.AdminSite):
    site_header = 'HE THON QUAN LI DU LỊCH'

    def get_urls(self):
        return [
                   path('tours_stats/', self.course_stats)
               ] + super().get_urls()

    def course_stats(self, request):
        tours_count = ToursTotal.objects.count()
        stats = ToursTotal.objects.annotate(tours_count=Count('tours')).values("id", "name", "tours_count")
        return TemplateResponse(request, 'admin/course-stats.html', {
            'tours_count': tours_count,
            'stats': stats
        })



# newss
# class TourTotalForm(forms.ModelForm):
#     description = forms.CharField(widget=CKEditorUploadingWidget)
#
#     class Meta:
#         model = ToursTotal
#         fields = '__all__'

admin_site = ToursAppAdmin('myqldl')

admin_site.register(User)
admin_site.register(ToursTotal, TourTotalAdmin)
admin_site.register(ToursDetail, TourDetailAdmin)
admin_site.register(Hotel)
admin_site.register(Tag)
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
