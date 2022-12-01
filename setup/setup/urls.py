
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('produtos', views.Produtos_base, name = 'Produtos_base'),
    path('produtos/<int:pk>/', views.Produtos_putID, name="Produtos_putID"),
    path('produtos/del/<int:pk>/', views.Produtos_delete, name="Produtos_delete"),
 
]
