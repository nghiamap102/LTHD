from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.db.models import Avg, Count
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import *
from rest_framework import serializers
from django import forms
import django.contrib.auth.password_validation as validators
from django.core.exceptions import ValidationError


class TagSerializers(ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']


class TransportSerializers(ModelSerializer):
    class Meta:
        model = Transport
        fields = ['id', 'name']


class UserSerializers(ModelSerializer):
    user_type = serializers.SerializerMethodField('type')
    avatar = serializers.SerializerMethodField()

    def get_avatar(self, user):
        avatar = user.avatar
        path = 'http://127.0.0.1:8000/%s' % avatar
        return path

    def type(self, user):
        try:
            admin = user.is_superuser
            staff = user.active_staff
            if admin:
                return "Admin"
            if staff:
                return "Staff"
            return "User"
        except:
            return "User"

    def validate_password(self, data):
        errors = dict()
        try:
            validators.validate_password(password=data)
        except ValidationError as e:
            errors = list(e.messages)
        if errors:
            raise serializers.ValidationError(errors)
        return super(UserSerializers, self).validate(data)

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(user.password)
        user.save()

        return user

    def update(self, instance, validated_data):
        user = super().update(instance, validated_data)
        if 'password' in validated_data:
            user.set_password(validated_data['password'])
            user.save()
        return user

    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "username", "password", "phone", "address", "email", "is_superuser",
                  "is_staff", 'active_staff', 'birthdate', 'point',
                  "date_joined", 'avatar', 'user_type']

        extra_kwargs = {
            'password': {'read_only': 'true'}
        }


class LikeSerializer(ModelSerializer):
    # type = serializers.CharField(source='get_type_display')
    #
    # def get_type(self, like):
    #     a = like.type
    #     return a

    class Meta:
        model = Like
        fields = ["id", "type", "created_date"]


class LikeSerializer2(ModelSerializer):
    type = serializers.CharField(source='get_type_display')

    def get_type(self, like):
        a = like.type
        return a

    class Meta:
        model = Like
        fields = ["id", "type", "created_date"]


class RatingSerializer(ModelSerializer):
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


class BlogSerializers(ModelSerializer):
    like = serializers.SerializerMethodField()
    cmt_blog = serializers.SerializerMethodField()

    def get_cmt_blog(self, blog):
        avg = blog.cmt_blog.aggregate(Count('content'))
        return avg

    def get_like(self, blog):
        avg = blog.like.aggregate(Count('type'))
        return avg

    class Meta:
        model = Blog
        fields = ["id", "content", "name", "tour_detail", "image", "created_date", 'like', 'cmt_blog', 'decription']


class HotelSerializers(ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['tour_detail', 'name', 'address', 'phone', 'email']


class ImgDetailSerializers(ModelSerializer):
    class Meta:
        model = ImgDetail
        fields = ['id', 'image', 'tour_detail']





class TourTesSerial(ModelSerializer):
    class Meta:
        model = TourDetail
        fields = ['id', 'status']


class TourDetailViewSerializers(ModelSerializer):
    class Meta:
        model = TourDetailViews
        fields = ["id", "views", "tour_detail"]


class TourTotalSerializers2(ModelSerializer):
    tags = TagSerializers(many=True, read_only=True)

    image = serializers.SerializerMethodField()

    def get_image(self, tour):
        name = tour.image.name

        path = 'http://127.0.0.1:8000/%s' % name

        return path

    class Meta:
        model = TourTotal
        fields = ['id', 'name', 'image', 'content', "tags", 'created_date', "active"]


class TourTotalSerializers(ModelSerializer):
    tags = TagSerializers(many=True, read_only=True)

    class Meta:
        model = TourTotal
        fields = ['id', 'name', 'image', 'content', "tags", 'created_date', "active"]


class TourDetailSerializers(ModelSerializer):
    rate = SerializerMethodField()
    status = SerializerMethodField()
    transport = TransportSerializers(many=True, read_only=True)
    img_detail = ImgDetailSerializers(many=True, read_only=True)
    # image = serializers.SerializerMethodField()
    #
    # def get_image(self, detail):
    #     avatar = detail.image.name
    #     path = 'http://127.0.0.1:8000/%s' % avatar
    #     return path

    def get_rate(self, tour):
        avg = tour.rating.aggregate(Avg('rate'))

        return avg

    def get_status(self, detail):
        try:
            status = detail.slot
            if status <= 0:
                return "Out of"
            return "Remaining"
        except:
            return "Remaining"

    class Meta:
        model = TourDetail
        fields = ['id', 'name', 'image', 'slot', 'time_start', 'duration', 'content', 'tour',
                  'price_room', 'price_tour', 'total', 'discount',
                  'transport', 'img_detail', 'status', 'transport', 'img_detail', 'rate']


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

    def get_rate(self, tour):
        avg = tour.rating.aggregate(Avg('rate'))

        return avg

    def get_status(self, detail):
        try:
            status = detail.slot
            if status <= 0:
                return "Out of"
            return "Remaining"
        except:
            return "Remaining"

    class Meta:
        model = TourDetail
        fields = ['id', 'name', 'image', 'slot', 'time_start', 'duration', 'content', 'tour',
                  'price_room', 'price_tour', 'total', 'discount',
                  'transport', 'img_detail', 'status', 'transport', 'img_detail', 'rate']




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


class BookingSerializers(ModelSerializer):
    customer = SerializerMethodField()
    status = serializers.CharField(source="get_status_display")

    def get_status(self, booking):
        a = booking.status
        return a

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
        fields = ['id', 'tour_detail', 'customer', 'adult', 'children', 'room', 'status', 'total', 'created_date']
