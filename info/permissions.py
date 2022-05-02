from rest_framework import permissions


class UpdateOwnInfo_and_tag(permissions.BasePermission):
    """Allow me n staff to edit their own Info"""

    def has_permission(self, request, view):
        """Check user is staff or superuser"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_superuser or request.user.is_staff



