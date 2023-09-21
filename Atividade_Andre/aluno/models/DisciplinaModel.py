from django.db import models


class DisciplinaModel(models.Model):
    nome = models.CharField(max_length=200, unique=True)
    descricao = models.CharField(max_length=200)


    def __srt__(self):
        return "Disciplina [%s]" % (self.name, self.descricao)

