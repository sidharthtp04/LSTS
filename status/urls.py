from django.urls import path 
from . import views

urlpatterns = [
    path('home',views.home,name='home'),
    path('computer',views.computer,name='computer'),
    path('display',views.display,name='display'),
    path('base',views.base,name='base'),
    path('comp/<int:pk>/',views.complaint,name='comp'),
    path('submit',views.submit,name='submit'),
    path('edit/<int:pk>/', views.edit_computer, name='edit_computer'),
    path('',views.report,name='report'),
    path('complaint_report',views.complaint_report,name='complaint_report'),
    path('report_generation/', views.report_generation, name='report_generation'),
    path('repair_detail/<int:pk>/', views.repair_detail, name='repair_detail'),
    path('delete_repair/<int:pk>/', views.delete_repair, name='delete_repair'),
    path('delete_complaint/<int:pk>/', views.delete_complaint, name='delete_complaint'),
    path('new/', views.new_page, name='new_page'),
    path('record_repair/',views.record_repair, name='record_repair'),
    path('delete/<int:computer_id>/', views.change_status_to_trashed, name='change_status_to_trashed'),
    path('trashed/', views.trashed_computers, name='trashed_computers'),
    path('complaint_report/<int:computer_id>/', views.computer_complaint_report, name='complaint_report'),
]