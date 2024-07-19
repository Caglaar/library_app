from rest_framework import permissions



class isAdminUserOrReadOnly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        is_admin = super().has_permission(request=request, view=view)
        return (
            is_admin or
            request.method in permissions.SAFE_METHODS
        )