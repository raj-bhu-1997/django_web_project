"""hostproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import login_page, user_creation, home_page, create_page, about_page, product_page, post_page
from django.contrib.auth import logout
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_page.as_view(), name='login'),
    path('create/', user_creation.as_view(), name='create'),
    path('home/', home_page.as_view(), name = 'home'),
    path('post/', post_page.as_view(), name='post'),
    path('logout/', LogoutView.as_view(next_page ='login'), name = 'logout'),
    path('add_post/', create_page.as_view(), name = 'add_post'),
    path('about/', about_page.as_view(), name = 'about'),
    path('product/', product_page.as_view(), name='product'),
    
    
]
