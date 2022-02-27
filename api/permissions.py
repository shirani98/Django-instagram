from rest_framework.permissions import BasePermission , SAFE_METHODS

class IsAdminOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        else:
            return bool(request.user.is_authenticated and request.user.is_admin)