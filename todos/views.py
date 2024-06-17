from django.shortcuts import render, redirect

def home(request):
    return render(request, 'todos/home.html')

def projetos(request):
    return render(request, 'todos/projetos.html')

def skills(request):
    return render(request, 'todos/skills.html')

def cursando(request):
    return render(request, 'todos/cursando.html')

