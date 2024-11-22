from django.urls import path
from . import views

from django.urls import path
from . import views

urlpatterns = [
    # Researcher URLs
    path('researchers/', views.researcher_list, name='researcher_list'),
    path('researchers/<int:pk>/', views.researcher_detail, name='researcher_detail'),
    path('researchers/add/', views.add_researcher, name='add_researcher'),
    path('researchers/<int:pk>/edit/', views.edit_researcher, name='edit_researcher'),
    path('researchers/<int:pk>/delete/', views.delete_researcher, name='delete_researcher'),

    # Research Project URLs
    path('projects/', views.project_list, name='project_list'),
    path('projects/<int:pk>/', views.project_detail, name='project_detail'),
    path('projects/add/', views.add_project, name='add_project'),
    path('projects/<int:pk>/edit/', views.edit_project, name='edit_project'),
    path('projects/<int:pk>/delete/', views.delete_project, name='delete_project'),
]

