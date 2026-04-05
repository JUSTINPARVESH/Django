# Force Django auto-reload
from django.urls import path
from .views import (
    RegisterView,
    ProfileView,
    AdminOnlyView,
    TeacherOnlyView,
    custom_login,
    register_page,
    student_dashboard
)

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.contrib.auth import views as auth_views

urlpatterns = [

    # 🔥 API AUTH (POSTMAN / API)
    path('register/', RegisterView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),

    # 🎨 UI PAGES
    path('custom-login/', custom_login),
    path('register-page/', register_page),
    path('student-dashboard/', student_dashboard),

    # 🔐 USER APIs
    path('profile/', ProfileView.as_view()),

    # 🎯 ROLE BASED
    path('admin-only/', AdminOnlyView.as_view()),
    path('teacher-only/', TeacherOnlyView.as_view()),

    # 📧 PASSWORD RESET
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
]