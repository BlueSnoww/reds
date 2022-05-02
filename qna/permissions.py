from rest_framework import permissions


class UpdateOwnQna(permissions.BasePermission):
    """Allow users to edit their own profile"""

    def has_permission(self, request, view):
        """Check user is staff or superuser"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_superuser or request.user.is_staff