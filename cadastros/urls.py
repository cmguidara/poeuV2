from django.urls import path

#views criadas para o app
from .views import EmpresaCreate, VagaCreate
from .views import EmpresaUpdate, VagaUpdate
from .views import EmpresaDelete, VagaDelete
from .views import EmpresaList, VagaList, AlunoList, AnuncioList


urlpatterns = [
    path('cadastrar/empresa', EmpresaCreate.as_view(), name='cadastrar-empresa'),
    path('cadastrar/vaga', VagaCreate.as_view(), name='cadastrar-vaga'),


    path('editar/empresa/<int:pk>/', EmpresaUpdate.as_view(), name='editar-empresa'),
    path('editar/vaga/<int:pk>/', VagaUpdate.as_view(), name='editar-vaga'),

    path('excluir/empresa/<int:pk>/', EmpresaDelete.as_view(), name='excluir-empresa'),
    path('excluir/vaga/<int:pk>/', VagaDelete.as_view(), name='excluir-vaga'),

    path('listar/empresas/', EmpresaList.as_view(), name='listar-empresas'),
    path('listar/vagas/', VagaList.as_view(), name = 'listar-vagas'),

    path('listar/mural/', AlunoList.as_view(), name = 'mural'),

    path('listar/vaga/<int:pk>', AnuncioList.as_view(), name= 'anuncio'),

]

