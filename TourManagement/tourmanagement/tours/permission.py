from rest_framework.permissions import BasePermission, SAFE_METHODS


class UserPermission(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        elif request.method in [SAFE_METHODS, 'PUT', 'PATCH'] or view.action in ['del_user', '']:
            return request.user.is_superuser
        elif view.action in ["create", 'forgot_password']:
            return True
        return request.user.is_authenticated


class TourToTalPermission(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        elif view.action in ['create', 'add_tags', "tour_detail", ''] or request.method in ['PUT', 'PATCH', 'DELETE']:
            return request.user.is_superuser
        return True


class TourDetailPermission(BasePermission):

    def has_permission(self, request, view):
        # if request.user.is_superuser:
        #     return True
        # elif view.action in ['create', 'add_tags', 'add_hotel', 'add_transport','add_img_detail'
        #     , "tour_detail"] or request.method in ['PUT', 'DELETE']:
        #     return request.user.is_superuser
        # elif request.method in ['PATCH']:
        #     return  request.user.is_superuser or request.user.active_staff
        # elif view.action in ['add_comment', 'add_rating']:
        #     return request.user.is_authenticated
        return True


class CmtPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        elif request.method in ['PUT']:
            return request.user.is_superuser
        elif request.method in ['PATCH', 'DELETE']:
            return request.user.is_authenticated
        return True

class HotelPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        elif view.action in ['create'] or request.method in ['PUT', 'PATCH', 'DELETE']:
            return request.user.is_superuser or request.user.active_staff
        return True


class TransportPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        elif request.method in ['PUT']:
            return request.user.is_superuser
        elif request.method in ['PATCH', 'DELETE'] or view.action in ['create']:
            return request.user.is_authenticated


class ImgDetailPermission(BasePermission):
    def has_permission(self, request, view):
        return True


class BlogPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['PUT', 'PATCH', 'DELETE'] or view.action in ['create']:
            return request.user.active_staff or request.user.is_superuser
        return True

class PriceRoomPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['PUT', 'PATCH', 'DELETE'] or view.action in ['create']:
            return request.user.active_staff or request.user.is_superuser
        return True
