from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:curso_id>', views.edu, name='edu'),
    path('cadastro', views.cadastro, name='cadastro'),
]
