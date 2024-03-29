from django.shortcuts import render, redirect
from .models import Professor, Disciplina


def index(request):
    return render(request, 'escola.html')


def criar_professor(request):
    nome_prof = request.POST['nome_prof']
    e_mail = request.POST['email']
    cell = request.POST['celular']
    professores = Professor(nome=nome_prof, email=e_mail, celular=cell)
    professores.save()
    return redirect("/listar_professores/")

def apagar_professores(request, id):
    professores = Professor.objects.get(id=id)
    professores.delete()
    return redirect('/listar_professores/')


def criar_disciplina(request):
    nom = request.POST['nome_disci']
    time = request.POST['carga_horaria']
    cod = request.POST['codigo']
    disciplinas = Disciplina(nome=nom, carga_horaria=time, codigo=cod)
    disciplinas.save()
    return redirect("/listar_disciplinas/")

def apagar_disciplinas(request,id):
    disciplinas=Disciplina.objects.get(id=id)
    disciplinas.delete()
    return redirect("/listar_disciplinas/")

def listar_professores(request):
    professores = Professor.objects.all()
    return render(request, 'listar_professores.html', {'professores': professores})


def listar_disciplinas(request):
    disciplinas = Disciplina.objects.all()
    return render(request, 'listar_disciplinas.html', {'disciplinas': disciplinas})
