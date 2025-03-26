from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import StudentSerializer
from rest_framework.response import Response
from .models import Student

class StudentAPIView(APIView):
    def get(self,request,pk=None):
        if pk is not None:
            student = Student.objects.get(id=pk)
            serializer = StudentSerializer(student)
            return Response(serializer.data)
        student = Student.objects.all()
        serializer = StudentSerializer(student,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def put(self,request,pk=None):
        student = Student.objects.get(id=pk)
        serializer = StudentSerializer(instance=student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self,request,pk=None):
        student = Student.objects.get(id=pk)
        student.delete()
        return Response("deleted")