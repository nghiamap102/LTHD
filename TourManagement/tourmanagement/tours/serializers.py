from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.db.models import Avg, Count
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import *
from rest_framework import serializers
from django import forms
import django.contrib.auth.password_validation as validators
from django.core.exceptions import ValidationError
from django.db.models import Q

class StaffSerializer(ModelSerializer):
    class Meta:
        model = Staff
        fields = ['user' , 'activeStaff']

class TagTourDetailSerializers(ModelSerializer):
    class Meta:
        model = TagTourDetail
        fields = ['id', 'name']


class TagBlogSerializers(ModelSerializer):
    class Meta:
        model = TagBlog
        fields = ['id', 'name']


class TagCountrySerializers(ModelSerializer):
    class Meta:
        model = TagCountry
        fields = ['id', 'name']


class TransportSerializers(ModelSerializer):
    class Meta:
        model = Transport
        fields = ['id', 'name']

#
# class UserSerializers(ModelSerializer):
#     def create(self, validated_data):
#         user = User(**validated_data)
#         user.set_password(user.password)
#         user.save()
#
#         return user
#
#     class Meta:
#         model = User
#         fields = ["id", "first_name", "last_name", "username", "password", "email", "date_joined"]
#
#         extra_kwargs = {
#             'password': {'write_only': 'true'}
#         }


class UserSerializers(ModelSerializer):
    user_type = serializers.SerializerMethodField('type')
    staff = StaffSerializer(read_only=True)

    # avatar = serializers.SerializerMethodField()
    #
    # def get_avatar(self, user):
    #     avatar = user.avatar
    #     path = 'http://127.0.0.1:8000/%s' % avatar
    #     return path

    def type(self, user):
        try:
            admin = user.is_superuser

            if admin:
                return "Admin"
            if user.staff.activeStaff :
                return "Staff"
            return "User"
        except:
            return "User"

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(user.password)
        user.save()

        return user



    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "username",'password', "phone", "address", "email", "is_superuser",
                  "is_staff", 'staff', 'birthdate', 'point',
                  "date_joined", 'avatar','avatar_url', 'user_type']

        extra_kwargs = {
            'password': {'write_only': 'true'}
        }


class LikeSerializer(ModelSerializer):
    # type = serializers.CharField(source='get_type_display')
    #
    # def get_type(self, like):
    #     a = like.type
    #     return a

    class Meta:
        model = Like
        fields = ["id", "type", "blog", "creator", "created_date"]


class LikeSerializer2(ModelSerializer):


    class Meta:
        model = Like
        fields = ["id","type", "created_date"]


class RatingSerializer(ModelSerializer):
    class Meta:
        model = Rating
        fields = ["id", "rate", 'creator', "created_date"]


class RatingSerializer2(ModelSerializer):
    class Meta:
        model = Rating
        fields = ["id", "rate", "created_date"]


class CmtBlogSerializers(ModelSerializer):
    customer = SerializerMethodField()

    def get_customer(self, cmt):
        name = cmt.customer.username
        id = cmt.customer.id
        avatar = cmt.customer.avatar.name
        avatar = 'http://127.0.0.1:8000/%s' % avatar
        fname = cmt.customer.first_name
        lname = cmt.customer.last_name

        return id, name, avatar, fname, lname

    class Meta:
        model = CommentBlog
        fields = ["id", "content", "blog", "customer", "created_date", "active"]


class ImgDetailSerializers(ModelSerializer):
    class Meta:
        model = ImgDetail
        fields = ['id', 'image']


class ImgDetailSerializers2(ModelSerializer):
    image2 = serializers.SerializerMethodField()

    def get_image2(self, img):
        name = img.image.name
        path = 'http://127.0.0.1:8000/%s' % name

        return path

    class Meta:
        model = ImgDetail
        fields = ['id', 'image2']


class BlogSerializers(ModelSerializer):
    count_like = serializers.SerializerMethodField()
    cmt_blog = serializers.SerializerMethodField()
    tag = TagBlogSerializers(many=True, read_only=True)
    img_detail = ImgDetailSerializers2(many=True, read_only=True)
    like = LikeSerializer(many=True, read_only=True)

    def get_cmt_blog(self, blog):
        avg = blog.cmt_blog.aggregate(Count('content'))
        return avg

    def get_count_like(self, blog):
        avg = blog.like.aggregate(Count('type'))
        return avg

    class Meta:
        model = Blog
        fields = ["id", "content", "name", "image", "created_date", 'like', 'count_like', 'cmt_blog', 'decription',
                  'tag', "img_detail"]


class BlogSerializers2(ModelSerializer):
    like = serializers.SerializerMethodField()
    cmt_blog = serializers.SerializerMethodField()
    tag = TagBlogSerializers(many=True, read_only=True)
    img_detail = ImgDetailSerializers2(many=True, read_only=True)
    image = serializers.SerializerMethodField()

    def get_image(self, tour):
        name = tour.image.name

        path = 'http://127.0.0.1:8000/%s' % name

        return path

    def get_cmt_blog(self, blog):
        avg = blog.cmt_blog.aggregate(Count('content'))
        return avg

    def get_like(self, blog):
        avg = blog.like.aggregate(Count('type'))
        return avg

    class Meta:
        model = Blog
        fields = ["id", "content", "name", "image", "created_date", 'like', 'cmt_blog', 'decription',
                  'tag', "img_detail"]


class HotelSerializers(ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['tour_detail', 'name', 'address', 'phone', 'email']


class ViewSerializers(ModelSerializer):
    class Meta:
        model = Views
        fields = ["id", "views", "created_date"]


class DepartureSerializers2(ModelSerializer):
    tag = TagCountrySerializers(many=True, read_only=True)
    image = serializers.SerializerMethodField()

    def get_image(self, tour):
        name = tour.image.name

        path = 'http://127.0.0.1:8000/%s' % name

        return path

    class Meta:
        model = Departure
        fields = ['id', 'name', 'image', 'content', "tag", 'created_date', "active"]


class CmtTourSerializers(ModelSerializer):
    customer = SerializerMethodField()

    def get_customer(self, cmt):
        name = cmt.customer.username
        id = cmt.customer.id
        avatar = cmt.customer.avatar.name
        avatar = 'http://127.0.0.1:8000/%s' % avatar
        fname = cmt.customer.first_name
        lname = cmt.customer.last_name

        return id, name, avatar, fname, lname

    class Meta:
        model = CommentTourDetail
        fields = ["id", "content", "tour_detail", "customer", "created_date", "active"]


class DepartureSerializers(ModelSerializer):
    tag = TagCountrySerializers(many=True, read_only=True)
    count = SerializerMethodField()

    def get_count(sel, tour):
        count = tour.detail.count()
        return count

    class Meta:
        model = Departure
        fields = ['id', 'name', 'image', 'content', "tag", 'created_date', "active", 'count']


class DestinationSerializers(ModelSerializer):
    tag = TagCountrySerializers(many=True, read_only=True)
    count = SerializerMethodField()

    def get_count(sel, tour):
        count = tour.detail.count()
        return count

    class Meta:
        model = Destination
        fields = ['id', 'name', 'image', 'content', "tag", 'created_date', "active", 'count']


class TourDetailSerializers(ModelSerializer):
    rate = SerializerMethodField()
    status = SerializerMethodField()
    transport = TransportSerializers(many=True, read_only=True)
    img_detail = ImgDetailSerializers(many=True, read_only=True)
    tag = TagTourDetailSerializers(many=True, read_only=True)

    def get_rate(self, tour):
        avg = tour.rating.aggregate(Avg('rate'))
        count_rate = tour.rating.aggregate(Count('rate'))
        star_1 = tour.rating.filter(rate=1).aggregate(star_1=Count('rate'))
        star_2 = tour.rating.filter(rate=2).aggregate(star_2=Count('rate'))
        star_3 = tour.rating.filter(rate=3).aggregate(star_3=Count('rate'))
        star_4 = tour.rating.filter(rate=4).aggregate(star_4=Count('rate'))
        star_5 = tour.rating.filter(rate=5).aggregate(star_5=Count('rate'))

        return avg, star_1, star_2, star_3, star_4, star_5, count_rate

    def get_status(self, detail):
        try:
            status = detail.slot
            if status <= 0:
                return "Out of Slot"
            return "Remaining"
        except:
            return "Remaining"

    class Meta:
        model = TourDetail
        fields = ['id', 'name', 'image', 'slot', 'time_start', 'duration', 'content', 'departure', 'destination',
                  'price_room',
                  'price_tour', 'total', 'discount', 'tag',
                  'transport', 'img_detail', 'status', 'transport', 'img_detail', 'rate', 'status']


class BookingSerializers(ModelSerializer):
    customer = SerializerMethodField()
    tour_detail = SerializerMethodField()
    tour_name = SerializerMethodField()
    status2 = serializers.CharField(source='get_status_display')

    def get_status2(self, booking):
        a = booking.status
        return a

    def get_tour_name(self, booking):
        name = booking.tour_detail.name
        return name

    def get_tour_detail(self, booking):
        id = booking.tour_detail.id
        return id

    def get_customer(self, cmt):
        name = cmt.customer.username
        id = cmt.customer.id
        avatar = cmt.customer.avatar.name
        avatar = 'http://127.0.0.1:8000/%s' % avatar
        fname = cmt.customer.first_name
        lname = cmt.customer.last_name
        return id, name, avatar, fname, lname

    class Meta:
        model = Booking
        fields = ['id', 'tour_detail', 'customer', 'adult', 'children', 'room',
                  'status', 'status2', 'total', 'created_date', 'tour_name']


class BookingSerializers2(ModelSerializer):

    def get_customer(self, cmt):
        name = cmt.customer.username
        id = cmt.customer.id
        avatar = cmt.customer.avatar.name
        avatar = 'http://127.0.0.1:8000/%s' % avatar
        fname = cmt.customer.first_name
        lname = cmt.customer.last_name
        return id, name, avatar, fname, lname

    class Meta:
        model = Booking
        fields = ['id', 'total', 'created_date']


class TourDetailSerializers2(ModelSerializer):
    rate = SerializerMethodField()
    status = SerializerMethodField()
    transport = TransportSerializers(many=True, read_only=True)
    img_detail = ImgDetailSerializers(many=True, read_only=True)
    image = serializers.SerializerMethodField()

    def get_image(self, detail):
        avatar = detail.image.name
        path = 'http://127.0.0.1:8000/%s' % avatar
        return path

    def get_status(self, detail):
        try:
            status = detail.slot
            if status <= 0:
                return "Out of Slot"
            return "Remaining"
        except:
            return "Remaining"

    def get_rate(self, tour):
        avg = tour.rating.aggregate(Avg('rate'))
        star_1 = tour.rating.filter(rate=1).aggregate(star_1=Count('rate'))
        star_2 = tour.rating.filter(rate=2).aggregate(star_2=Count('rate'))
        star_3 = tour.rating.filter(rate=3).aggregate(star_3=Count('rate'))
        star_4 = tour.rating.filter(rate=4).aggregate(star_4=Count('rate'))
        star_5 = tour.rating.filter(rate=5).aggregate(star_5=Count('rate'))

        return avg, star_1, star_2, star_3, star_4, star_5

    class Meta:
        model = TourDetail
        fields = ['id', 'name', 'image', 'slot', 'time_start', 'duration', 'content', 'departure', 'destination',
                  'price_room',
                  'price_tour', 'total', 'discount',
                  'transport', 'img_detail', 'status', 'transport', 'img_detail', 'rate', 'status', 'hotel']



