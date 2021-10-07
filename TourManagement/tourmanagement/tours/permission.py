from rest_framework.permissions import BasePermission,SAFE_METHODS

class UserPermission(BasePermission):

    def has_permission(self, request, view):
        if view.action in ['current_user', 'booking_detail', 'change_password']:
            return request.user.is_authenticated
        # if request.method in SAFE_METHODS or view.action == "create":
        #     return True
        return request.user.is_authenticated


    # def upgrate_permission(self,request,view):
    #     if view.action in ['']
    #         return request.user.is_authenticated