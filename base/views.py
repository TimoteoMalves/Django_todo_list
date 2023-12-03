from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Task
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


class CustomLoginView(LoginView):
   template_name = "base/login.html"
   fields = '__all__' # asking for it to create all fields of our model
   redirect_authenticated_user = True

   def get_success_url(self):
      return reverse_lazy('tasks')
   
class RegisterPage(FormView):
   template_name = 'base/register.html'
   form_class = UserCreationForm
   redirect_authenticated_user = True
   success_url = reverse_lazy('tasks')


   # checking if the user is logged in once the form is saved
   def form_valid(self, form):
      user = form.save()
      if user is not None:
         login(self.request, user) #login if completed, no need to ask to log
      return super(RegisterPage, self).form_valid(form)

class TaskList(LoginRequiredMixin, ListView): #inheriting from ListView
   model = Task
   context_object_name = "tasks" #changing the object name so we can access it in a better way

   # making sure the user sees his own data only
   def get_context_data(self, **kwargs): #js ...
      context = super().get_context_data(**kwargs)
      context['tasks'] = context['tasks'].filter(user=self.request.user)
      context['count'] = context['tasks'].filter(complete=False).count() #counting incomplete

      search_input = self.request.GET.get('search-area') or ''
      if search_input:
         context['tasks'] = context['tasks'].filter(title__startswith=search_input) #startswith the input

      context['search_input'] = search_input
      return context

class TaskDetail(LoginRequiredMixin, DetailView): #inheriting from DetailView 
   model = Task
   context_object_name = "task_detail"

class TaskCreate(LoginRequiredMixin, CreateView):
   model = Task
   fields = ['title', 'description','complete']  # asking for it to create all fields of our model
   success_url = reverse_lazy('tasks') #navigate back to tasks screen 

   #
   def form_valid(self, form):
      form.instance.user = self.request.user
      return super(TaskCreate, self).form_valid(form)

class TaskUpdate(LoginRequiredMixin, UpdateView):
   model = Task
   fields = "__all__"
   success_url = reverse_lazy('tasks')

class DeleteView(LoginRequiredMixin, DeleteView):
   model = Task
   context_object_name = "task"
   success_url = reverse_lazy('tasks')
