# paginas/views.py
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'

class estatisticasView(TemplateView):
    template_name = 'estatisticas.html'

class sobrenosView(TemplateView):
    template_name = 'sobrenos.html'

class contatoView(TemplateView):
    template_name = 'contato.html'
