from django.shortcuts import render, redirect
from .entidades import twitter
from .services import argo_service
from .forms import ArgoForm
from .models import Argo


def listar_tags(request):
    argo = argo_service.listar()
    return render(request, 'twitter/listar.html', {'argo': argo})


def inserir_tags(request):
    # aqui fazemos a validação das informações e inserimos no DB
    if request.method == "POST":
        form = ArgoForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            descricao = form.cleaned_data['descricao']
            tag_novo = twitter.Argo(nome=nome, descricao=descricao)
            argo_service.cadastrar(tag_novo)
            return redirect('listar')
    else:
        form = ArgoForm()
    return render(request, 'twitter/form.html', {'form': form})


def listar_tag_id(request, id):
    argo = Argo.objects.get(id=id)
    return render(request, 'twitter/form.html', {'argo': argo})
