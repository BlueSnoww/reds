from rest_framework import permissions


class UpdateOwnPrice(permissions.BasePermission):
    """Allow users to edit their own profile"""

    def has_permission(self, request, view):
        """Check user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_superuser or request.user.is_staff