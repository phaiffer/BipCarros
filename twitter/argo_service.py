from ..models import Argo


def listar():
    argo = Argo.objects.all()
    return argo


def listar_id(id):
    argo = Argo.objects.get(id=id)
    return argo


def remover(argo):
    argo.delete()


def cadastrar(argo):
    Argo.objects.create(nome=argo.nome, descricao=argo.descricao)
