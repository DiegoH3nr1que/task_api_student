# Importa as bibliotecas necessárias
from django.http import Http404  # Importe a exceção Http404
from rest_framework.views import APIView  # Importe a classe base para visualizações da API
from rest_framework.response import Response  # Importe a classe Response para criar respostas da API
from aluno.serializers.TarefaSerializer import TarefaSerializer  # Importe o serializador TarefaSerializer
from rest_framework import status  # Importe os códigos de status HTTP

# Define a classe da visualização AddTarefaView, que herda de APIView
class AddTarefaView(APIView):
    # Define o método POST, que lida com a criação de uma nova tarefa
    def post(self, request, format=None):
        # Cria uma instância do TarefaSerializer com os dados recebidos na requisição
        serializer = TarefaSerializer(data=request.data)
        
        # Verifica se os dados fornecidos são válidos de acordo com as regras do TarefaSerializer
        if (serializer.is_valid()):
            # Se os dados são válidos, salva a tarefa no banco de dados
            serializer.save()
            # Retorna uma resposta de sucesso (código 201 - Created) com os dados da tarefa
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # Se os dados não são válidos, retorna uma resposta de erro (código 400 - Bad Request)
        # com os erros de validação do serializer
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

