from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_pets, name='list_pets'),
    path('breeds/', views.breed_list, name='breed_list'),
    path('dogs/', views.dog_list, name='dog_list'),
    path('create/', views.create_pet, name='create_pet'),
    path('update/<int:pk>/', views.update_pet, name='update_pet'),
    path('delete/<int:pk>/', views.delete_pet, name='delete_pet'),
]
