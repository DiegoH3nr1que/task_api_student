# Importa as bibliotecas necessárias
from django.http import Http404  # Importe a exceção Http404
from rest_framework.views import APIView  # Importe a classe base para visualizações da API
from rest_framework.response import Response  # Importe a classe Response para criar respostas da API
from aluno.models.AlunoModel import AlunoModel  # Importe o modelo AlunoModel
from aluno.serializers.AlunoSerializer import AlunoSerializer  # Importe o serializador AlunoSerializer
from rest_framework import status  # Importe os códigos de status HTTP

# Define a classe da visualização GetAlunoView, que herda de APIView
class GetAlunoView(APIView):
    # Define o método GET, que lida com a solicitação de obtenção de todos os alunos
    def get(self, request, format=None):
        # Obtém todos os alunos do banco de dados
        alunos = AlunoModel.objects.all()
        # Cria um serializador para a lista de alunos e obtém os dados serializados (many=True)
        serializer = AlunoSerializer(alunos, many=True)
        # Retorna uma resposta com os dados serializados de todos os alunos
        return Response(serializer.data)
