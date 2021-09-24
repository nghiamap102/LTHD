from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .models import *
from .serializers import *
from django.db.models import F


# generics.CreateAPIView,  # tao
# generics.RetrieveAPIView,generics.UpdateAPIView):  # lay thong tin

class UserViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializers
    parser_classes = [MultiPartParser]

    def get_permissions(self):
        if self.action == 'current_user':
            return [permissions.IsAuthenticated()]

        return [permissions.AllowAny()]

    @action(methods=['get'], detail=False, url_path='current-user')
    def current_user(self, request):
        return Response(self.serializer_class(request.user).data)


class ToursTotalPagination(PageNumberPagination):
    page_size = 9


class TourTotalViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = ToursTotal.objects.all()
    serializer_class = TourTotalSerializers

    def get_permissions(self):
        if self.action == 'add_tags':
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

    def get_queryset(self):
        courses = ToursTotal.objects.filter(active=True)
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

    @action(methods=['get'], detail=True, url_path='details')  # detail
    def get_details(self, request, pk):
        details = ToursTotal.objects.get(pk=pk).details.filter(active=True)
        # lessons = self.get_object().lessons.filter(active=True)

        q = request.query_params.get('q')
        if q is not None:
            details = details.filter(name__icontains=q)

        # tours_id = self.request.query_params.get("tours_id")  # tìm theo khóa ngoại
        # if tours_id is not None:
        #     details = details.filter(tours_id=tours_id)

        return Response(TourDetailSerializers(details, many=True).data,
                        status=status.HTTP_200_OK)


class ToursDetailViewSet(viewsets.ModelViewSet, generics.RetrieveAPIView):
    queryset = ToursDetail.objects.filter(active=True)
    serializer_class = TourDetailSerializers

    def get_permissions(self):
        if self.action in ['add_cmt', 'like_action', 'rating_action']:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

    # search
    def get_queryset(self):
        tour = ToursDetail.objects.filter(active=True)
        kw = self.request.query_params.get('kw')
        if kw is not None:
            tour = tour.filter(name__contains=kw)

        tour_id = self.request.query_params.get('tour_id')
        if tour_id is not None:
            tour = tour.filter(name__contains=tour_id)

        return tour

    @action(methods=['post'], detail=True, url_path='add-cmt')
    def add_cmt(self, request, pk):
        content = request.data.get('content')
        if content:
            c = Comment.objects.create(cmt=content,
                                       tourdetail=self.get_object(),
                                       customer=request.user)
            return Response(CmtSerializers(c).data, status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['post'], detail=True, url_path='like')
    def like_action(self, request, pk):
        try:
            action_type = request.data['type']
        except IndexError | ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            action = Action.objects.create(type=action_type, creator=request.user, tour=self.get_object())

            return Response(ActionSerializer(action).data, status=status.HTTP_200_OK)

    @action(methods=['post'], detail=True, url_path='rating')
    def rating_action(self, request,pk):
        try:
            value = request.data['value']
        except IndexError | ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            rate = Rating.objects.create(rate=value, tour=self.get_object(), creator=request.user)
        return Response(RatingSerializer(rate).data, status=status.HTTP_200_OK)

    @action(methods=['get'], detail=True, url_path='views')
    def inc_view(self, request,pk):
        v, created = TourDetailViews.objects.get_or_create(tourdetail=self.get_object())
        v.views = F('views') + 1
        v.save()

        v.refresh_from_db()
        return Response(TourDetailViewSerializers(v).data, status=status.HTTP_200_OK)


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


class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.filter(active=True)
    serializer_class = HotelSerializers


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializers
