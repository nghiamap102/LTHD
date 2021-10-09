from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import *
from rest_framework import serializers


class TagSerializers(ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']


class UserSerializers(ModelSerializer):
    avatar = SerializerMethodField()
    user_type = serializers.SerializerMethodField('type')

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

    def get_avatar(self, cmt):
        avatar = cmt.avatar.name
        path = 'http://127.0.0.1:8000/%s' % avatar

        return path

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(user.password)
        user.save()

        return user

    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "username", "password", "phone", "address", "email", "is_superuser",
                  "is_staff", 'active_staff', 'birthdate',
                  "date_joined", 'avatar', 'user_type']

        extra_kwargs = {
            'password': {'write_only': 'true'}
        }


class TourTotalSerializers(ModelSerializer):
    tags = TagSerializers(many=True)

    class Meta:
        model = TourTotal
        fields = ['id', 'name', 'image', 'tags', 'content', 'created_date']

# class TourDetailSerializers(ModelSerializer):
#     image = SerializerMethodField()
#     image_detail = serializers.StringRelatedField(many=True)
#     rate = SerializerMethodField()
#
#     def get_rate(self, tour):
#         request = self.context.get("request")
#         if request and request.user.is_authenticated:
#             r = tour.rating_set.filter(creator=request.user).first()
#             if r:
#                 return r.rate
#         return -1
#
#     def get_image(self, course):
#         name = course.image.name
#         if name.startswith("static/"):
#             path = 'http://127.0.0.1:8000/%s' % name
#         return path
#
#     class Meta:
#         model = TourDetail
#         fields = ['id', 'name', 'image', 'created_date', 'price', 'status', 'time_start',
#                   'duration', 'content', 'tour', 'discount',
#                   'transport', 'image_detail', "rate", 'final_price']
#
#
# class CmtSerializers(ModelSerializer):
#     customer = SerializerMethodField()
#
#     def get_customer(self, cmt):
#         name = cmt.customer.username
#         id = cmt.customer.id
#         avatar = cmt.customer.avatar.name
#         avatar = 'http://127.0.0.1:8000/%s' % avatar
#         fname = cmt.customer.first_name
#         lname = cmt.customer.last_name
#         return id, name, avatar, fname, lname
#
#     class Meta:
#         model = Comment
#         fields = ["id", "content", "tour_detail", "customer", "created_date", "active"]
#
#
# class BookingSerializers(ModelSerializer):
#     customer = SerializerMethodField()
#
#     def get_customer(self, cmt):
#         name = cmt.customer.username
#         id = cmt.customer.id
#         avatar = cmt.customer.avatar.name
#         avatar = 'http://127.0.0.1:8000/%s' % avatar
#         fname = cmt.customer.first_name
#         lname = cmt.customer.last_name
#         return id, name, avatar, fname, lname
#
#     class Meta:
#         model = Booking
#         fields = ['id', 'tour_detail', 'customer', 'adult', 'children', 'room', 'room_price', 'status', 'total']
#
#
# # class BookingSerializers(ModelSerializer):
# #
# #     class Meta:
# #         model = Booking
# #         fields = ['id', 'customer', 'tour_detail', 'content']
#
# class Room_PriceSerializer(ModelSerializer):
#     class Meta:
#         model = Point
#         fields = ['id', 'tour_detail', 'price']
#
#
# class TourTesSerial(ModelSerializer):
#     class Meta:
#         model = TourDetail
#         fields = ['id', 'status']
#
#
# class PointSerializer(ModelSerializer):
#     class Meta:
#         model = Point
#         fields = ['id', 'customer', 'point']
#
#
# class RatingSerializer(ModelSerializer):
#     class Meta:
#         model = Rating
#         fields = ["id", "rate", "created_date"]
#
#
# class TourDetailViewSerializers(ModelSerializer):
#     class Meta:
#         model = TourDetailViews
#         fields = ["id", "views", "tour_detail"]
#
#
# class HotelSerializers(ModelSerializer):
#     class Meta:
#         model = Hotel
#         fields = ['id', 'name', 'address', 'phone', 'email']
#
#
# class TransportSerializers(ModelSerializer):
#     class Meta:
#         model = Transport
#         fields = ['id', 'name', 'active']
#
#


#

# class BlogSerializers(ModelSerializer):
#     class Meta:
#         model = Blog
#         fields = ['id', 'created_date', 'image', 'tags', 'active']
