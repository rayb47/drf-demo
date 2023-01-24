from django.urls import path, include
from rest_framework.routers import DefaultRouter
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



