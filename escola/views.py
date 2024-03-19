from django.shortcuts import render, redirect
from .models import Professor
from .forms import ProfessorForm, DisciplinaForm


def index(request):
    professores = Professor.objects.all()
    return render(request, 'escola.html', {'professores': professores})


def criar_professor(request):
    if request.method == 'POST':
        form = ProfessorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ProfessorForm()
    return render(request, 'escola.html', {'form': form})


def criar_disciplina(request):
    if request.method == 'POST':
        form = DisciplinaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = DisciplinaForm()
    return render(request, 'escola.html', {'form': form})
