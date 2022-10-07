# Registros/urls.py
from django.urls import path
from .views import RegistroListView, RegistroUpdateView, RegistroDetailView, RegistroDeleteView, RegistroCreateView,\
	RegistroCommentView, ComentarioDeleteView


urlpatterns = [
	path('<int:pk>/edit/', RegistroUpdateView.as_view(), name='article_edit'),
	path('<int:pk>/', RegistroDetailView.as_view(), name='article_detail'),
	path('<int:pk>/delete/', RegistroDeleteView.as_view(), name='article_delete'),
	path('', RegistroListView.as_view(), name='article_list'),
	path('new/', RegistroCreateView.as_view(), name='article_new'),
	path('<int:pk>/comentario/', RegistroCommentView.as_view(), name='article_comment'),
	path('<int:pk>/comentario/delete/', ComentarioDeleteView.as_view(), name='comment_delete'),]
