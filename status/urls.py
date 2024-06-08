from django.urls import path 
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('computer',views.computer,name='computer'),
    path('display',views.display,name='display'),
    path('base',views.base,name='base'),
    path('lab1',views.lab1,name='lab1'),
    path('lab2',views.lab2,name='lab2'),
    path('comp',views.complaint,name='comp'),
    path('submit',views.submit,name='submit'),
    path('edit/<int:pk>/', views.edit_computer, name='edit_computer'),
    path('report',views.report,name='report')
    
]