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


# generics.CreateAPIView,  # tao
# generics.RetrieveAPIView,generics.UpdateAPIView):  # lay thong tin

class UserViewSet(viewsets.ViewSet, generics.ListAPIView, generics.RetrieveAPIView, generics.CreateAPIView,
                  generics.UpdateAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializers
    parser_classes = [MultiPartParser]

    def get_permissions(self):
        if self.action in ['current_user', 'booking_detail', 'change_password']:
            return [permissions.IsAuthenticated()]

        return [permissions.AllowAny()]

    @action(methods=['get'], detail=False, url_path='current-user')
    def current_user(self, request):
        return Response(self.serializer_class(request.user).data)

    @action(methods=['get'], detail=False, url_path="booking_detail")
    def booking_detail(self, request):
        cmt = User.objects.get(pk=request.user.id).booking.all()

        return Response(BookingSerializers(cmt, many=True).data,
                        status=status.HTTP_200_OK)

    @action(methods=['post'], detail=False, url_path="update_booking")
    def update_booking(self, request):
        # cmt = User.objects.get(pk=request.user.id).booking.all()
        try:
            tour_detail = request.data['tour_detail']
            t = TourDetail.objects.get()
            ud = Booking.objects.get(customer=request.user.id,tour_detail= tour_detail)
            ud.status = "Booking accepted"
            ud.save()
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST, data="failed")
        return Response(BookingSerializers(ud).data, status=status.HTTP_200_OK)

    @action(methods=['post'], detail=False, url_path='change_password')
    def change_password(self, request):
        try:
            u = User.objects.get(pk=request.user.id)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST, data="Don't Get it!")
        try:
            u.password = request.data['current_password']
            try:
                u.set_password(request.data['password'])
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST, data="Don't have any data")
            try:
                u.save()
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST, data="Faild to save!")
            return Response(UserSerializers(u).data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST, data="Current Password incorrectly!")

    @action(methods=['post'] , detail=False , url_path="forgot_password")
    def forgot_password(self,request):
        try:
            phone = request.data['phone']
            username = request.data['username']
            current_password = request.data['current_password']
            new_password = request.data['new_password']
        except:
            return  Response(status=status.HTTP_400_BAD_REQUEST,data="Invalid")
        try:
            r = User.objects.get(username=username,password=current_password,phone=phone)
            try:
                r.set_password(new_password)
                r.save()
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST, data="Invalid")
        except:
            return  Response(status=status.HTTP_400_BAD_REQUEST,data="failed")



    # @action(methods=['get'],detail=True,url_path="point")
    # def get_point(self,pk):
    #     p = User.objects.get(pk=pk).point.all()
    #     return Response(BookingSerializers(cmt, many=True).data,
    #                     status=status.HTTP_200_OK)

    @action(methods='post', )
class ToursTotalPagination(PageNumberPagination):
    page_size = 6


class TourTotalViewSet(viewsets.ViewSet, generics.ListAPIView, generics.RetrieveAPIView):
    queryset = TourTotal.objects.all()
    serializer_class = TourTotalSerializers
    pagination_class = ToursTotalPagination

    def get_permissions(self):
        if self.action == 'add_tags':
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

    def get_queryset(self):
        courses = TourTotal.objects.filter(active=True)
        q = self.request.query_params.get("q")
        if q is not None:
            courses = courses.filter(name__contains=q)

        return courses

    @action(methods=['post'], detail=True, url_path="tags")  # add_tag
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

    @action(methods=['get'], detail=True, url_path='detail')  # detail
    def get_detail(self, request, pk):
        dt = TourTotal.objects.get(pk=pk).detail.filter(active=True)

        q = request.query_params.get('q')
        if q is not None:
            dt = dt.filter(name__icontains=q)

        return Response(TourDetailSerializers(dt, many=True).data,
                        status=status.HTTP_200_OK)

    # @action(methods='post' ,url_path="del_tour")
    # def del_tour(self,request):

class ToursDetailViewSet(viewsets.ModelViewSet, generics.RetrieveAPIView, generics.UpdateAPIView,
                         generics.CreateAPIView):
    queryset = TourDetail.objects.filter(active=True)
    serializer_class = TourDetailSerializers

    def get_permissions(self):
        if self.action in ['add-comment', 'like_action', 'rating_action', 'booking_action']:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

    # search
    def get_queryset(self):
        tour = TourDetail.objects.filter(active=True)
        kw = self.request.query_params.get('kw')
        if kw is not None:
            tour = tour.filter(name__contains=kw)

        tour_id = self.request.query_params.get('tour_id')
        if tour_id is not None:
            tour = tour.filter(name__contains=tour_id)

        return tour

    @action(methods=['get'], detail=True, url_path="comment")
    def get_cmt(self, request, pk):
        cmt = TourDetail.objects.get(pk=pk).comment.all()

        return Response(CmtSerializers(cmt, many=True).data,
                        status=status.HTTP_200_OK)

    @action(methods=['post'], detail=True, url_path='add-comment')
    def add_cmt(self, request, pk):
        content = request.data.get('content')
        if content:
            c = Comment.objects.create(content=content,
                                       tour_detail=self.get_object(),
                                       customer=request.user)
            return Response(CmtSerializers(c).data, status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['post'], detail=True, url_path='rating')
    def rating_action(self, request, pk):
        try:
            rating = int(request.data['rating'])
        except IndexError | ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            rate = Rating.objects.update_or_create(creator=request.user, tour=self.get_object(),
                                                   defaults={"rate": rating})

            return Response(RatingSerializer(rate).data, status=status.HTTP_200_OK)

    @action(methods=['post'], detail=True, url_path="booking")
    def booking_action(self, request, pk):
        try:
            content = request.data.get('content')
            children = int(request.data['children'])
            adult = int(request.data['adult'])
            room = int(request.data['room'])
            room_price = int(request.data['room_price'])
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST, data="invalid")
        try:
            c = Booking.objects.create(content=content,
                                       children=children,
                                       adult=adult,
                                       room=room,
                                       room_price=room_price,
                                       tour_detail=self.get_object(),
                                       customer=request.user)
            if c:
                sl = TourDetail.objects.get(pk=pk)
                stt = sl.status - adult
                sl.status = stt
                sl.save()
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST, data="Failed")
        return Response(BookingSerializers(c).data, status=status.HTTP_201_CREATED)

    # @action(methods=['post'],url_path="payment")

    @action(methods=['get'], detail=True, url_path='views')
    def inc_view(self, request, pk):
        v, created = TourDetailViews.objects.get_or_create(tourdetail=self.get_object())
        v.views = F('views') + 1
        v.save()

        v.refresh_from_db()
        return Response(TourDetailViewSerializers(v).data, status=status.HTTP_200_OK)

    # @action(methods='post' ,detail=True,url_path="del_detail")
    # def del_detail(self,reques):
    # @action(methods=['post'], detail=True, url_path='like')
    # def like_action(self, request, pk):
    #     try:
    #         action_type = request.data['type']
    #     except IndexError | ValueError:
    #         return Response(status=status.HTTP_400_BAD_REQUEST)
    #     else:
    #         action = Action.objects.create(type=action_type, creator=request.user, tour=self.get_object())
    #
    #         return Response(ActionSerializer(action).data, status=status.HTTP_200_OK)


class CmtViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.filter(active=True)
    serializer_class = CmtSerializers
    permissions = [permissions.IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        if request.user == self.get_object().customer:
            return super().destroy(request, *args, **kwargs)
        return Response(status=status.HTTP_403_FORBIDDEN)

    def partial_update(self, request, *args, **kwargs):
        if request.user == self.get_object().customer:
            return super().partial_update(request, *args, **kwargs)
        return Response(status=status.HTTP_403_FORBIDDEN)


class BookingDetailViewSet(viewsets.ViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializers
    permissions = [permissions.IsAuthenticated]

    # def destroy(self, request, *args, **kwargs):
    #     if request.user == self.get_object().customer:
    #         return super().destroy(request, *args, **kwargs)
    #     return Response(status=status.HTTP_403_FORBIDDEN)
    #
    # def partial_update(self, request, *args, **kwargs):
    #     if request.user == self.get_object().customer:
    #         return super().partial_update(request, *args, **kwargs)
    #     return Response(status=status.HTTP_403_FORBIDDEN)


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.filter(active=True)
    serializer_class = BlogSerializers


class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.filter(active=True)
    serializer_class = HotelSerializers


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializers


class AuthInfo(APIView):
    def get(self, request):
        return Response(settings.OAUTH2_INFO, status=status.HTTP_200_OK)
