# Registros/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Registro

"""class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Registro
        fields = ('instituicao',)  # new"""


