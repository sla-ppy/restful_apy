from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Task
from .serializers import TaskSerializer

# Create your views here.
def index(request):
    return HttpResponse("Tasks index")

# First endpoint view
class TaskListApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        tasks = Task.objects
        serializer = TaskSerializer(tasks, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            'title': request.data.get('title'),
            'description': request.data.get('description'),
            'creation_date': request.data.get('creation_date'),
            'due_date': request.data.get('due_date'),
            'status': request.data.get('status')
        }

        serializer = TaskSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)