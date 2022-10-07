# Registros/models.py
from django.conf import settings
from django.contrib.auth import get_user_model, get_user
from django.db import models
from django.urls import reverse
from usuarios.models import CustomUser
from django.utils.functional import lazy


def choices_():
    return CustomUser.objects.filter(Finalidade='r').values_list("username", "username")

class Registro(models.Model):
    doacao = models.CharField(max_length=255, verbose_name='Doação')
    contato = models.CharField(max_length=255, null=True, blank=False, verbose_name='Telefone para contato')
    endereco = models.CharField(max_length=255, null=True, blank=False, verbose_name='Endereço para entrega')
    obs = models.TextField(blank=True, verbose_name='Observação')
    data_1 = models.DateTimeField(auto_now_add=True, verbose_name='Data')
    instituicao = models.CharField(choices=CustomUser.objects.filter(Finalidade='r').values_list(
        "username", "username"), null=True, max_length=150)
    doador = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=False)

    def __init__(self, *args, **kwargs):
        super(Registro, self).__init__(*args, **kwargs)
        self._meta.get_field('instituicao').choices = lazy(choices_, list)()

    def __str__(self):
        return self.doacao

    def get_absolute_url(self):
        return reverse('article_list')


class Comentario(models.Model):
    registro = models.ForeignKey(Registro, on_delete=models.CASCADE, related_name='comentarios', )
    comentario = models.CharField(max_length=500, blank=False, verbose_name='Comentar')
    data_2 = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Data')
    autor = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.comentario

    def get_absolute_url(self):
        return reverse('article_list')

