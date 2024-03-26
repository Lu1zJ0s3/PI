from django.contrib import admin
from .models import Professor, Disciplina


class ProfessorAdmin(admin.ModelAdmin):
    list_display = 'nome', 'email', 'celular'


class DisciplinaAdmin(admin.ModelAdmin):
    list_display = 'nome', 'carga_horaria', 'codigo'


admin.site.register(Professor, ProfessorAdmin)
admin.site.register(Disciplina, DisciplinaAdmin)
