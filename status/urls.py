from django.urls import path 
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('computer',views.computer,name='computer'),
    path('display',views.display,name='display'),
    path('base',views.base,name='base'),
    path('comp/<int:pk>/',views.complaint,name='comp'),
    path('submit',views.submit,name='submit'),
    path('edit/<int:pk>/', views.edit_computer, name='edit_computer'),
    path('report',views.report,name='report'),
    path('complaint_report',views.complaint_report,name='complaint_report'),
    
 
    
    
]