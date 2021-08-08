from rest_framework.serializers import ModelSerializer
from .models import *


class UserSerializers(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'username', 'password', 'avatar']

    def create(self, validated_data):
        user = User(**validated_data)

        # user.first_name = validated_data['first_name'] **validated_data lo het
        # user.last_name  = validated_data['last_name']
        user.set_password(validated_data['password'])
        user.save()

        return user


class TagSerializers(ModelSerializer):
    class Meta:
        nodel = Tag
        fields = ['id', 'name']

class TourTotalSerializers(ModelSerializer):
    # tags = TagSerializers(many=True)

    class Meta:
        model = ToursTotal
        fields = ['id', 'name', 'count','imageTours']

class TourDetailSerializers(ModelSerializer):
    class Meta:
        model = ToursDetail
        fields = ['tourid', 'name', 'timestart', 'timefinish', 'price', 'vat']


class HotelSerializers(ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['id', 'name', 'address', 'phone', 'email', 'price']


class TransportSerializers(ModelSerializer):
    class Meta:
        model = Transport
        field = ['id', 'name', 'price']
# class NewsSerializers(ModelSerializer):
#     class Meta:
#         model = news
#         fỉelds = ['id', 'decription']
