from django.urls import path
from peoples import views

app_name = 'peoples'

urlpatterns = [
    path('', views.StudentListView.as_view(), name='student-list'),
    path('students/create/', views.StudentCreateView.as_view(), name='student-create'),
    path('students/update/<int:pk>/', views.StudentUpdateView.as_view(), name='student-edit'),
    path('students/detail/<int:pk>/', views.StudentDetailView.as_view(), name='student-detail'),
    path('stuff/', views.StuffListView.as_view(), name='stuff-list'),
    path('stuff/create/', views.StuffCreateView.as_view(), name='stuff-create'),
    path('stuff/update/<int:pk>/', views.StuffUpdateView.as_view(), name='stuff-edit'),
    path('stuff/detail/<int:pk>/', views.StuffDetailView.as_view(), name='stuff-detail'),
]