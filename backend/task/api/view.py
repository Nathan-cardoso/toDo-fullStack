from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from ..models import Task
from ..api.serializer import TaskForUserSerializer

class TaskViewSet(viewsets.ModelViewSet):

    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TaskForUserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)