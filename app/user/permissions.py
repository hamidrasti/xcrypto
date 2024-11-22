from rest_framework import permissions


class CurrentUserOrAdmin(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        user = request.user
        return user.is_staff or obj.pk == user.pk


class CurrentUserOrAdminOrReadOnly(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        user = request.user
        if isinstance(obj, type(user)) and obj == user:
            return True
        return request.method in permissions.SAFE_METHODS or user.is_staff
