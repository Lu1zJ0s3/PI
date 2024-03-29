from django.db import models


class Professor(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    celular = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Disciplina(models.Model):
    nome = models.CharField(max_length=50)
    professor = models.ManyToManyField(Professor)
    carga_horaria = models.IntegerField()

    def __str__(self):
        return self.nome
