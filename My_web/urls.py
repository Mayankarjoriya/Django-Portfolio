from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('projects/', views.projects, name='projects'),
    path('base/', views.base, name='base'),
]