import pandas as pd
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response

from .models import Student
from courses.models import Course


@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
def upload_students(request):

    if 'file' not in request.FILES:
        return Response({"error": "No file uploaded"}, status=400)

    file = request.FILES['file']

    df = pd.read_excel(file)

    for _, row in df.iterrows():

        try:
            course = Course.objects.get(name=row['course'])

            Student.objects.create(
                reg_number=row['reg_number'],
                full_name=row['full_name'],
                email=row['email'],
                phone_number=row['phone'],
                course=course,
                year_of_study=row['year']
            )

        except Exception as e:
            return Response({"error": str(e)}, status=400)

    return Response({"message": "Students uploaded successfully"})