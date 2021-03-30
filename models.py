from django.db import models

class Argo(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)


def __str__(self):
    return self.nome