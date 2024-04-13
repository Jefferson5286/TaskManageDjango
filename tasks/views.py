from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.request import Request

from tasks.api.serializers import TaskSerializer
from tasks.models import Task


@api_view(['POST'])
def create_task(request: Request):
    serializer = TaskSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_many_tasks(request: Request):
    serializer = TaskSerializer(data=request.data, many=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_many_tasks(request: Request):
    ids = request.data.get('ids')

    if not ids:
        return Response('not IDs!', status=status.HTTP_400_BAD_REQUEST)

    delete_tasks = Task.objects.filter(id__in=ids).delete()

    if delete_tasks[0] > 0:
        return Response('Tasks deleted successfully!', status=status.HTTP_204_NO_CONTENT)

    return Response('IDs not found!', status=status.HTTP_404_NOT_FOUND)

