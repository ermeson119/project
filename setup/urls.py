
from django.contrib import admin
from django.urls import path
from todos.views import home, projetos, skills, cursando

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('projetos/', projetos, name='projetos'),
    path('skills/', skills, name='skills'),
    path('cursando/', cursando, name='cursando'),
]
