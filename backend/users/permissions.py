from rest_framework import permissions


class IsOwnerOrAdmin(permissions.BasePermission):
    # for object level permissions
    def has_object_permission(self, request, view, obj):
        return (obj.user == request.user or request.user.is_staff) and request.user.is_active


class IsStaffUserOrAdmin(permissions.BasePermission):
    # for view permission
    def has_permission(self, request, view):
        return request.user and request.user.is_staff and request.user.is_active

    # for object level permissions
    def has_object_permission(self, request, view, obj):
        return request.user and request.user.is_staff and request.user.is_active


class IsAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_superuser and request.user.is_active

    def has_object_permission(self, request, view, obj):
        return request.user and request.user.is_superuser and request.user.is_active


class IsTeacherUser(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return request.user.is_teacher and request.user.is_active

    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False
        return request.user.is_teacher and request.user.is_active


class IsPartnerUser(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return request.user.is_partner and request.user.is_active

    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False
        return request.user.is_partner and request.user.is_active


class IsStudentUser(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return request.user.is_student and request.user.is_active

    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False
        return request.user.is_student and request.user.is_active
