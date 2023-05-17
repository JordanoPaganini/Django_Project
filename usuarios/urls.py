from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar_vendedor/', views.cadastar_vendedor, name='cadastar_vendedor')
]