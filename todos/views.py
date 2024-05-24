from django.shortcuts import render, redirect

def home(request):
    return render(request, 'todos/home.html')

def projetos(request):
    return render(request, 'todos/projetos.html')

def linkedin(request):
    link_linkedin = 'https://www.linkedin.com/in/ermeson-balbinot/'
    return redirect(link_linkedin)

def instagram(request):
    link_instagram = 'https://www.instagram.com/ermesonbalbinot/'
    return redirect(link_instagram)

def whatsapp(request):
    link_whatsapp = 'https://wa.me/qr/OKMH27RO567BB1'
    return redirect(link_whatsapp)

def skills(request):
    return render(request, 'todos/skills.html')

