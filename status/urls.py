from django.urls import path 
from . import views

urlpatterns = [
    path('',views.login_view,name='login'),
    path('home',views.home,name='home'),
    path('computer',views.computer,name='computer'),
    path('display',views.display,name='display'),
    path('base',views.base,name='base')
]