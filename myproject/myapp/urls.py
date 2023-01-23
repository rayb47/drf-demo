from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from .views import TaskViewSet, task_list

# router = DefaultRouter()
# router.register(r'tasks', TaskViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
#      path('tasks/', task_list, name='task_list')
# ]

# from django.urls import path
# from .views import UserListView, UserCreateView, UserDetailView
# from django.shortcuts import render

# # def task_list(request):
# #     return render(request, 'task_list.html')


# urlpatterns = [
#     # path('users/', task_list, name='task_list'),
#     path('users/', UserListView.as_view(), name='user_list'),
#     path('users/create/', UserCreateView.as_view(), name='user_create'),
#     path('users/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
# ]

# from django.urls import path
# from .views import TaskList, TaskDetail

# urlpatterns = [
#     path('tasks/', TaskList.as_view()),
#     path('tasks/<int:pk>/', TaskDetail.as_view()),
# ]

#------------------------------------------2---------------------------------------
# from django.urls import path
# from .views import item_list, item_create, item_update, item_delete

# urlpatterns = [
#     path('items/', item_list, name='item_list'),
#     path('items/create/', item_create, name='item_create'),
#     path('items/update/<int:pk>/', item_update, name='item_update'),
#     path('items/delete/<int:pk>/', item_delete, name='item_delete'),
# ]


#------------------------------------3-------------------------------------------
from django.urls import path, include
from .views import TaskCreateView, TaskListView, TaskDetailView
from django.views.generic.base import TemplateView
from rest_framework import routers
from .views import MyViewSet, item_detail

router = routers.DefaultRouter()
router.register(r'Item', MyViewSet)

urlpatterns = [
    path('tasks/', TaskListView.as_view(),  name='task-list'),
    path('tasks/create/', TaskCreateView.as_view(), name='task-create'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(),  name='task-detail'),
    path('task/detail/<int:pk>/', item_detail,  name='item-detail'),
    path('home/', TemplateView.as_view(template_name='item_list.html')),
    path('', include(router.urls))

]



