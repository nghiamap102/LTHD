from operator import ge
from django.contrib.auth.hashers import make_password, check_password
from django.template.defaulttags import url
from rest_framework import generics, viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser, JSONParser
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from django.conf import settings
from .models import *
from .serializers import *
from django.db.models import F
from .permission import *
from .paginator import *


class UserViewSet(viewsets.ViewSet, generics.ListAPIView, generics.RetrieveAPIView, generics.CreateAPIView,
                  generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializers
    parser_classes = [MultiPartParser]
    permission_classes = [UserPermission]

    def partial_update(self, request, *args, **kwargs):
        c = request.data['id']
        if c:
            print(c)
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

    @action(methods=['get'], detail=False, url_path='current_user')  ## xong
    def current_user(self, request):
        return Response(self.serializer_class(request.user).data)

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

    @action(methods=['post'], detail=False, url_path='del_user')  ##xong xóa nhân viên
    def del_user(self, request):
        try:
            t = User.objects.get(pk=request.data['user_id'])
            t.delete()
            return Response(data=UserSerializers(t, context={'request': request}).data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['post'], detail=False, url_path="update_info")  ## Cập nhật csdl nhưng vẫn bị catch lỗi
    def update_info(self, request):
        try:
            b = request.data
            p = User.objects.update_or_create(pk=request.user.id, defaults={
                'phone': b['phone'],
                'address': b['address'],
                'birthdate': b['birthdate'],
                'avatar': b['avatar'],
                'email': b['email'],
                'last_name': b['last_name'],
                # 'active_staff': b['active_staff']
            })
            a = User.objects.get(pk=request.user.id)
            return Response(UserSerializers(a).data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST, data="Create_failed")

    @action(methods=['post'], detail=False, url_path='change-password')
    def change_password(self, request):
        try:
            try:
                u = User.objects.get(pk=request.user.id)
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST, data="user not found")
            try:
                u.set_password(request.data['password'])
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST, data="failed")
            try:
                u.save()
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST, data="save!")
            return Response(status=status.HTTP_200_OK, data="Change password success!")
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST, data="Failed!")

    # @action(methods=['get'], detail=False, url_path="booking_detail")  ##Xong
    # def booking_detail(self, request):
    #     b = User.objects.get(pk=request.user.id).booking.all()
    #
    #     return Response(BookingSerializers(b, many=True).data,
    #                     status=status.HTTP_200_OK)
    #
    # @action(methods=['post'], detail=False, url_path="update_booking")
    # def update_booking(self, request):
    #     # try:
    #     #     tour_detail = request.data['tour_detail']
    #     # try:
    #     t = TourDetail.objects.get().booking.all()
    #     return Response(BookingSerializers(t).data, status=status.HTTP_200_OK)

    #     ud = Booking.objects.get(customer=request.user.id, tour_detail=tour_detail)
    #     ud.status = "Booking accepted"
    #     ud.save()
    # except:
    #     return Response(status=status.HTTP_400_BAD_REQUEST, data="failed")
    # return Response(BookingSerializers(ud).data, status=status.HTTP_200_OK)

    # @action(methods=['post'], detail=False, url_path="cancel_booking")
    # def del_booking(self, request):
    #     # cmt = User.objects.get(pk=request.user.id).booking.all()
    #     try:
    #         tour_detail = request.data['tour_detail']
    #         ud = Booking.objects.get(customer=request.user.id, tour_detail=self.get_object())
    #         if ud.created_date.date  + 3
    #             ud.status = "Booking canceled"
    #             ud.save()
    #     except:
    #         return Response(status=status.HTTP_400_BAD_REQUEST, data="failed")
    #     return Response(BookingSerializers(ud).data, status=status.HTTP_200_OK)


class TourTotalViewSet(viewsets.ViewSet, generics.ListAPIView, generics.CreateAPIView, generics.RetrieveAPIView,
                       generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = TourTotal.objects.filter(active=True)
    serializer_class = TourTotalSerializers
    parser_classes = [JSONParser, MultiPartParser]
    permission_classes = [TourToTalPermission]
    pagination_class = ToursTotalPagination

    # tạo, sửa , xóa xong

    def create(self, request, *args, **kwargs):
        try:
            b = request.data
            if b:
                try:
                    a = TourTotal.objects.create(
                        name=b['name'],
                        content=b['content'],
                        image=b['image'],
                    )
                    tags = request.data["tags"]
                    if tags is not None:
                        t, _ = Tag.objects.get_or_create(name=tags)
                        a.tags.add(t)

                        a.save()
                    # b = TourTotalSerializers.objects.get(name=b['name'],
                    #                                      content=b['content'],
                    #                                      image=b['image'],
                    #
                    #                                      )
                    return Response(TourTotalSerializers2(a).data, status=status.HTTP_200_OK)
                except:
                    return Response(status=status.HTTP_400_BAD_REQUEST, data="create_failed")
            return super().create(request, *args, **kwargs)
        except:
            return Response(status=status.HTTP_403_FORBIDDEN)

    def get_queryset(self):
        courses = TourTotal.objects.filter(active=True)
        q = self.request.query_params.get("q")
        if q is not None:
            courses = courses.filter(name__contains=q)

        return courses

    @action(methods=['post'], detail=True, url_path="add_tag")  # add_tag
    def add_tag(self, request, pk):
        try:
            tour = self.get_object()
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            tags = request.data["tags"]
            if tags is not None:
                for tag in tags:
                    t, _ = Tag.objects.get_or_create(name=tag)
                    tour.tags.add(t)

                tour.save()

                return Response(TourTotalSerializers(tour).data, status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_404_NOT_FOUND)

    @action(methods=['get'], detail=True, url_path='list_detail')  # detail
    def list_detail(self, request, pk):
        dt = TourTotal.objects.get(pk=pk).detail.filter(active=True)

        # name = request.query_params.get('name')
        # price = request.query_params.get('price')
        # time = request.query_params.get('time')
        # status = request.query_params.get('status')

        # if name is not None:
        #     dt = dt.filter(name__icontains=name)
        # if price is not None:
        #     dt = dt.filter(tags__icontains=price)
        # if time is not None:
        #     dt = dt.filter(name__icontains=time)
        # if status is not None:
        #     dt = dt.filter(name__icontains=status)
        return Response(TourDetailSerializers2(dt, many=True).data,
                        status=status.HTTP_200_OK)

    @action(methods=['post'], detail=True, url_path="add_tour_detail")
    def add_tour_detail(self, request, pk):
        try:
            data = request.data
            price_tour = int(data['price_tour'])
            discount = int(data['discount'])
            duration = int(data['duration'])
            price_room = int(data['price_room'])
            name = data['name']
            image = data['image']
            time_start = data['time_start']
            total = int(price_tour - discount / 100 * price_tour)
            try:
                dt = TourDetail.objects.create(
                    tour=self.get_object(),
                    name=name,
                    time_start=time_start,
                    duration=duration,
                    price_room=price_room,
                    price_tour=price_tour,
                    discount=discount,
                    total=total,
                    image=image,
                )
                # transport = data['transport']
                # if transport is not None:
                #     for i in transport:
                #         t, _ = Transport.objects.get_or_create(name=i)
                #         dt.transport.add(t)
                #
                #     dt.save()
                return Response(TourDetailSerializers2(dt).data, status=status.HTTP_200_OK)
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST, data="add_fail")
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST, data="invalid")


class ToursDetailViewSet(viewsets.ModelViewSet, generics.RetrieveAPIView, generics.UpdateAPIView,
                         generics.CreateAPIView, generics.ListAPIView):
    queryset = TourDetail.objects.filter(active=True)
    serializer_class = TourDetailSerializers
    permission_classes = [TourDetailPermission]
    parser_classes = [MultiPartParser, JSONParser]

    # Thêm sửa xóa detail xog
    # Thêm sửa xóa cmt trong tour và cmtviewset xog


    # def retrieve(self, request, *args, **kwargs):
    #     c = request.data['id']
    #     a = TourTotal.objects.get(pk =c)
    #     return Response(TourDetailSerializers2())

    def partial_update(self, request, *args, **kwargs):
        c = request.data['id']
        if c:
            if request.data['id'] == self.get_object().pk:
                try:
                    b = request.data
                    p = TourDetail.objects.update_or_create(pk=c, defaults={
                        "tour": b["tour"],
                        "name": b["name"],
                        "time_start": b["time_start"],
                        "duration": b["duration"],
                        "price_room": b["price_room"],
                        "price_tour": b["price_tour"],
                        "discount": b["discount"],
                        "total": int(b["price_room"] - b["discount"] / 100 * b["price_tour"]),
                        "image": b["image"],
                    })
                    print(b['image'])
                    a = TourDetail.objects.get(pk=request.data['id'])
                    return Response(TourDetailSerializers(a).data, status=status.HTTP_200_OK)
                except:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
            return super().partial_update(request, *args, **kwargs)
        return Response(status=status.HTTP_403_FORBIDDEN)

    def get_queryset(self):  # search
        tour = TourDetail.objects.filter(active=True)
        kw = self.request.query_params.get('kw')
        if kw is not None:
            tour = tour.filter(name__contains=kw)

        tour_id = self.request.query_params.get('tour_id')
        if tour_id is not None:
            tour = tour.filter(name__contains=tour_id)

        return tour

    @action(methods=['get'], detail=True, url_path="comment")  # xong
    def get_cmt(self, request, pk):
        cmt = TourDetail.objects.get(pk=pk).cmt_tour.all()

        return Response(CmtTourSerializers(cmt, many=True).data,
                        status=status.HTTP_200_OK)

    @action(methods=['post'], detail=True, url_path="add_transport")  # xong
    def add_transport(self, request, pk):
        try:
            tour = self.get_object()
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            transport = request.data["transport"]
            if transport is not None:
                for i in transport:
                    t, _ = Transport.objects.get_or_create(name=i)
                    tour.transport.add(t)

                tour.save()

                return Response(TourDetailSerializers(tour).data, status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_404_NOT_FOUND)

    @action(methods=['post'], detail=True, url_path="add_img_detail")  # xong
    def add_img_detail(self, request, pk):
        try:
            image = request.FILES['image']
            try:
                for a in image:
                    t, _ = ImgDetail.objects.get_or_create(tour_detail=self.get_object(), image=image)

                return Response(status=status.HTTP_200_OK, data="success")
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST, data='add_failed')
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

            return Response(RatingSerializer(rate).data, status=status.HTTP_200_OK)

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
                    return  Response(BookingSerializers(c).data,status=status.HTTP_200_OK)
                except:
                    return Response(status=status.HTTP_400_BAD_REQUEST, data="Failed_add")
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST, data="Failed")

    @action(methods=['get'], detail=True, url_path="update_booking")
    def update_booking(self, request, pk):
        try:
            ud = Booking.objects.get(customer=request.user,tour_detail = self.get_object())
            sl = TourDetail.objects.get(pk=pk)

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

    @action(methods=['post'],detail=True,url_path='cancel_booking')
    def cancel_booking(self,request,pk):
        try:
            ud = Booking.objects.get(customer=request.user,tour_detail = self.get_object())
            ud.status = "c"
            ud.save()
            return Response(BookingSerializers(ud).data,status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST, data="failed")


    @action(methods=['get'], detail=True, url_path='views')
    def inc_view(self, request, pk):
        v, created = TourDetailViews.objects.get_or_create(tourdetail=self.get_object())
        v.views = F('views') + 1
        v.save()

        v.refresh_from_db()
        return Response(TourDetailViewSerializers(v).data, status=status.HTTP_200_OK)


class CmtTourViewSet(viewsets.ViewSet, generics.RetrieveAPIView, generics.CreateAPIView, generics.UpdateAPIView,
                     generics.DestroyAPIView):
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
                     generics.DestroyAPIView):
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

    @action(methods=['post'], detail=True, url_path='like')  # xong hiện count
    def like_action(self, request, pk):
        try:
            action_type = request.data['type']
        except IndexError | ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            action = Like.objects.update_or_create(creator=request.user, blog=self.get_object()
                                                   , defaults={'type': action_type})

            return Response(LikeSerializer(action).data, status=status.HTTP_200_OK)

    @action(methods=['get'], detail=True, url_path="comment")  # xong
    def get_cmt(self, request, pk):
        cmt = Blog.objects.get(pk=pk).cmt_blog.all()

        return Response(CmtBlogSerializers(cmt, many=True).data,
                        status=status.HTTP_200_OK)

    @action(methods=['get'], detail=True, url_path="get_like")  # xong
    def get_like(self, request, pk):
        cmt = Blog.objects.get(pk=pk).like.all()

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


class HotelViewSet(viewsets.ViewSet, generics.CreateAPIView, generics.RetrieveAPIView,
                   generics.DestroyAPIView, generics.UpdateAPIView, generics.ListAPIView):
    # thêm sửa xóa xong
    queryset = Hotel.objects.filter(active=True)
    serializer_class = HotelSerializers
    parser_classes = [MultiPartParser, JSONParser]
    permission_classes = [HotelPermission]


class TagViewSet(viewsets.ViewSet, generics.ListAPIView, generics.CreateAPIView, generics.RetrieveAPIView,
                 generics.DestroyAPIView, generics.UpdateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializers
    parser_classes = [MultiPartParser, JSONParser]


class BookingDetailViewSet(viewsets.ViewSet,generics.ListAPIView, generics.RetrieveAPIView, generics.DestroyAPIView, generics.UpdateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializers
    permissions = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, JSONParser]



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


class StaticViewSet(viewsets.ViewSet, generics.ListAPIView, generics.CreateAPIView, generics.RetrieveAPIView
    , generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Booking.objects.filter(status="a")
    serializer_class = BookingSerializers
    # permission_classes = []


class AuthInfo(APIView):
    def get(self, request):
        return Response(settings.OAUTH2_INFO, status=status.HTTP_200_OK)
