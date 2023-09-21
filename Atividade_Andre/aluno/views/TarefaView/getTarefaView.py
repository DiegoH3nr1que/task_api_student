# Importe as bibliotecas necessárias
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from aluno.models import TarefaModel  # Importe o modelo TarefaModel
from aluno.serializers.AlunoSerializer import AlunoSerializer  # Importe os serializadores TarefaSerializer e AlunoSerializer
from aluno.serializers.TarefaSerializer import TarefaSerializer
from aluno.serializers.DisciplinaSerializer import DisciplinaSerializer
from rest_framework import status


# Define a classe da visualização GetTarefaView, que herda de APIView
class GetTarefaView(APIView):
    # Define o método GET, que lida com a solicitação de obtenção de todas as tarefas
    def get(self, request, format=None):
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