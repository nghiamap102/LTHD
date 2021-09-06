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


# generics.CreateAPIView,  # tao
# generics.RetrieveAPIView,generics.UpdateAPIView):  # lay thong tin
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializers
#     parser_classes = [MultiPartParser, ]
#     # swagger_schema = None
#
#     def get_permissions(self):
#         if self.action == 'current_user':
#             return [permissions.IsAuthenticated()]
#
#         return [permissions.AllowAny()]
#
#     @action(methods=['get'], detail=False, url_path='current-user')
#     def current_user(self, request):
#         return Response(self.serializer_class(request.user).data)


    # def get_permissions(self):
    #     if self.action == 'list':
    #         return [permissions.AllowAny()]
    #     return [permissions.IsAuthenticated()]


class UserViewSet(viewsets.ViewSet,
                  generics.CreateAPIView,
                  generics.ListAPIView,  # tao
                  generics.RetrieveAPIView):  # lay thong tin
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



# class NewsViesSet(viewsets.ModelViewSet):
#     queryset = News.objects.filter(active=True)
#     serializer_class = NewsSerializers

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializers

    def get_permissions(self):
        if self.action == 'list':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

class ToursTotalPagination(PageNumberPagination):
    page_size = 9


class ToursTotalViewSet(viewsets.ModelViewSet):
    queryset = ToursTotal.objects.filter(active=True)
    serializer_class = TourTotalSerializers
    pagination_class = ToursTotalPagination
    # permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        operation_description='Add tags to a lesson',
        responses={
            status.HTTP_200_OK: TourTotalSerializers()
        }
    )
    @action(methods=['post'], detail=True, url_path="hide-lesson", url_name="hide-lesson")
    def hide_lesson(self, request, pk):
        try:
            l = ToursTotal.objects.get(pk=pk)
            l.active = False
            l.save()
        except ToursTotal.DoesNotExits:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(TourTotalSerializers(l, context={'request': request}).data,
                        status=status.HTTP_200_OK)

    # def get_permissions(self):
    #     if self.action == 'list':
    #         return [permissions.AllowAny()]
    #     return [permissions.IsAuthenticated()]


class ToursDetailViewSet(viewsets.ModelViewSet):
    queryset = ToursDetail.objects.filter(active=True)
    serializer_class = TourDetailSerializers

    # def get_permissions(self):
    #     if self.action == 'list':
    #         return [permissions.AllowAny()]
    #     return [permissions.IsAuthenticated()]


class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.filter(active=True)
    serializer_class = HotelSerializers

    def get_permissions(self):
        if self.action == 'list':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]


# # class Feedback(viewsets.ModelViewSet):
# #     queryset = Comment.objects.all()
# #     serializer_class = CmtSerializers
# #
# #     def get_permissions(self):
# #         if self.action == 'list':
# #             return [permissions.AllowAny()]
# #         return [permissions.IsAuthenticated()]
# #
#
# def index(request):
#     search = request.GET.get('kw')
#
#     # detail = ToursDetail.objects.filter(active=True)
#
#     destination = ToursTotal.objects.filter(active=True, name__icontains='D')
#     fill = ToursDetail.objects.filter(name__icontains='DL')
#     count_tour = fill.count()
#     # hotel = Hotel.objects.filter(actice =True)
#     # blog = Blog.objects.filter(active= True)
#     # cmt = cmt.objects.filter(active=True)
#     # tags = Tag.objects.filter()
#
#     context = {
#         'destination': destination,
#         'count_tour': count_tour
#     }
#
#     return render(request, template_name='index.html', context=context)
#
#
# def tourdetail(request):
#     # tourdetail = ToursDetail.objects.filter(active= True)
#     # search
#     # register
#     # cmt
#
#     return render(request, template_name='detail-tour-dl.html')
#
#
# def contact(request):
#     return render(request, template_name='contact.html')
#
#
# def list_tour(request):
#     # tour_id  =ToursDetail.objects.filter(pk=tourid)
#     # page_number =
#     # kw = request.GET.get('kw')
#     # tag = ToursTotal.objects.filter(tag__name__contain ='kw')
#     # name = ToursTotal.objects.filter(name__contain ='kw')
#     return render(request, template_name='destination.html')
#
#
# def tour_detail(request):
#     return render(request, template_name='detail-tour-dl.html')
#
#
# def booking(request):
#     return render(request, template_name='booking.html')
#
#
# def hotel(request):
#     return render(request, template_name='hotel.html')
#
#
# def blog(request):
#     return render(request, template_name='blog.html')
#
#
# def login(request):
#     return render(request, template_name='login.html')

# def tourdetail(request):
#     return  render(request,template_name='tourdetail.html')
#
# def tourdetail(request):
#     return  render(request,template_name='tourdetail.html')
