from rest_framework import serializers
from aluno.models.DisciplinaModel import DisciplinaModel

class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DisciplinaModel
        fields = "__all__"
        