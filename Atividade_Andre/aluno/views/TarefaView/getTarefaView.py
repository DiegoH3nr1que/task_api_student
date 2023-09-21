# Importa as bibliotecas necessárias
from django.http import Http404  # Importe a exceção Http404
from rest_framework.views import APIView  # Importe a classe base para visualizações da API
from rest_framework.response import Response  # Importe a classe Response para criar respostas da API
from aluno.models.TarefaModel import TarefaModel  # Importe o modelo TarefaModel
from aluno.serializers.TarefaSerializer import TarefaSerializer  # Importe o serializador TarefaSerializer
from rest_framework import status  # Importe os códigos de status HTTP

# Define a classe da visualização GetTarefaView, que herda de APIView
class GetTarefaView(APIView):
    # Define o método GET, que lida com a solicitação de obtenção de todas as tarefas
    def get(self, request, format=None):
        # Obtém todas as tarefas do banco de dados
        tarefa = TarefaModel.objects.all()
        # Cria um serializador para a lista de tarefas e obtém os dados serializados (many=True)
        serializer = TarefaSerializer(tarefa, many=True)
        # Retorna uma resposta com os dados serializados de todas as tarefas
        return Response(serializer.data)
