from operator import ge
from django.contrib.auth.hashers import make_password, check_password
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


class UserViewSet(viewsets.ViewSet, generics.ListAPIView, generics.RetrieveAPIView, generics.CreateAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializers
    parser_classes = [MultiPartParser]
    permission_classes = [UserPermission]

    ## register user,staff k cần đăng nhập
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

    @action(methods=['post'], detail=False, url_path="forgot_password")  ##xong
    def forgot_password(self, request):
        try:
            phone = request.data['phone']
            username = request.data['username']
            new_password = request.data['new_password']
            confirm_password = request.data['confirm_password']
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST, data="Invalid")
        try:
            r = User.objects.get(username=username, phone=phone)
            if r:
                if new_password == confirm_password:
                    try:
                        r.set_password(new_password)
                        r.save()
                        return Response(data=UserSerializers(r, context={'request': request}).data,
                                        status=status.HTTP_400_BAD_REQUEST)
                    except:
                        return Response(status=status.HTTP_400_BAD_REQUEST, data="Dont save")
            return Response(status=status.HTTP_400_BAD_REQUEST, data="confirm and password incorrect")

        except:
            return Response(status=status.HTTP_400_BAD_REQUEST, data="failed")

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

    # @action(methods=['post'], detail=False, url_path="register_staff")  ## xong
    # def register_user(self, request):
    #     try:
    #         username = request.data['username']
    #         password = make_password(request.data['password'])
    #         is_staff = request.data['is_staff']
    #         is_superuser = request.data['is_superuser']
    #     except:
    #         return Response(status=status.HTTP_400_BAD_REQUEST, data="invalid")
    #
    #     try:
    #         u = User.objects.create(username=username,
    #                                 password=password,
    #                                 is_staff=is_staff,
    #                                 is_superuser=is_superuser)
    #         return Response(data=UserSerializers(u, context={'request': request}).data, status=status.HTTP_201_CREATED)
    #     except:
    #         return Response(status=status.HTTP_400_BAD_REQUEST, data="Create_failed")

    @action(methods=['post'], detail=False, url_path="update_info_user")  ## Cập nhật csdl nhưng vẫn bị catch lỗi
    def update_info_user(self, request):
        # try:
        #     phone =
        #     address =
        #     birthdate =
        #     avatar =
        #     # active_staff = request.data['active_staff']
        # except:
        #     return Response(status=status.HTTP_400_BAD_REQUEST, data="invalid")

        # try:
        data = request.data
        p = User.objects.update_or_create(pk=request.user.id, defaults={
            'phone': data['phone'],
            'address': data['address'],
            'birthdate': data['birthdate'],
            'avatar': data['avatar'],
            # 'username': data['username'],
            # 'password': make_password(data['password']),
            # 'active_staff':active_staff
        })
        a = User.objects.get(pk=request.user.id)
        return Response(UserSerializers(a).data, status=status.HTTP_200_OK)
        # except:
        #     return Response(status=status.HTTP_400_BAD_REQUEST, data="Create_failed")

    @action(methods=['post'], detail=False, url_path="update_info_staff")  ## Cập nhật csdl nhưng vẫn bị catch lỗi
    def update_info_staff(self, request):
        try:
            b = request.data
            p = User.objects.update_or_create(pk=request.user.id, defaults={
                'phone': b['phone'],
                'address': b['address'],
                'birthdate': b['birthdate'],
                'avatar': b['avatar'],
                'username': b['username'],
                'password': make_password(b['password']),
                'active_staff': b['birthdate']
            })
            a = User.objects.get(pk=request.user.id)
            return Response(UserSerializers(a).data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST, data="Create_failed")



    # @action(methods=['get'], detail=False, url_path="point")  # xong lấy điểm theo nv
    # def get_point(self, request):
    #     try:
    #         p = Point.objects.get(customer=request.user.id)
    #     except:
    #         return Response(status=status.HTTP_400_BAD_REQUEST, data="Failed to get point")
    #     return Response(PointSerializer(p).data,
    #                     status=status.HTTP_200_OK)

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

class ToursTotalPagination(PageNumberPagination):
    page_size = 20


class TourTotalViewSet(viewsets.ViewSet, generics.ListAPIView, generics.CreateAPIView, generics.RetrieveAPIView,
                       generics.UpdateAPIView):

    queryset = TourTotal.objects.filter(active=True)
    serializer_class = TourTotalSerializers
    parser_classes = [MultiPartParser]
    permission_classes = [TourToTalPermission]

    # post tạo tourtal xog

    def get_queryset(self):
        courses = TourTotal.objects.filter(active=True)
        q = self.request.query_params.get("q")
        if q is not None:
            courses = courses.filter(name__contains=q)

        return courses

    @action(methods=['post'], detail=True, url_path="add_tag")  # add_tag
    def add_tags(self, request):
        try:
            tour = self.get_object()
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            tags = request.data.get("tags")
            if tags is not None:
                for tag in tags:
                    t, _ = Tag.objects.get_or_create(name=tag)
                    tour.tags.add(t)

                tour.save()

                return Response(TourTotalSerializers(tour).data, status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_404_NOT_FOUND)

    # @action(methods=['get'], detail=True, url_path='get_detail')  # detail
    # def get_detail(self, request, pk):
    #     dt = TourTotal.objects.get(pk=pk).detail.filter(active=True)
    #
    #     q = request.query_params.get('q')
    #     if q is not None:
    #         dt = dt.filter(name__icontains=q)
    #
    #     return Response(TourDetailSerializers(dt, many=True).data,
    #                     status=status.HTTP_200_OK)

# class ToursDetailViewSet(viewsets.ModelViewSet, generics.RetrieveAPIView, generics.UpdateAPIView,
#                          generics.CreateAPIView, generics.ListAPIView):
#     queryset = TourDetail.objects.filter(active=True)
#     serializer_class = TourDetailSerializers
#
#     def get_permissions(self):
#         if self.action in ['add-comment', 'like_action', 'rating_action', 'booking_action']:
#             return [permissions.IsAuthenticated()]
#         return [permissions.AllowAny()]
#
#     # search
#     def get_queryset(self):
#         tour = TourDetail.objects.filter(active=True)
#         kw = self.request.query_params.get('kw')
#         if kw is not None:
#             tour = tour.filter(name__contains=kw)
#
#         tour_id = self.request.query_params.get('tour_id')
#         if tour_id is not None:
#             tour = tour.filter(name__contains=tour_id)
#
#         return tour
#
#     @action(methods=['get'], detail=True, url_path="comment")
#     def get_cmt(self, request, pk):
#         cmt = TourDetail.objects.get(pk=pk).comment.all()
#
#         return Response(CmtSerializers(cmt, many=True).data,
#                         status=status.HTTP_200_OK)
#
#     @action(methods=['post'], detail=True, url_path='add-comment')
#     def add_cmt(self, request, pk):
#         content = request.data.get('content')
#         if content:
#             c = Comment.objects.create(content=content,
#                                        tour_detail=self.get_object(),
#                                        customer=request.user)
#             return Response(CmtSerializers(c).data, status=status.HTTP_201_CREATED)
#
#         return Response(status=status.HTTP_400_BAD_REQUEST)
#
#     @action(methods=['post'], detail=True, url_path='rating')
#     def rating_action(self, request, pk):
#         try:
#             rating = int(request.data['rating'])
#         except IndexError | ValueError:
#             return Response(status=status.HTTP_400_BAD_REQUEST)
#         else:
#             rate = Rating.objects.update_or_create(creator=request.user, tour=self.get_object(),
#                                                    defaults={"rate": rating})
#
#             return Response(RatingSerializer(rate).data, status=status.HTTP_200_OK)
#
#     @action(methods=['post'], detail=True, url_path="booking")
#     def booking_action(self, request, pk):
#         try:
#             content = request.data.get('content')
#             children = int(request.data['children'])
#             adult = int(request.data['adult'])
#             room = int(request.data['room'])
#             room_price = int(request.data['room_price'])
#         except:
#             return Response(status=status.HTTP_400_BAD_REQUEST, data="invalid")
#         try:
#             sl = TourDetail.objects.get(pk=pk)
#             # if sl:
#             #     r = Room_price.objects.all()
#             #     return Response(Room_PriceSerializer(r).data, status=status.HTTP_200_OK)
#             try:
#                 if sl.status <= 0:
#                     return Response(status=status.HTTP_400_BAD_REQUEST, data="out of stt")
#                 else:
#                     c = Booking.objects.create(content=content,
#                                                tour_detail=self.get_object(),
#                                                children=children,
#                                                adult=adult,
#                                                room=room,
#                                                room_price=room_price,
#                                                customer=request.user)
#                     if c:
#                         if sl:
#                             p = Point.objects.get(customer=request.use.id)
#                             obj = Booking.objects.get(customer=request.user.id)
#
#                             p.point = p.point + obj.total / 1000
#                             point = int(request.data['point'])
#
#                             p = Point.objects.update_or_create(customer=request.user, defaults={
#                                 'point': point
#                             })
#                             return Response(PointSerializer(p, many=True).data, status=status.HTTP_200_OK)
#
#                         try:
#                             try:
#                                 if sl.status != 0:
#                                     stt = sl.status - adult
#                                     sl.status = stt
#                                     sl.save()
#                                     # return Response(TourDetailSerializers(sl).data,status=status.HTTP_200_OK)
#                             except:
#                                 return Response(status=status.HTTP_400_BAD_REQUEST, data="Failed_stt")
#                             try:
#                                 if sl:
#                                     p = Point.objects.all()
#                                     # p.point = c.total / 1000
#                                     # p.save()
#                             except:
#                                 return Response(PointSerializer(p).data, status=status.HTTP_400_BAD_REQUEST)
#                         except:
#                             return Response(status=status.HTTP_400_BAD_REQUEST, data="Failed_point_stt")
#             except:
#                 return Response(status=status.HTTP_400_BAD_REQUEST, data="Failed_booking")
#         except:
#             return Response(status=status.HTTP_400_BAD_REQUEST, data="Failed")
#         return Response(BookingSerializers(c).data, status=status.HTTP_201_CREATED)
#
#     @action(methods=['post'], detail=True, url_path="update_booking")
#     def update_booking(self, request):
#         try:
#             tour_detail = request.data['tour_detail']
#             t = TourDetail.objects.get()
#             ud = Booking.objects.get(customer=request.user.id, tour_detail=self.get_object())
#             ud.status = "Booking accepted"
#             ud.save()
#         except:
#             return Response(status=status.HTTP_400_BAD_REQUEST, data="failed")
#         return Response(BookingSerializers(ud).data, status=status.HTTP_200_OK)
#
#     @action(methods=['get'], detail=True, url_path='views')
#     def inc_view(self, request, pk):
#         v, created = TourDetailViews.objects.get_or_create(tourdetail=self.get_object())
#         v.views = F('views') + 1
#         v.save()
#
#         v.refresh_from_db()
#         return Response(TourDetailViewSerializers(v).data, status=status.HTTP_200_OK)
#
#     # @action(methods=['post'], detail=True, url_path='like')
#     # def like_action(self, request, pk):
#     #     try:
#     #         action_type = request.data['type']
#     #     except IndexError | ValueError:
#     #         return Response(status=status.HTTP_400_BAD_REQUEST)
#     #     else:
#     #         action = Action.objects.create(type=action_type, creator=request.user, tour=self.get_object())
#     #
#     #         return Response(ActionSerializer(action).data, status=status.HTTP_200_OK)
#
#
# class CmtViewSet(viewsets.ModelViewSet):
#     queryset = Comment.objects.filter(active=True)
#     serializer_class = CmtSerializers
#     permissions = [permissions.IsAuthenticated]
#
#     def destroy(self, request, *args, **kwargs):
#         if request.user == self.get_object().customer:
#             return super().destroy(request, *args, **kwargs)
#         return Response(status=status.HTTP_403_FORBIDDEN)
#
#     def partial_update(self, request, *args, **kwargs):
#         if request.user == self.get_object().customer:
#             return super().partial_update(request, *args, **kwargs)
#         return Response(status=status.HTTP_403_FORBIDDEN)
#
#
# class BookingDetailViewSet(viewsets.ViewSet):
#     queryset = Booking.objects.all()
#     serializer_class = BookingSerializers
#     permissions = [permissions.IsAuthenticated]
#
#
# class BlogViewSet(viewsets.ModelViewSet):
#     queryset = Blog.objects.filter(active=True)
#     serializer_class = BlogSerializers
#
#
# class HotelViewSet(viewsets.ModelViewSet):
#     queryset = Hotel.objects.filter(active=True)
#     serializer_class = HotelSerializers
#
#
# class TagViewSet(viewsets.ModelViewSet):
#     queryset = Tag.objects.all()
#     serializer_class = TagSerializers
#
#
# class AuthInfo(APIView):
#     def get(self, request):
#         return Response(settings.OAUTH2_INFO, status=status.HTTP_200_OK)
