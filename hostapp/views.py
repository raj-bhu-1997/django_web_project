from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView
from django.views.generic import TemplateView

#login logout and authenticate

class login_page(LoginView):
  template_name = 'hostapp/login.html'
  fields = '__all__'
  def post(self, request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username= username, password= password)
    if user is not None:
      login(self.request, user)
      return redirect('home')
    else:
      return render(request, 'hostapp/login_fail.html')
    
# crud operation 

class user_creation(FormView):
  form_class = UserCreationForm
  template_name = 'hostapp/user_create.html'
  success_url = reverse_lazy('login')
  def form_valid(request, form):
    user = form.save()
    user.save()
    return super().form_valid(form)
      

class post_page(LoginRequiredMixin, ListView):
  model = Post
  template_name = 'hostapp/post.html'
  fields = '__all__'
  context_object_name = 'objects'

class detail_page(LoginRequiredMixin, DetailView):
  model = Post
  template_name = 'hostapp/detail.html'
  context_object_name = 'object'

class create_page(LoginRequiredMixin, CreateView):
  model = Post
  template_name = 'hostapp/create.html'
  fields = '__all__'
  success_url = reverse_lazy('post')
  
class update_page(LoginRequiredMixin, UpdateView):
  model = Post
  success_url = reverse_lazy('post')

class delete_page(LoginRequiredMixin, DeleteView):
  model = Post
  success_url = reverse_lazy('post')
  
# template view

class product_page(LoginRequiredMixin, TemplateView):
  template_name = 'hostapp/product.html'
  
  
class about_page(LoginRequiredMixin, TemplateView):
  template_name = 'hostapp/about.html'
  
class home_page(LoginRequiredMixin, TemplateView):
  template_name = 'hostapp/home.html'