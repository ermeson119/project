from django.shortcuts import render

def home(request):
    return render(request, 'todos/home.html')

def projetos(request):
    return render(request, 'todos/projetos.html')