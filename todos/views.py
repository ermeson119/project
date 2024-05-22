from django.shortcuts import render, redirect

def home(request):
    return render(request, 'todos/home.html')

def projetos(request):
    return render(request, 'todos/projetos.html')

def linkedin(request):
    linkedin = 'https://www.linkedin.com/in/ermeson-balbinot/'
    return redirect(linkedin)

def instagram(request):
    instagram = 'https://www.instagram.com/ermesonbalbinot/'
    return redirect(instagram)

def whatsapp(request):
    whatsapp = 'https://wa.me/qr/OKMH27RO567BB1'
    return redirect(whatsapp)

