# Importa as bibliotecas necessárias
from django.http import Http404  # Importe a exceção Http404
from rest_framework.views import APIView  # Importe a classe base para visualizações da API
from rest_framework.response import Response  # Importe a classe Response para criar respostas da API
from aluno.serializers.DisciplinaSerializer import DisciplinaSerializer  # Importe o serializador DisciplinaSerializer
from rest_framework import status  # Importe os códigos de status HTTP

# Define a classe da visualização AddDisciplinaView, que herda de APIView
class AddDisciplinaView(APIView):
    # Define o método POST, que lida com a criação de uma nova disciplina
    def post(self, request, format=None):
        # Cria uma instância do DisciplinaSerializer com os dados recebidos na requisição
        serializer = DisciplinaSerializer(data=request.data)
        # Verifica se os dados fornecidos são válidos de acordo com as regras do DisciplinaSerializer
        if (serializer.is_valid()):
            # Se os dados são válidos, salva a disciplina no banco de dados
            serializer.save()
            # Retorna uma resposta de sucesso (código 201 - Created) com os dados da disciplina
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # Se os dados não são válidos, retorna uma resposta de erro (código 400 - Bad Request)
        # com os erros de validação do serializer
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
