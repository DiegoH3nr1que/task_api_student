from rest_framework import serializers
from aluno.models.AlunoModel import AlunoModel

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlunoModel
        fields = "__all__"
        
