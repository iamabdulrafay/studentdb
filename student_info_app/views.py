from .models import StudentModel
from .serializers import StudentSerializer

from rest_framework import viewsets


 

class StudentViewSet(viewsets.ModelViewSet):
    
    queryset = StudentModel.objects.all()    

    serializer_class = StudentSerializer