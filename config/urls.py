from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Geofencing Attendance System API",
        default_version='v1',
        description="""
        This API handles:
        - Student Registration & Login (JWT Authentication)
        - Fingerprint Verification
        - OTP Device Verification
        - Geofencing Attendance (GPS/WiFi/BLE)
        - Attendance Reports

        NOTE: Student app is mobile-only. Web app handles Lecturer/HOD/Admin.
        """,
        terms_of_service="",
        contact=openapi.Contact(email="support@attendance.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)



urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/accounts/', include('accounts.urls')),
    path('api/students/', include('students.urls')),
    path('api/attendance/', include('attendance.urls')),
    path('api/courses/', include('courses.urls')),


   
    # 🔥 ADD HII (IMPORTANT)
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc'),
]