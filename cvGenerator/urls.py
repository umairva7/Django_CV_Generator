from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from pdf import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Home page
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),  # Login
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),  # Logout
    path('submit/', views.submit, name='submit'),  # Form submission (requires login)
    path('waiting/<int:id>/', views.waiting, name='waiting'),  # Waiting page
    path('resume/<int:id>/', views.generating, name='generating'),  # Generate resume
    path('list/', views.list, name='list'),  # List of all CVs (requires login)
]
