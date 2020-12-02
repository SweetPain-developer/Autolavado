from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Productos
from .validators import MaxSizeDocumentValidator

class CustomUserCreationForm(UserCreationForm):

    first_name = forms.CharField(min_length=3, max_length=80)
    last_name = forms.CharField(min_length=3, max_length=80)

    class Meta:
        model = User
        fields = ['username', "first_name", "last_name", "email", "password1", "password2"]

class ProductosFrom(forms.ModelForm):

    nombre = forms.CharField(min_length=3, max_length=120)
    imagen = forms.ImageField(required=False, validators=[MaxSizeDocumentValidator])
    precio = forms.IntegerField(min_value=1, max_value=1500000)

    class Meta:
        model = Productos
        fields = '__all__'