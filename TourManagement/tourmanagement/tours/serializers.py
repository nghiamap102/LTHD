from rest_framework.serializers import ModelSerializer,SerializerMethodField
from .models import *
from rest_framework import serializers


class UserSerializers(ModelSerializer):
    avatar = SerializerMethodField()

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
        fields = ["id", "first_name", "last_name", "username", "password", "email", "is_superuser", "is_staff",
                  "date_joined",'avatar']

        extra_kwargs = {
            'password': {'write_only': 'true'}
        }


class TagSerializers(ModelSerializer):
    class Meta:
        nodel = Tag
        fields = ['id', 'name']


class TourTotalSerializers(ModelSerializer):
    # tags = TagSerializers(many=True)

    class Meta:
        model = ToursTotal
        fields = ['id', 'name', 'image', 'tags','created_date']


class TourDetailSerializers(ModelSerializer):
    image = SerializerMethodField()
    imagedetail = serializers.StringRelatedField(many=True)

    def get_image(self, course):
        name = course.image.name
        if name.startswith("static/"):
            path = 'http://127.0.0.1:8000/%s' % name
        return path

    class Meta:
        model = ToursDetail
        fields = ['id', 'name','image', 'timestart', 'timefinish', 'price','decription', 'vat', 'tours','imagedetail','hotel']



class CmtSerializers(ModelSerializer):
    customer = SerializerMethodField()

    def get_customer(self,cmt):
        name = cmt.customer.username
        id = cmt.customer.id
        avatar = cmt.customer.avatar.name
        avatar = 'http://127.0.0.1:8000/%s' % avatar
        fname = cmt.customer.first_name
        lname = cmt.customer.last_name
        return id , name , avatar,fname,lname
    class Meta:
        model = Comment
        fields = ["id","content", "customer", "tourdetail", "created_date"]


class ActionSerializer(ModelSerializer):
    class Meta:
        model = Action
        fields = ["id", "type", "created_date"]


class RatingSerializer(ModelSerializer):
    class Meta:
        model = Rating
        fields = ["id", "rate", "created_date"]


class TourDetailViewSerializers(ModelSerializer):
    class Meta:
        model = TourDetailViews
        fields = ["id", "views", "tourdetail"]


class HotelSerializers(ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['id', 'name', 'address', 'phone', 'email', 'price']


class TransportSerializers(ModelSerializer):
    class Meta:
        model = Transport
        fields = ['id', 'name', 'price']



# class NewsSerializers(ModelSerializer):
#     class Meta:
#         model = news
#         fỉelds = ['id', 'name' , 'created_date' , 'content','imageNews']
