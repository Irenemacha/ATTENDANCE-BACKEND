from django.db import models
from django.conf import settings

from students.models import Student
from courses.models import Subject


# 🔥 SESSION MODEL
class Session(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    lecturer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.subject.name} - {'Active' if self.is_active else 'Closed'}"


# 🔥 ATTENDANCE MODEL (THIS WAS MISSING)
class Attendance(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    time_in = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default="present")

    class Meta:
        unique_together = ('session', 'student')

    def __str__(self):
        return f"{self.student.reg_number} - {self.session.subject.name}"