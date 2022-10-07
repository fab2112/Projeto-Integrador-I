# paginas/urls.py
from django.urls import path
from .views import HomePageView, estatisticasView, sobrenosView, contatoView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('estatisticas', estatisticasView.as_view(), name='estatisticas'),
    path('sobrenos', sobrenosView.as_view(), name='sobrenos'),
    path('contato', contatoView.as_view(), name='contato'),
]

