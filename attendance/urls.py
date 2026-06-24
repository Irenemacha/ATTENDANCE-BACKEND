from django.urls import path
from .views import start_session, check_in

urlpatterns = [
    path('start/', start_session),
    path('checkin/', check_in),
]