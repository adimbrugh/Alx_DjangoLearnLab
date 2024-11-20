

from rest_framework.permissions import BasePermission


class IsAuthorORReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True # Read-only permissions for any request
        return obj.author == request.user # Write permissions for the object's author only