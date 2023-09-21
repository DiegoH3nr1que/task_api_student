# Importa as bibliotecas necessárias
from django.http import Http404  # Importe a exceção Http404
from rest_framework.views import APIView  # Importe a classe base para visualizações da API
from rest_framework.response import Response  # Importe a classe Response para criar respostas da API
from aluno.models.DisciplinaModel import DisciplinaModel  # Importe o modelo DisciplinaModel
from aluno.serializers.DisciplinaSerializer import DisciplinaSerializer  # Importe o serializador DisciplinaSerializer
from rest_framework import status  # Importe os códigos de status HTTP

# Define a classe da visualização GetDisciplinaDetailView, que herda de APIView
class GetDisciplinaDetailView(APIView):
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
