# views.py
from rest_framework import views
from rest_framework.response import Response
from .models import Item
from rest_framework import status
from .serializers import ItemSerializer
from django.http import Http404
from rest_framework import viewsets
from django.views.generic import DetailView
from django.shortcuts import render

# ModelViewSet to show pages created by default
class MyViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    
# API Views
class TaskCreateView(views.APIView):
    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskListView(views.APIView):
    def get(self, request):
        tasks = Item.objects.all()
        serializer = ItemSerializer(tasks, many=True)
        print(serializer.data)
        return Response(serializer.data)

class TaskDetailView(views.APIView):
    def get_object(self, pk):
        try:
            return Item.objects.get(pk=pk)
        except Item.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        task = self.get_object(pk)
        serializer = ItemSerializer(task)
        return Response(serializer.data)

    def put(self, request, pk):
        task = self.get_object(pk)
        serializer = ItemSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        task = self.get_object(pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def item_detail(request, pk):
    item = Item.objects.get(id=pk)
    return render(request, 'item_detail.html', {'item': item})



