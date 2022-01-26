from rest_framework.pagination import PageNumberPagination


class ToursTotalPagination(PageNumberPagination):
    page_size = 6


class TourDetailPagination(PageNumberPagination):
    page_size = 20


class BlogPagination(PageNumberPagination):
    page_size = 6
