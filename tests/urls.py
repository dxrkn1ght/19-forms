from django.urls import path
from . import views


app_name = 'tests'

urlpatterns = [
    path('test-list/', views.test_list, name='list'),
    path('test-create/', views.create_test, name='create'),
    path('test-delete/<int:pk>', views.delete_test, name='delete'),
    path('test-detail/<int:pk>', views.test_detail, name='detail'),
    path('edit-test/<int:pk>/', views.edit_test, name='edit')
]