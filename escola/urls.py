from django.contrib import admin
from django.urls import path
from escola import views

urlpatterns = [
    path('criar_professor/', views.criar_professor, name='criar_professor'),
    path('criar_disciplina/', views.criar_disciplina, name='criar_disciplina'),
    path('listar_professores/', views.listar_professores, name='listar_professores'),
    path('listar_disciplinas/', views.listar_disciplinas, name='listar_disciplinas'),
    path('apagar_disciplinas/<int:id>/', views.apagar_disciplinas, name='apagar_disciplinas'),
    path('apagar_professores/<int:id>/', views.apagar_professores, name = 'apagar_professores'), 
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
]
