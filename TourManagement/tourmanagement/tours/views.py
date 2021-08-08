from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from rest_framework import generics, viewsets ,permissions ,status
from rest_framework.parsers import MultiPartParser
from  .models import *
from .serializers import *


# def index (request):
#     return  render(request, template_name='index.html' , context= {'name' : 'abc'} )
#
# class UserViewSet(viewsets.ViewSet, generics.CreateAPIView,generics.ListAPIView,  # tao
#                   generics.RetrieveAPIView):  # lay thong tin
#     queryset = User.objects.filter(is_active=True)
#     serializer_class = UserSerializers
#     parser_classes = [MultiPartParser]
#
#     def get_permissions(self):
#         if self.action == 'retrieve':
#             return [permissions.IsAuthenticated()]
#
#         return [permissions.AllowAny()]


class ToursTotalViewSet(viewsets.ModelViewSet):
    queryset = ToursTotal.objects.filter(active=True)
    serializer_class = TourTotalSerializers
    # permission_classes = [permissions.IsAuthenticated]

    # @swagger_auto_schema(
    #     operation_description='Add tags to a lesson',
    #     responses={
    #                   status.HTTP_200_OK: LessonSerializers()
    #               }
    # )
    # @action(methods=['post'], detail=True, url_path="hide-lesson", url_name="hide-lesson")
    # def hide_lesson(self, request, pk):
    #     try:
    #         l = Lesson.objects.get(pk=pk)
    #         l.active = False
    #         l.save()
    #     except Lesson.DoesNotExits:
    #         return Response(status=status.HTTP_400_BAD_REQUEST)
    #
    #     return Response(LessonSerializers(l, context={'request': request}).data,
    #                     status=status.HTTP_200_OK)


class ToursDetailViewSet(viewsets.ModelViewSet):
    queryset = ToursDetail.objects.filter(active=True)
    serializer_class = TourDetailSerializers

class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.filter(active=True)
    serializer_class = HotelSerializers



class UserViewSet(viewsets.ViewSet, generics.CreateAPIView,generics.ListAPIView,  # tao
                  generics.RetrieveAPIView):  # lay thong tin
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializers
    parser_classes = [MultiPartParser]

    def get_permissions(self):
        if self.action == 'retrieve':
            return [permissions.IsAuthenticated()]

        return [permissions.AllowAny()]

