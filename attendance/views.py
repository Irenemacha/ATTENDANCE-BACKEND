from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from courses.models import Subject, LecturerSubject
from students.models import Student
from .models import Session, Attendance


# 🔥 START SESSION
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def start_session(request):

    subject_id = request.data.get('subject_id')

    try:
        subject = Subject.objects.get(id=subject_id)
    except Subject.DoesNotExist:
        return Response({"error": "Invalid subject_id"})

    if not LecturerSubject.objects.filter(
        lecturer=request.user,
        subject=subject
    ).exists():
        return Response({"error": "Not allowed to start session"})

    session = Session.objects.create(
        subject=subject,
        lecturer=request.user,
        is_active=True
    )

    return Response({
        "message": "Session started",
        "session_id": session.id
    })


# 🔥 CHECK IN
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def check_in(request):

    reg_number = request.data.get('reg_number')

    try:
        student = Student.objects.get(reg_number=reg_number)
    except Student.DoesNotExist:
        return Response({"error": "Student not found"})

    session = Session.objects.filter(is_active=True).last()
    if not session:
        return Response({"error": "No active session"})

    if Attendance.objects.filter(session=session, student=student).exists():
        return Response({"error": "Already checked in"})

    Attendance.objects.create(
        session=session,
        student=student,
        status="present"
    )

    return Response({
        "message": "Check-in successful",
        "student": student.full_name,
        "session": session.subject.name
    })