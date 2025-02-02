from django.urls import path
from . import views


app_name = 'lessons'

urlpatterns = [
    path('lessons-list/', views.lessons_list, name='list'),
    path('lesson-create/', views.create_lesson, name='create'),
    path('lesson-detail/<int:pk>/', views.lesson_detail, name='detail'),
    path('lesson-delete/<int:pk>/', views.delete_lesson, name='delete'),
    path('edit-lesson/<int:pk>/', views.edit_lesson, name='edit'),
]