from rest_framework.permissions import BasePermission


# 👑 Admin only
class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'ADMIN'


# 👨‍🏫 Teacher only
class IsTeacher(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'TEACHER'


# 🎓 Student only
class IsStudent(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'STUDENT'