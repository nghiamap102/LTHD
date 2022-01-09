from builtins import filter
from collections import deque
from operator import ge

from coreschema import Ref
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.sites.shortcuts import get_current_site
from django.template.defaulttags import url
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.utils import six
from rest_framework import generics, viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser, JSONParser
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework import filters
from django.conf import settings
from .models import *
from .serializers import *
from django.db.models import F
from .permission import *
from .paginator import *
from django.core.mail import send_mail
from django.contrib.auth import login, logout, authenticate
from datetime import date


class UserViewSet(viewsets.ViewSet, generics.ListAPIView, generics.RetrieveAPIView, generics.CreateAPIView,
                  generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializers
    parser_classes = [MultiPartParser, JSONParser]
    permission_classes = [UserPermission]

    def partial_update(self, request, *args, **kwargs):
        c = request.data['id']
        if c:
            if request.data['id'] == self.get_object().pk:
                try:
                    b = request.data
                    p = User.objects.update_or_create(pk=request.user.id, defaults={
                        'phone': b['phone'],
                        'address': b['address'],
                        'birthdate': b['birthdate'],
                        'avatar': b['avatar'],
                        'username': b['username'],
                        'password': make_password(b['password']),
                        # 'active_staff': b['active_staff']
                    })
                    a = User.objects.get(pk=request.user.id)
                    return Response(UserSerializers(a).data, status=status.HTTP_200_OK)
                except:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
            return super().partial_update(request, *args, **kwargs)
        return Response(status=status.HTTP_403_FORBIDDEN)
        # return Response(UserSerializers(a).data, status=status.HTTP_200_OK)

    @action(methods=['get'], detail=False, url_path="current_user")
    def current_user(self, request):
        return Response(self.serializer_class(request.user).data, status=status.HTTP_200_OK)

    @action(methods=['post'], detail=False, url_path='change_password')  ## xong 3 quyền
    def change_password(self, request):
        try:
            u = User.objects.get(pk=request.user.id)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST, data="Don't Get it!")
        try:
            if not check_password(request.data['current_password'], u.password):
                return Response(status=status.HTTP_400_BAD_REQUEST, data="incorrect current password")
            else:
                try:
                    u.set_password(request.data['new_password'])
                except:
                    return Response(status=status.HTTP_400_BAD_REQUEST, data="Don't have any data")
                try:
                    u.save()
                except:
                    return Response(status=status.HTTP_400_BAD_REQUEST, data="Failed to save!")
                return Response(status=status.HTTP_200_OK, data=UserSerializers(u, context={'request': request}).data)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST, data="Current Password incorrectly!")

    @action(methods=['post'], detail=False, url_path='forgot_password')  ## xong
    def forgot_password(self, request):
        try:

            username = request.data['username']
            phone = request.data['phone']
            new_password = request.data['new_password']
            confirm_password = request.data['confirm_password']
            if new_password == confirm_password:
                r = User.objects.get(username=username, phone=phone)
                try:
                    r.set_password(new_password)
                    r.save()
                    return Response(UserSerializers(r).data, status=status.HTTP_200_OK)
                except:
                    return Response(status=status.HTTP_400_BAD_REQUEST, data="Dont save")
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST, data="Invalid")
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST, data="Invalid")

    @action(methods=['post'], detail=False, url_path='inactive_user')  ## xong
    def inactive_user(self, request):
        try:
            t = User.objects.get(pk=request.user.id)
            t.is_active = False
            t.save()
            return Response(data=UserSerializers(t, context={'request': request}).data, status=status.HTTP_200_OK)

        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=False, url_path="booking_detail")  ##Xong
    def booking_detail(self, request):
        b = User.objects.get(pk=request.user.id).booking.all()

        return Response(BookingSerializers(b, many=True).data,
                        status=status.HTTP_200_OK)

    @action(methods=['post'], detail=False, url_path="update_booking")
    def update_booking(self, request):
        try:
            tour_detail = request.data['tour_detail']
            ud = Booking.objects.get(customer=request.user, tour_detail=tour_detail, status="p")
            sl = TourDetail.objects.get(pk=tour_detail)

            ud.status = "a"
            ud.save()

            try:
                if sl.slot >= 0:
                    sl.slot = sl.slot - ud.adult - ud.children
                    sl.save()
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST, data="Failed_stt")
            try:
                u = User.objects.get(pk=request.user.id)

                u.point = u.point + ud.total / 1000
                u.save()
                return Response(UserSerializers(u).data, status=status.HTTP_200_OK)
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST, data="point_failed")
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST, data="failed")

    @action(methods=['post'], detail=False, url_path="cancel_booking")
    def del_booking(self, request):
        # cmt = User.objects.get(pk=request.user.id).booking.all()
        try:
            tour_detail = request.data['tour_detail']
            ud = Booking.objects.get(customer=request.user.id, tour_detail=self.get_object())
            if ud.created_date.date + 3:
                ud.status = "Booking canceled"
                ud.save()
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST, data="failed")
        return Response(BookingSerializers(ud).data, status=status.HTTP_200_OK)

    @action(methods=['post'], detail=False, url_path="check_exist")
    def check_exist(self, request):
        a = request.data['username']
        u = User.objects.get(username=a)
        return Response(UserSerializers(u).data, status=status.HTTP_200_OK)

    @action(methods=['post'], detail=False, url_path="send_mail")
    def send_mail(self, request):
        mail_to = request.data['mail_to']
        send_mail('Test', 'abc', settings.EMAIL_HOST_USER, [mail_to],
                  fail_silently=False)
        return Response(status=status.HTTP_200_OK)

    @action(methods=['post'], detail=False, url_path="send_mail_all")
    def send_mail_all(self, request):
        mail_to = request.data['mail_to']
        send_mail('Test', 'abc', settings.EMAIL_HOST_USER, [mail_to],
                  fail_silently=False)
        return Response(status=status.HTTP_200_OK)


class DepartureViewSet(viewsets.ViewSet, generics.ListAPIView, generics.CreateAPIView, generics.RetrieveAPIView,
                       generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Departure.objects.filter(active=True)
    serializer_class = DepartureSerializers
    parser_classes = [JSONParser, MultiPartParser]
    permission_classes = [TourToTalPermission]
    pagination_class = ToursTotalPagination

    # tạo, sửa , xóa xong

    def create(self, request, *args, **kwargs):
        try:
            b = request.data
            if b:
                try:
                    a = Departure.objects.create(
                        name=b['name'],
                        content=b['content'],
                        image=b['image'],
                    )

                    return Response(DepartureSerializers2(a).data, status=status.HTTP_200_OK)
                except:
                    return Response(status=status.HTTP_400_BAD_REQUEST, data="create_failed")
            return super().create(request, *args, **kwargs)
        except:
            return Response(status=status.HTTP_403_FORBIDDEN)

    def get_queryset(self):
        a = Departure.objects.filter(active=True)
        try:

            q = self.request.query_params.get("q")
            tag = self.request.query_params.get("tag")
            try:
                if q is not None:
                    a = a.filter(name__icontains=q)
                if tag is not None:
                    a = a.filter(tag__name__icontains=tag)
                return a
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST, data="search_failed")
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST, data="invalid")

    @action(methods=['post'], detail=True, url_path="add_tag")  # add_tag
    def add_tag(self, request, pk):
        try:
            tour = self.get_object()
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            tag = request.data["tag"]
            t, _ = TagCountry.objects.get_or_create(name=tag)
            tour.tag.add(t)

            tour.save()

            return Response(DepartureSerializers(tour).data, status=status.HTTP_201_CREATED)

    @action(methods=['post'], detail=True, url_path="update_tag")  # add_tag
    def update_tag(self, request, pk):
        try:
            tour = self.get_object()
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        try:
            try:
                tag = request.data["tag1"]
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST, data="invalid")
            try:
                t1, _ = TagCountry.objects.get_or_create(name=tag)
                tour.tag.set([t1])
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST, data="failed_update")

            tour.save()

            return Response(DepartureSerializers(tour).data, status=status.HTTP_201_CREATED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST, data="failed_")

    @action(methods=['get'], detail=True, url_path='list_detail')  # detail
    def list_detail(self, request, pk):
        try:
            dt = Departure.objects.get(pk=pk).detail.filter(active=True)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST, data="get_fail")
        try:
            name = request.query_params.get('name')
            price = request.query_params.get('price')
            time = request.query_params.get('time')
            discount = request.query_params.get('discount')
            duration_to = request.query_params.get('duration_to')
            duration_from = request.query_params.get('duration_from')
            time_from = request.query_params.get('time_from')
            departure = request.query_params.get('departure')
            destination = request.query_params.get('destination')
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST, data="invalid")
        try:
            if name is not None:
                dt = dt.filter(name__icontains=name)
            if price is not None:
                dt = dt.filter(price_tour__lt=price)
            if time is not None:
                dt = dt.filter(time_start__icontains=time)
            if discount is not None:
                dt = dt.filter(discount__gt=discount)
            if duration_from and duration_to is not None:
                dt = dt.filter(duration__range=[duration_from, duration_to])
            if duration_from is not None:
                dt = dt.filter(duration__gte=duration_from)
            if time_from is not None:
                dt = dt.filter(time_start__gte=time_from)
            if departure is not None:
                dt = dt.filter(departure=departure)
            if destination is not None:
                dt = dt.filter(destination=destination)
            return Response(TourDetailSerializers2(dt, many=True).data,
                            status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST, data="search_fail")


class DestinationViewSet(viewsets.ViewSet, generics.ListAPIView, generics.CreateAPIView, generics.RetrieveAPIView,
                         generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Destination.objects.filter(active=True)
    serializer_class = DestinationSerializers
    parser_classes = [JSONParser, MultiPartParser]
    pagination_class = ToursTotalPagination


class ToursDetailViewSet(viewsets.ModelViewSet, generics.RetrieveAPIView, generics.UpdateAPIView,
                         generics.CreateAPIView, generics.ListAPIView):
    queryset = TourDetail.objects.filter(active=True)
    serializer_class = TourDetailSerializers
    permission_classes = [TourDetailPermission]
    parser_classes = [MultiPartParser, JSONParser]
    pagination_class = TourDetailPagination

    def partial_update(self, request, *args, **kwargs):
        c = request.data['id']
        if c:
            if request.data['id'] == self.get_object().pk:
                try:
                    b = request.data
                    p = TourDetail.objects.update_or_create(pk=c, defaults={
                        "departure": b["departure"],
                        "name": b["name"],
                        "time_start": b["time_start"],
                        "duration": b["duration"],
                        "price_room": b["price_room"],
                        "price_tour": b["price_tour"],
                        "discount": b["discount"],
                        "total": int(b["price_room"] - b["discount"] / 100 * b["price_tour"]),
                        "image": b["image"],
                    })
                    a = TourDetail.objects.get(pk=request.data['id'])
                    return Response(TourDetailSerializers(a).data, status=status.HTTP_200_OK)
                except:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
            return super().partial_update(request, *args, **kwargs)
        return Response(status=status.HTTP_403_FORBIDDEN)

    def get_queryset(self):  # search
        a = TourDetail.objects.filter(active=True)
        try:

            name = self.request.query_params.get("name")
            total = self.request.query_params.get("total")
            time_to = self.request.query_params.get("time_to")
            time_from = self.request.query_params.get("time_from")
            price = self.request.query_params.get("price")
            duration_from = self.request.query_params.get("duration_from")
            duration_to = self.request.query_params.get("duration_to")
            discount = self.request.query_params.get("discount")
            slot = self.request.query_params.get("slot")
            transport = self.request.query_params.get("transport")
            departure = self.request.query_params.get('departure')
            destination = self.request.query_params.get('destination')
            tag = self.request.query_params.get('tag')
            try:
                if name is not None:
                    a = a.filter(name__icontains=name)
                if total is not None:
                    a = a.filter(total__lte=total)
                if time_to and time_from is not None:
                    a = a.filter(time_start__range=[time_from, time_to])
                if time_from is not None and time_to is None:
                    a = a.filter(time_start__gte=time_from)
                if time_to is not None and time_from is None:
                    a = a.filter(time_start__lte=time_to)
                if price is not None:
                    a = a.filter(total__lte=price)
                if duration_from and duration_to is not None:
                    a = a.filter(duration__range=[duration_from, duration_to])
                if duration_from is not None and duration_to is None:
                    a = a.filter(duration__gte=duration_from)
                if duration_to is not None and duration_from is None:
                    a = a.filter(duration__gte=duration_to)
                if discount is not None:
                    a = a.filter(discount__gte=discount)
                if slot is not None:
                    a = a.filter(slot__gte=slot)
                if transport is not None:
                    a = a.filter(transport__name__icontains=transport)
                if departure is not None:
                    a = a.filter(departure=departure)
                if destination is not None:
                    a = a.filter(destination=destination)
                if tag is not None:
                    a = a.filter(tag__name__icontains=tag)
                return a
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST, data="search_failed")
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST, data="invalid")

    @action(methods=['get'], detail=True, url_path="comment")  # xong
    def get_cmt(self, request, pk):
        cmt = TourDetail.objects.get(pk=pk).cmt_tour.all()

        return Response(CmtTourSerializers(cmt, many=True).data,
                        status=status.HTTP_200_OK)

    @action(methods=['post'], detail=True, url_path="update_transport")  # add_tag
    def update_tag(self, request, pk):
        try:
            tour = self.get_object()
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        try:

            try:
                transport1 = request.data["transport1"]
                transport2 = request.data["transport2"]
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST, data="invalid")
            try:
                t1, _ = Transport.objects.get_or_create(name=transport1)
                t2, _ = Transport.objects.get_or_create(name=transport2)
                tour.transport.set([t1, t2])
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST, data="failed_update")

            tour.save()

            return Response(TourDetailSerializers(tour).data, status=status.HTTP_201_CREATED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST, data="failed_")

    @action(methods=['post'], detail=True, url_path="add_img_detail")  # xong
    def add_img_detail(self, request, pk):
        try:
            tour = self.get_object()
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        try:

            try:
                img_detail1 = request.data["img_detail1"]
                img_detail2 = request.data["img_detail2"]
                img_detail3 = request.data["img_detail3"]
                img_detail4 = request.data["img_detail4"]
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST, data="invalid")
            try:
                t1, _ = ImgDetail.objects.get_or_create(image=img_detail1)
                t2, _ = ImgDetail.objects.get_or_create(image=img_detail2)
                t3, _ = ImgDetail.objects.get_or_create(image=img_detail3)
                t4, _ = ImgDetail.objects.get_or_create(image=img_detail4)
                tour.img_detail.set([t1, t2, ])
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST, data="failed_update")

            tour.save()

            return Response(TourDetailSerializers(tour).data, status=status.HTTP_201_CREATED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST, data="failed_")

    @action(methods=['post'], detail=True, url_path="add_hotel")  # xong
    def add_hotel(self, request, pk):
        try:
            name = request.data['name']
            image = request.data['image']
            address = request.data['address']
            phone = request.data['phone']
            email = request.data['email']

            try:
                t = Hotel.objects.get_or_create(name=name,
                                                tour_detail=self.get_object(),
                                                image=image,
                                                address=address,
                                                phone=phone,
                                                email=email
                                                )
                return Response(HotelSerializers(t).data, status=status.HTTP_200_OK)
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST, data="failed")
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST, data="invalid")

    @action(methods=['post'], detail=True, url_path='add_comment')  # xong
    def add_comment(self, request, pk):
        content = request.data.get('content')
        if content:
            c = CommentTourDetail.objects.create(content=content,
                                                 tour_detail=self.get_object(),
                                                 customer=request.user)
            return Response(CmtTourSerializers(c).data, status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['post'], detail=True, url_path='add_rating')  # xong
    def add_rating(self, request, pk):
        try:
            rating = int(request.data['rating'])
        except IndexError | ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST, data="invalid")
        else:
            rate = Rating.objects.update_or_create(creator=request.user, tour=self.get_object(),
                                                   defaults={"rate": rating})

            return Response(RatingSerializer2(rate).data, status=status.HTTP_200_OK)

    @action(methods=['post'], detail=True, url_path="get_rating")  # xong
    def get_rating(self, request, pk):
        id = request.data['id']
        cmt = TourDetail.objects.get(pk=pk).rating.filter(creator=id)

        return Response(RatingSerializer(cmt, many=True).data,
                        status=status.HTTP_200_OK)

    @action(methods=['post'], detail=True, url_path="add_booking")
    def add_booking(self, request, pk):
        try:
            children = int(request.data['children'])
            adult = int(request.data['adult'])
            room = int(request.data['room'])
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST, data="invalid")
        try:
            sl = TourDetail.objects.get(pk=pk)
            total = int((children * sl.total) * 50 / 100
                        + adult * sl.total
                        + room * sl.price_room)
            if sl.slot <= 0:
                return Response(status=status.HTTP_400_BAD_REQUEST, data="out of stt")
            else:
                try:
                    c = Booking.objects.create(
                        tour_detail=self.get_object(),
                        children=children,
                        adult=adult,
                        room=room,
                        total=total,
                        customer=request.user)
                    return Response(BookingSerializers(c).data, status=status.HTTP_200_OK)
                except:
                    return Response(status=status.HTTP_400_BAD_REQUEST, data="Failed_add")
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST, data="Failed")

    @action(methods=['get'], detail=True, url_path="update_booking")
    def update_booking(self, request, pk):
        try:
            ud = Booking.objects.get(customer=request.user, tour_detail=self.get_object(), status="p")
            sl = TourDetail.objects.get(pk=pk)

            ud.status = "a"
            ud.save()

            try:
                if sl.slot > 0:
                    sl.slot = sl.slot - ud.adult - ud.children
                    sl.save()
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST, data="Failed_stt")
            try:
                u = User.objects.get(pk=request.user.id)

                u.point = u.point + ud.total / 1000
                u.save()

                message = "Thank " + u.first_name + " " + u.last_name + " to booking at them with " + str(
                    ud.total) + "VND"

                send_mail('Test', message, settings.EMAIL_HOST_USER, [u.email],
                          fail_silently=False)
                return Response(UserSerializers(u).data, status=status.HTTP_200_OK)
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST, data="point_failed")
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST, data="failed")

    @action(methods=['post'], detail=True, url_path='cancel_booking')
    def cancel_booking(self, request, pk):
        try:
            ud = Booking.objects.get(customer=request.user, tour_detail=self.get_object())
            ud.status = "c"
            ud.save()
            return Response(BookingSerializers(ud).data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST, data="failed")


class CmtTourViewSet(viewsets.ViewSet, generics.RetrieveAPIView, generics.CreateAPIView, generics.UpdateAPIView,
                     generics.DestroyAPIView, generics.ListAPIView):
    queryset = CommentTourDetail.objects.filter(active=True)
    serializer_class = CmtTourSerializers
    permission_classes = [CmtPermission]
    parser_classes = [MultiPartParser, JSONParser]

    def destroy(self, request, *args, **kwargs):
        if request.user == self.get_object().customer:
            return super().destroy(request, *args, **kwargs)
        return Response(status=status.HTTP_403_FORBIDDEN)

    def partial_update(self, request, *args, **kwargs):
        if request.user == self.get_object().customer:
            return super().partial_update(request, *args, **kwargs)
        return Response(status=status.HTTP_403_FORBIDDEN)


class CmtBlogViewSet(viewsets.ViewSet, generics.RetrieveAPIView, generics.CreateAPIView, generics.UpdateAPIView,
                     generics.DestroyAPIView, generics.ListAPIView):
    queryset = CommentBlog.objects.filter(active=True)
    serializer_class = CmtBlogSerializers
    permission_classes = [CmtPermission]
    parser_classes = [MultiPartParser, JSONParser]

    def destroy(self, request, *args, **kwargs):
        if request.user == self.get_object().customer:
            return super().destroy(request, *args, **kwargs)
        return Response(status=status.HTTP_403_FORBIDDEN)

    def partial_update(self, request, *args, **kwargs):
        if request.user == self.get_object().customer:
            return super().partial_update(request, *args, **kwargs)
        return Response(status=status.HTTP_403_FORBIDDEN)


class BlogViewSet(viewsets.ViewSet, generics.RetrieveAPIView, generics.CreateAPIView,
                  generics.UpdateAPIView, generics.DestroyAPIView, generics.ListAPIView):
    # xong thêm sửa xóa
    queryset = Blog.objects.filter(active=True)
    serializer_class = BlogSerializers
    # permission_classes = [BlogPermission]
    parser_classes = [MultiPartParser, JSONParser]
    pagination_class = BlogPagination

    @action(methods=['post'], detail=False, url_path='send_mail')
    def send_mail(self, request, pk):

        email = request.data['email']
        phone = request.data['phone']
        content = request.data['content']

        msg = 'from' + email + 'phone' + phone + content

        send_mail('Request', msg, email, [settings.EMAIL_HOST_USER],
                  fail_silently=False)
        return Response(status=status.HTTP_200_OK, data="success")

    def get_queryset(self):  # search
        a = Blog.objects.filter(active=True)
        try:
            name = self.request.query_params.get("name")
            created_date = self.request.query_params.get("created_date")
            tag = self.request.query_params.get("tag")
            try:
                if name is not None:
                    a = a.filter(name__icontains=name)
                if created_date is not None:
                    a = a.filter(created_date=created_date)
                if tag is not None:
                    a = a.filter(tag__name__icontains=tag)

                return a
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST, data="search_failed")
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST, data="invalid")

    @action(methods=['post'], detail=True, url_path='like')  # xong hiện count
    def like_action(self, request, pk):
        try:
            action_type = request.data['type']
        except IndexError | ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            action = Like.objects.update_or_create(creator=request.user, blog=self.get_object()
                                                   , defaults={'type': action_type})

            return Response(LikeSerializer2(action).data, status=status.HTTP_200_OK)

    @action(methods=['get'], detail=True, url_path="comment")  # xong
    def get_cmt(self, request, pk):
        cmt = Blog.objects.get(pk=pk).cmt_blog.all()

        return Response(CmtBlogSerializers(cmt, many=True).data,
                        status=status.HTTP_200_OK)

    @action(methods=['get'], detail=True, url_path="get_like")  # xong
    def get_like(self, request, pk):
        print(request.user)
        cmt = Blog.objects.get(pk=pk).like.filter(creator=request.user.id)

        return Response(LikeSerializer(cmt, many=True).data,
                        status=status.HTTP_200_OK)

    @action(methods=['post'], detail=True, url_path='add_comment')  # xong
    def add_comment(self, request, pk):
        try:
            content = request.data.get('content')
            try:
                if content:
                    c = CommentBlog.objects.create(content=content,
                                                   blog=self.get_object(),
                                                   customer=request.user)
                    return Response(CmtBlogSerializers(c).data, status=status.HTTP_201_CREATED)
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST, data="failed")
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST, data="invalid")

    @action(methods=['post'], detail=True, url_path="update_tag")
    def update_tag(self, request, pk):
        try:
            blog = self.get_object()
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        try:
            try:
                tag = request.data["tag"]
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST, data="invalid")
            try:
                t1, _ = TagBlog.objects.get_or_create(name=tag)
                blog.tag.set([t1])
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST, data="failed_update")

            blog.save()

            return Response(BlogSerializers(blog).data, status=status.HTTP_201_CREATED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST, data="failed_")

    @action(methods=['post'], detail=True, url_path="add_img_detail")  # xong
    def add_img_detail(self, request, pk):
        try:
            blog = self.get_object()
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        else:
            img_detail = request.data["img_detail"]
            t, _ = ImgDetail.objects.get_or_create(image=img_detail)
            blog.img_detail.add(t)

            blog.save()

            return Response(BlogSerializers2(blog).data, status=status.HTTP_201_CREATED)


class HotelViewSet(viewsets.ViewSet, generics.CreateAPIView, generics.RetrieveAPIView,
                   generics.DestroyAPIView, generics.UpdateAPIView, generics.ListAPIView):
    # thêm sửa xóa xong
    queryset = Hotel.objects.filter(active=True)
    serializer_class = HotelSerializers
    parser_classes = [MultiPartParser, JSONParser]
    # permission_classes = [HotelPermission]


class TagBlogViewSet(viewsets.ViewSet, generics.ListAPIView, generics.CreateAPIView, generics.RetrieveAPIView,
                     generics.DestroyAPIView, generics.UpdateAPIView):
    queryset = TagBlog.objects.all()
    serializer_class = TagBlogSerializers
    parser_classes = [MultiPartParser, JSONParser]


class TagCountryViewSet(viewsets.ViewSet, generics.ListAPIView, generics.CreateAPIView, generics.RetrieveAPIView,
                        generics.DestroyAPIView, generics.UpdateAPIView):
    queryset = TagCountry.objects.all()
    serializer_class = TagCountrySerializers
    parser_classes = [MultiPartParser, JSONParser]


class TagTourDetailViewSet(viewsets.ViewSet, generics.ListAPIView, generics.CreateAPIView, generics.RetrieveAPIView,
                           generics.DestroyAPIView, generics.UpdateAPIView):
    queryset = TagTourDetail.objects.all()
    serializer_class = TagTourDetailSerializers
    parser_classes = [MultiPartParser, JSONParser]


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializers
    permissions = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, JSONParser]

    @action(methods=['post'], detail=False, url_path='static')
    def static(self, request):
        try:
            date = request.data['date']
            b = Booking.objects.filter(status="a", created_date__icontains=date)
            return Response(BookingSerializers(b, many=True).data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST, data='failed')

    @action(methods=['post'], detail=False, url_path='static_quy')
    def static_quy(self, request):
        try:
            date = request.data['date']
            date2 = request.data['date2']
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST, data='invalid')
        try:
            b = Booking.objects.filter(status="a", created_date__range=[date, date2])
            # dt = dt.filter(duration__range=[duration_from, duration_to])

            return Response(BookingSerializers(b, many=True).data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST, data='failed')


class ImgDetailViewSet(viewsets.ViewSet, generics.ListAPIView, generics.CreateAPIView
    , generics.UpdateAPIView):
    queryset = ImgDetail.objects.all()
    serializer_class = ImgDetailSerializers
    permission_classes = [ImgDetailPermission]


class RatingViewSet(viewsets.ViewSet, generics.ListAPIView, generics.CreateAPIView
    , generics.UpdateAPIView, generics.DestroyAPIView, generics.RetrieveAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


class LikeViewSet(viewsets.ViewSet, generics.ListAPIView, generics.CreateAPIView, generics.RetrieveAPIView
    , generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer


class TransportViewSet(viewsets.ModelViewSet):
    queryset = Transport.objects.all()
    serializer_class = TransportSerializers


class IncViewsViewSet(viewsets.ModelViewSet):
    queryset = Views.objects.all()
    serializer_class = ViewSerializers

    @action(methods=['post'], detail=False, url_path='get_view')
    def get_view(self, request):
        d = request.data['date']
        v = Views.objects.get(created_date__icontains=d)
        return Response(ViewSerializers(v).data, status=status.HTTP_200_OK)

    @action(methods=['get'], detail=False, url_path='inc_view')
    def inc_view(self, request):
        d = date.today()
        v, created = Views.objects.get_or_create(created_date=d)
        v.views = F('views') + 1
        v.save()

        v.refresh_from_db()
        return Response(ViewSerializers(v).data, status=status.HTTP_200_OK)


class AuthInfo(APIView):
    def get(self, request):
        return Response(settings.OAUTH2_INFO, status=status.HTTP_200_OK)


class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
                six.text_type(user.pk) + six.text_type(timestamp) +
                six.text_type(user.is_active)
        )


account_activation_token = TokenGenerator()


class VerifyEmail(viewsets.ModelViewSet):

    def signup(request):
        if request.method == 'POST':
            email = request.data['email']
            if User.objects.filter(email=email).count() == 1:
                user = User.objects.get(email=email)
                current_site = get_current_site(request)
                mail_subject = 'Activate your account.'
                message = render_to_string('email_template.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
                })
                send_mail(mail_subject, message, settings.EMAIL_HOST_USER, [user.email])
            return Response(status=status.HTTP_200_OK)

    # def activate(request, uidb64, token):
    #     User = get_user_model()
    #     try:
    #         uid = force_text(urlsafe_base64_decode(uidb64))
    #         user = User.objects.get(pk=uid)
    #     except(TypeError, ValueError, OverflowError, User.DoesNotExist):
    #         user = None
    #     if user is not None and account_activation_token.check_token(user, token):
    #         user.is_active = True
    #         user.save()
    #         return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    #     else:
    #         return HttpResponse('Activation link is invalid!')
