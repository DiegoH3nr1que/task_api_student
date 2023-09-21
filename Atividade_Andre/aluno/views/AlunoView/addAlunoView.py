# Importa as bibliotecas necessárias
from django.http import Http404  # Importa a exceção Http404
from rest_framework.views import APIView  # Importa a classe base para visualizações da API
from rest_framework.response import Response  # Importa a classe Response para criar respostas da API
from aluno.serializers.AlunoSerializer import AlunoSerializer  # Importa o serializador AlunoSerializer
from rest_framework import status  # Importa os códigos de status HTTP

# Define a classe da visualização AddAlunoView, que herda de APIView
class AddAlunoView(APIView):
    # Define o método POST, que lida com a criação de um novo aluno
    def post(self, request, format=None):
        # Cria uma instância do AlunoSerializer com os dados recebidos na requisição
        serializer = AlunoSerializer(data=request.data)
        
        # Verifica se os dados fornecidos são válidos de acordo com as regras do AlunoSerializer
        if (serializer.is_valid()):
            # Se os dados são válidos, salva o aluno no banco de dados
            serializer.save()
            
            # Retorna uma resposta de sucesso (código 201 - Created) com os dados do aluno
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        # Se os dados não são válidos, retorna uma resposta de erro (código 400 - Bad Request)
        # com os erros de validação do serializer
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

