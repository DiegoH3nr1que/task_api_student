from django.db import models


class AlunoModel(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True)


    def __srt__(self):
        return "Alunos [%s]" % (self.id, self.name, self.email)    