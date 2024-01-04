from django.urls import path
from main import views

app_name = 'main'

urlpatterns = [
    path('', views.DepartmentListView.as_view(), name='department-list'),
    path('departments/create/', views.DepartmentCreateView.as_view(), name='department-create'),
    path('departments/update/<int:pk>/', views.DepartmentUpdateView.as_view(), name='department-edit'),
    path('departments/detail/<int:pk>/', views.DepartmentDetailView.as_view(), name='department-detail'),
    path('faculties/', views.FacultyListView.as_view(), name='faculty-list'),
    path('faculties/create/', views.FacultyCreateView.as_view(), name='faculty-create'),
    path('faculties/update/<int:pk>/', views.FacultyUpdateView.as_view(), name='faculty-edit'),
    path('faculties/detail/<int:pk>/', views.FacultyDetailView.as_view(), name='faculty-detail'),
    path('statements/', views.StatementListView.as_view(), name='statement-list'),
    path('statements/create/', views.StatementCreateView.as_view(), name='statement-create'),
    path('statements/update/<int:pk>/', views.StatementUpdateView.as_view(), name='statement-edit'),
    path('statements/detail/<int:pk>/', views.StatementDetailView.as_view(), name='statement-detail'),
]
