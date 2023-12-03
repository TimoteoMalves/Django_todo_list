# thats how we create our pattern
from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, DeleteView, CustomLoginView, RegisterPage
from django.contrib.auth.views import LogoutView

# we create the urls that can be access the view, just like in reat, we handle it to use it 
urlpatterns = [
   path('login/', CustomLoginView.as_view(), name='login'), 
   path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
   path('register/', RegisterPage.as_view(), name='register'),

   path('', TaskList.as_view(), name='tasks'), #as_view its because url cant handle a class without it
   path('task/<int:pk>', TaskDetail.as_view(), name='task'),
   path('task-create/', TaskCreate.as_view(), name='task_create'),
   path('task-update/<int:pk>', TaskUpdate.as_view(), name='task_update'),
   path('task-delete/<int:pk>', DeleteView.as_view(), name='task_delete'),
]