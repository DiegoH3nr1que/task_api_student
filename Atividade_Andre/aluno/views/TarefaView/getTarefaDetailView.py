# Importa as bibliotecas necessárias
from django.http import Http404  # Importe a exceção Http404
from rest_framework.views import APIView  # Importe a classe base para visualizações da API
from rest_framework.response import Response
from aluno.serializers.DisciplinaSerializer import DisciplinaSerializer
from aluno.serializers.AlunoSerializer import AlunoSerializer  # Importe a classe Response para criar respostas da API
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
       # Obtém todas as tarefas do banco de dados
        tarefas = TarefaModel.objects.all()
        
        # Crie uma lista para armazenar os dados de tarefas com informações do aluno e da disciplina
        tarefas_com_aluno_e_disciplina = []

        # Itere sobre as tarefas e adicione informações do aluno e da disciplina
        for tarefa in tarefas:
            aluno = tarefa.aluno
            disciplinas = tarefa.disciplinas.all()  # Assumindo que uma tarefa pode ter várias disciplinas
            aluno_serializer = AlunoSerializer(aluno)
            disciplina_serializer = DisciplinaSerializer(disciplinas, many=True)  # Use many=True para serializar várias disciplinas
            tarefa_serializer = TarefaSerializer(tarefa)
            tarefa_data = tarefa_serializer.data
            tarefa_data['aluno'] = aluno_serializer.data
            tarefa_data['disciplinas'] = disciplina_serializer.data
            tarefas_com_aluno_e_disciplina.append(tarefa_data)

        # Retorna uma resposta com os dados serializados de todas as tarefas, incluindo informações do aluno e da disciplina
        return Response(tarefas_com_aluno_e_disciplina)
