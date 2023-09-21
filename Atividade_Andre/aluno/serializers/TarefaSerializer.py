from rest_framework import serializers
from aluno.models.TarefaModel import TarefaModel

class TarefaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TarefaModel
        fields = "__all__"

class TarefaParcialSerializer(serializers.ModelSerializer):
    class Meta:
        model = TarefaModel
        fields = ['titulo', 'descricao', 'data_entrega', 'concluida']        