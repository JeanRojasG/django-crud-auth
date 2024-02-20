from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def bienvenidos(request):
      return render(request, 'singup.html',{
        'form': UserCreationForm
    })