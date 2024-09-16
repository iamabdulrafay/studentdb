from .models import StudentModel

from rest_framework_mongoengine import serializers



class StudentSerializer(serializers.DocumentSerializer):
    class Meta:
        model = StudentModel
        fields = '__all__'
 
