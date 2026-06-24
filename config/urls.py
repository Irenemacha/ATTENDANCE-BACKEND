from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),

    # AUTH (JWT LOGIN)
    path('api/auth/login/', TokenObtainPairView.as_view()),
    path('api/auth/refresh/', TokenRefreshView.as_view()),

    # APPS
    path('api/courses/', include('courses.urls')),
    path('api/students/', include('students.urls')),
    path('api/attendance/', include('attendance.urls')),
]