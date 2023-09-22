# Importa as bibliotecas necessárias
from django.http import Http404  # Importe a exceção Http404
from rest_framework.views import APIView  # Importe a classe base para visualizações da API
from rest_framework.response import Response  # Importe a classe Response para criar respostas da API
from aluno.models.DisciplinaModel import DisciplinaModel  # Importe o modelo DisciplinaModel
from aluno.serializers.DisciplinaSerializer import DisciplinaSerializer  # Importe o serializador DisciplinaSerializer
from rest_framework import status  # Importe os códigos de status HTTP

# Define a classe da visualização DeleteDisciplinaView, que herda de APIView
class DeleteDisciplinaView(APIView):
    # Define o método get_object para obter uma disciplina com base em um ID
    def get_object(self, id):
        try:
            # Tenta buscar uma disciplina no banco de dados com o ID fornecido
            return DisciplinaModel.objects.get(id=id)
        except DisciplinaModel.DoesNotExist:
            # Se a disciplina não existe, levanta a exceção Http404
            raise Http404
        
    # Define o método GET, que lida com a solicitação de obtenção de detalhes de uma disciplina
    def get(self, request, id, format=None):
        # Obtém a disciplina com base no ID usando o método get_object
        disciplina = self.get_object(id)
        # Cria um serializador para a disciplina e obtém os dados serializados
        serializer = DisciplinaSerializer(disciplina)
        # Retorna uma resposta com os dados da disciplina
        return Response(serializer.data)    
    # Define o método DELETE, que lida com a solicitação de exclusão de uma disciplina
    def delete(self, request, id, format=None):
        # Obtém a disciplina com base no ID usando o método get_object
        disciplina = self.get_object(id)
        # Exclui a disciplina do banco de dados
        disciplina.delete()
        # Retorna uma resposta de sucesso com o código 204 (No Content) indicando que a disciplina foi excluída
        return Response("Disciplina deletada com sucessso!",status=status.HTTP_204_NO_CONTENT)
