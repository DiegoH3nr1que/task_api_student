from django.db import models
from aluno.models.AlunoModel import AlunoModel  # Importe o modelo AlunoModel corretamente
from aluno.models.DisciplinaModel import DisciplinaModel  # Importe o modelo DisciplinaModel corretamente

class TarefaModel(models.Model):  # Corrija o nome da classe para TarefaModel
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    data_entrega = models.DateField()
    concluida = models.BooleanField(default=False)
    aluno = models.ForeignKey(AlunoModel, on_delete=models.CASCADE) 
    disciplinas = models.ManyToManyField(DisciplinaModel)

    def __str__(self):
        return "Tarefa [%s]" % self.titulo
  