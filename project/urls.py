from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('newtask', views.new_form, name='new_form'),
    path('add', views.addTask, name='add'),
    path('complete/<task_id>', views.completed, name='completed'),
    path('deletecomplete', views.deleteCompleted, name='deletecomplete'),
    path('deleteAll', views.deleteAll, name='deleteAll'),
]