# from django.shortcuts import render

# # Create your views here.
# from rest_framework.views import APIView
# from rest_framework import viewsets
# from .models import Task
# from .serializers import TaskSerializer as UserSerializer
# from rest_framework.response import Response
# from rest_framework import status

# class UserListView(APIView):
#     def get(self, request, format=None):
#         """
#         Return a list of all users.
#         """
#         users = Task.objects.all()
#         serializer = UserSerializer(users, many=True)
#         return Response(serializer.data)

# class UserCreateView(APIView):
#     def post(self, request, format=None):
#         """
#         Create a new user.
#         """
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class UserDetailView(APIView):
#     def get_object(self, pk):
#         try:
#             return Task.objects.get(pk=pk)
#         except Task.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)

#     def get(self, request, pk, format=None):
#         """
#         Retrieve a user.
#         """
#         user = self.get_object(pk)
#         serializer = UserSerializer(user)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         """
#         Update a user.
#         """
#         user = self.get_object(pk)
#         serializer = UserSerializer(user, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         """
#         Delete a user.
#         """
#         user = self.get_object(pk)
#         user.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)







# class TaskViewSet(viewsets.ModelViewSet):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer

# def task_list(request):
#     tasks = TaskViewSet.as_view({'get': 'list'})(request)
#     return render(request, 'task_list.html', {'tasks': tasks.data})

# # API VIEW 
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Task
# from .serializers import TaskSerializer

# class TaskList(APIView):
#     def get(self, request):
#         tasks = Task.objects.all()
#         serializer = TaskSerializer(tasks, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = TaskSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class TaskDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return Task.objects.get(pk=pk)
#         except Task.DoesNotExist:
#             raise Response("Not so good")

#     def get(self, request, pk):
#         task = self.get_object(pk)
#         serializer = TaskSerializer(task)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         task = self.get_object(pk)
#         serializer = TaskSerializer(task, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         task = self.get_object(pk)
#         task.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

#----------------------2--------------------------------
# from django.shortcuts import render, redirect
# from django.urls import reverse
# from .models import Item

# def item_list(request):
#     items = Item.objects.all()
#     return render(request, 'item_list.html', {'items': items})

# def item_create(request):
#     if request.method == 'POST':
#         name = request.POST['name']
#         description = request.POST['description']
#         Item.objects.create(name=name, description=description)
#         return redirect(reverse('item_list'))
#     return render(request, 'item_create.html')

# def item_update(request, pk):
#     item = Item.objects.get(pk=pk)
#     if request.method == 'POST':
#         item.name = request.POST['name']
#         item.description = request.POST['description']
#         item.save()
#         return redirect(reverse('item_list'))
#     return render(request, 'item_update.html', {'item': item})

# def item_delete(request, pk):
#     item = Item.objects.get(pk=pk)
#     item.delete()
#     return redirect('item_list')


#--------------------------------3----------------------------------------------------
# views.py
from rest_framework import views
from rest_framework.response import Response
from .models import Item
from rest_framework import status
from .serializers import ItemSerializer as TaskSerializer
from django.http import Http404
from rest_framework import viewsets
from django.views.generic import DetailView
from django.shortcuts import render

class MyViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = TaskSerializer

def item_detail(request, pk):
    item = Item.objects.get(id=pk)
    return render(request, 'item_detail.html', {'item': item})

class TaskCreateView(views.APIView):
    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskListView(views.APIView):
    def get(self, request):
        print("HEHEHEHE")
        tasks = Item.objects.all()
        serializer = TaskSerializer(tasks, many=True)
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
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def put(self, request, pk):
        task = self.get_object(pk)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        task = self.get_object(pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



