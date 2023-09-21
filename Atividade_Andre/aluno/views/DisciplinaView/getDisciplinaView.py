# Importa as bibliotecas necessárias
from django.http import Http404  # Importe a exceção Http404
from rest_framework.views import APIView  # Importe a classe base para visualizações da API
from rest_framework.response import Response  # Importe a classe Response para criar respostas da API
from aluno.models.DisciplinaModel import DisciplinaModel  # Importe o modelo DisciplinaModel
from aluno.serializers.DisciplinaSerializer import DisciplinaSerializer  # Importe o serializador DisciplinaSerializer
from rest_framework import status  # Importe os códigos de status HTTP

# Define a classe da visualização GetDisciplinaView, que herda de APIView
class GetDisciplinaView(APIView):
    # Define o método GET, que lida com a solicitação de obtenção de todas as disciplinas
    def get(self, request, format=None):
        # Obtém todas as disciplinas do banco de dados
        disciplina = DisciplinaModel.objects.all()
        
        # Cria um serializador para a lista de disciplinas e obtém os dados serializados (many=True)
        serializer = DisciplinaSerializer(disciplina, many=True)
        
        # Retorna uma resposta com os dados serializados de todas as disciplinas
        return Response(serializer.data)
