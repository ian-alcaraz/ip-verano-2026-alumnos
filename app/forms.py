from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class registroUsuarioForm (UserCreationForm):  # hereda las funciones de userCreationForms
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']

