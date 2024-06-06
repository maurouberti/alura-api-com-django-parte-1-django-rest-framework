from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=100, blank=False, null=False)
    rg = models.CharField(max_length=20)
    cpf = models.CharField(max_length=11)
    nascimento = models.DateField()
    
    def __str__(self):
        return self.nome

class Curso(models.Model):
    NIVEL = (
        ('B', 'Básico'),
        ('I', 'Intermediário'),
        ('A', 'Avançado')
    )
    codigo = models.CharField(max_length=10, blank=False, null=False)
    descricao = models.CharField(max_length=100, blank=False, null=False)
    nivel = models.CharField(max_length=1, choices=NIVEL, blank=False, null=False, default='B')

    def __str__(self):
        return self.descricao

class Matricula(models.Model):
    PERIODO = (
        ('M', 'Matutino'),
        ('V', 'Vespertino'),
        ('N', 'Noturno')
    )
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    periodo = models.CharField(max_length=1, choices=PERIODO, blank=False, null=False, default='M')

    def __str__(self):
        return f"{self.aluno} {self.curso}"
