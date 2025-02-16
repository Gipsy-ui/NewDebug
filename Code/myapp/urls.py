from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('save/', views.save, name='save'),
    path('edit/<str:model_type>/<int:id>/', views.edit, name='edit'),
    path('update/<str:model_type>/<int:id>/', views.update, name='update'),  # Updated for both models
    path('delete/<str:model_type>/<int:id>/', views.delete, name='delete'),
]
