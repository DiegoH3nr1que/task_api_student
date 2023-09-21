# Importa as bibliotecas necessárias
from django.http import Http404  # Importe a exceção Http404
from rest_framework.views import APIView  # Importe a classe base para visualizações da API
from rest_framework.response import Response  # Importe a classe Response para criar respostas da API
from aluno.models.AlunoModel import AlunoModel  # Importe o modelo AlunoModel
from aluno.serializers.AlunoSerializer import AlunoSerializer  # Importe o serializador AlunoSerializer
from rest_framework import status  # Importe os códigos de status HTTP

# Define a classe da visualização UpdateAlunoView, que herda de APIView
class UpdateAlunoView(APIView):
    # Define o método get_object para obter um aluno com base em um ID
    def get_object(self, id):
        try:
            # Tenta buscar um aluno no banco de dados com o ID fornecido
            return AlunoModel.objects.get(id=id)
        except AlunoModel.DoesNotExist:
            # Se o aluno não existe, levanta a exceção Http404
            raise Http404

    # Define o método GET, que lida com a solicitação de obtenção de detalhes de um aluno
    def get(self, request, id, format=None):
        # Obtém o aluno com base no ID usando o método get_object
        aluno = self.get_object(id)
        # Cria um serializador para o aluno e obtém os dados serializados
        serializer = AlunoSerializer(aluno)
        # Retorna uma resposta com os dados do aluno
        return Response(serializer.data)

    # Define o método PUT, que lida com a atualização de um aluno com base no ID
    def put(self, request, id, format=None):
        # Obtém o aluno com base no ID usando o método get_object
        aluno = self.get_object(id)
        # Cria um serializador para o aluno com os dados recebidos na requisição
        serializer = AlunoSerializer(aluno, data=request.data)
        
        # Verifica se os dados fornecidos são válidos de acordo com as regras do AlunoSerializer
        if (serializer.is_valid()):
            # Se os dados são válidos, atualiza o aluno no banco de dados
            serializer.save()
            # Retorna uma resposta com os dados atualizados do aluno
            return Response(serializer.data)
        # Se os dados não são válidos, retorna uma resposta de erro (código 400 - Bad Request)
        # com os erros de validação do serializer
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
