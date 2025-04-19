from django.urls import path
from . import views

urlpatterns = [
    path('', views.code_list, name='code_list'),
    path('details', views.details, name='details'),
    path('add/', views.adddata, name='adddata'),
    path('about/<int:pk>/', views.about, name='about'),
    path('update/<int:pk>/', views.update_code_model, name='update_code_model'),  # Fixed name
    path('delete/<int:pk>/', views.delete_data, name='delete_data'),
]
