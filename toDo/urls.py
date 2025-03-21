from django.urls import path # type: ignore
from . import views
urlpatterns = [
path('addTask',views.addTask, name ='addTask'),
 path('mark_as_done/<int:pk>/', views.mark_as_done, name='mark_as_done'),
 path('mark_as_undone/<int:pk>/', views.mark_as_undone, name='mark_as_undone'),
 path('edit_task/<int:pk>/', views.edit_task, name='edit_task'),
 path('deleted_task/<int:pk>/', views.deleted_task, name='deleted_task'),

]