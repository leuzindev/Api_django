
from produto.serializer import ProdutoSerializer

from rest_framework import routers
from django.contrib import admin
from django.urls import path, include
from produto.views import (
    ProdutoAPI,
    ProdutoActions
)




urlpatterns = [
    path('admin/', admin.site.urls),
    path('produtos', ProdutoAPI.as_view()),
    path('produtos/<int:pk>/', ProdutoActions.as_view())
]
