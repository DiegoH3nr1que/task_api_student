# Importa as bibliotecas necessárias
from django.http import Http404  # Importe a exceção Http404
from rest_framework.views import APIView  # Importe a classe base para visualizações da API
from rest_framework.response import Response  # Importe a classe Response para criar respostas da API
from aluno.models.TarefaModel import TarefaModel  # Importe o modelo TarefaModel
from aluno.serializers.TarefaSerializer import TarefaSerializer  # Importe o serializador TarefaSerializer
from rest_framework import status  # Importe os códigos de status HTTP

# Define a classe da visualização GetTarefaDetailView, que herda de APIView
class GetTarefaDetailView(APIView):
    # Define o método get_object para obter uma tarefa com base em um ID
    def get_object(self, id):
        try:
            # Tenta buscar uma tarefa no banco de dados com o ID fornecido
            return TarefaModel.objects.get(id=id)
        except TarefaModel.DoesNotExist:
            # Se a tarefa não existe, levanta a exceção Http404
            raise Http404

    # Define o método GET, que lida com a solicitação de obtenção de detalhes de uma tarefa
    def get(self, request, id, format=None):
        # Obtém a tarefa com base no ID usando o método get_object
        tarefa = self.get_object(id)
        
        # Cria um serializador para a tarefa e obtém os dados serializados
        serializer = TarefaSerializer(tarefa)
        
        # Retorna uma resposta com os dados da tarefa
        return Response(serializer.data)
