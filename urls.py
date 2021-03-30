from django.urls import path
from .views import *

urlpatterns = [
    path('listar/tags', listar_tags, name='listar'),
    path('cadastrar', inserir_tags, name='form'),
    path('listar/<int:id>', listar_tag_id, name='listar_tag_id'),
]