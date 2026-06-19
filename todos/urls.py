from django.urls import path
from . import views
urlpatterns=[
    path('list/',views.home,name='list-tasks'),
    path('create/',views.create_task,name='create-task'),
    path('delete/<int:id>',views.delete_task,name='delete-task'),
    path('edit-task/<int:id>',views.update_task,name='edit-task'),
    path('register/',views.register,name='register')
]