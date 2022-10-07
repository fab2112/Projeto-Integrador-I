# Registros/views.py
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Registro, Comentario


class RegistroListView(LoginRequiredMixin, ListView):
    model = Registro
    template_name = 'registro_listagem.html'
    login_url = 'login'

class RegistroDetailView(LoginRequiredMixin, DetailView):
    model = Registro
    template_name = 'article_detail.html'
    login_url = 'login'


class RegistroUpdateView(LoginRequiredMixin, UpdateView):
    model = Registro
    fields = ('doacao', 'contato', 'endereco', 'obs', 'instituicao')
    template_name = 'registro_edicao.html'
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.doador != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class RegistroCommentView(LoginRequiredMixin, CreateView):
    model = Comentario
    fields = ('comentario',)
    template_name = 'registro_comentario.html'
    login_url = 'login'

    def form_valid(self, form):
        form.instance.autor = self.request.user
        form.instance.registro_id = self.kwargs['pk']
        return super().form_valid(form)


class ComentarioDeleteView(LoginRequiredMixin, DeleteView):
    model = Comentario
    template_name = 'comentario_delecao.html'
    success_url = reverse_lazy('article_list')
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.autor != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class RegistroDeleteView(LoginRequiredMixin, DeleteView):
    model = Registro
    template_name = 'registro_delecao.html'
    success_url = reverse_lazy('article_list')
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.doador != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class RegistroCreateView(LoginRequiredMixin, CreateView):
    model = Registro
    template_name = 'registro_novo.html'
    fields = ('doacao', 'contato', 'endereco', 'obs', 'instituicao')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.doador = self.request.user
        return super().form_valid(form)
        
        
