from rest_framework.serializers import ModelSerializer,SerializerMethodField
from .models import *


class UserSerializers(ModelSerializer):
    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(user.password)
        user.save()

        return user

    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "username", "password", "email", "is_superuser", "is_staff",
                  "date_joined"]

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
        fields = ['id', 'name', 'image', 'tags']


class TourDetailSerializers(ModelSerializer):
    image = SerializerMethodField()

    def get_image(self, course):
        name = course.image.name
        if name.startswith("static/"):
            path = 'http://127.0.0.1:8000/%s' % name
        return path

    class Meta:
        model = ToursDetail
        fields = ['id', 'name','image', 'timestart', 'timefinish', 'price', 'vat', 'tours']


class CmtSerializers(ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "customer", "tourdetail", "created_date"]


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
