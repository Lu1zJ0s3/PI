from django.contrib import admin
from django.urls import path
from escola import views

urlpatterns = [
    path('criar_prof/', views.criar_professor, name='criar_professor'),
    path('criar_disci/', views.criar_disciplina, name='criar_disciplina'),
    path('listar_professores/', views.listar_professores, name='listar_profs'),
    path('listar_disciplina/', views.listar_disciplinas, name='listar_disci'),
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
]
