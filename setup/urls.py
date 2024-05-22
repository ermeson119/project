
from django.contrib import admin
from django.urls import path
from todos.views import home, projetos, linkedin,instagram, whatsapp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('projetos/', projetos, name='projetos'),
    path('linkedin/', linkedin, name='linkedin'),
    path('instagram/', instagram, name='instagram'),
    path('whatsapp/', whatsapp, name='whatsapp'),

   
]
