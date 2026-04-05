from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login
from django.contrib import messages
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import RegisterSerializer
from .permissions import IsAdmin, IsTeacher

User = get_user_model()


# 🔥 API VIEWS
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({
            "email": request.user.email,
            "role": request.user.role
        })

class AdminOnlyView(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]

    def get(self, request):
        return Response({"message": "Welcome Admin!"})

class TeacherOnlyView(APIView):
    permission_classes = [IsAuthenticated, IsTeacher]

    def get(self, request):
        return Response({"message": "Welcome Teacher!"})


# 🔥 REGISTER PAGE
def register_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        role = request.POST.get("role")

        if password != confirm_password:
            return render(request, "register.html", {"error": "Passwords do not match ❌"})

        if User.objects.filter(email=email).exists():
            return render(request, "register.html", {"error": "Email already registered"})

        User.objects.create_user(
            email=email,
            password=password,
            role=role
        )

        messages.success(request, "Account created successfully 🔥")
        return redirect('/api/custom-login/')

    return render(request, "register.html")


    # 🔥 LOGIN PAGE
def custom_login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)

            if user.role == "ADMIN":
                return redirect('/api/admin-dashboard/')
            elif user.role == "TEACHER":
                return redirect('/api/teacher-dashboard/')
            else:
                return redirect('/api/student-dashboard/')

        return render(request, "login.html", {"error": "Invalid credentials ❌"})

    return render(request, "login.html")

# 🔥 STUDENT DASHBOARD
def student_dashboard(request):
    return render(request, "student_dashboard.html")

# 🔥 TEACHER DASHBOARD
def teacher_dashboard(request):
    return render(request, "teacher_dashboard.html")

# 🔥 ADMIN DASHBOARD
def admin_dashboard(request):
    return render(request, "admin_dashboard.html")