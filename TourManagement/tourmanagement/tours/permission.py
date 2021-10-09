from rest_framework.permissions import BasePermission, SAFE_METHODS


class UserPermission(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_superuser :
            return True
        elif request.method in SAFE_METHODS or view.action in ['del_user','']:
            return request.user.is_superuser
        elif view.action in ["create",'forgot_password']:
            return True
        return request.user.is_authenticated

class TourToTalPermission(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        elif request.method in SAFE_METHODS or view.action in ['PUT', 'PATCH','create','add_tags']:
            return request.user.is_superuser
        return request.user.is_authenticated
