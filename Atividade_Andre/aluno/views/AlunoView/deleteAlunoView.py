# Importa as bibliotecas necessárias
from django.http import Http404  # Importa a exceção Http404
from rest_framework.views import APIView  # Importa a classe base para visualizações da API
from rest_framework.response import Response  # Importa a classe Response para criar respostas da API
from aluno.models.AlunoModel import AlunoModel  # Importa o modelo AlunoModel
from aluno.serializers.AlunoSerializer import AlunoSerializer  # Importa o serializador AlunoSerializer
from rest_framework import status  # Importa os códigos de status HTTP

# Define a classe da visualização DeleteAlunoView, que herda de APIView
class DeleteAlunoView(APIView):
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

    # Define o método DELETE, que lida com a solicitação de exclusão de um aluno
    def delete(self, request, id, format=None):
        # Obtém o aluno com base no ID usando o método get_object
        aluno = self.get_object(id)
        # Exclui o aluno do banco de dados
        aluno.delete()
        # Retorna uma resposta de sucesso com o código 204 (No Content) indicando que o aluno foi excluído
        return Response("Aluno deletado com Sucesso!",status=status.HTTP_204_NO_CONTENT)

        