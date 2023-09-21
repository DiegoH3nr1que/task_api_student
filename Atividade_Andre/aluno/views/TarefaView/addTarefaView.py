# Importe as bibliotecas necessárias
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from aluno.models import AlunoModel, TarefaModel, DisciplinaModel  # Importe os modelos AlunoModel, TarefaModel e DisciplinaModel
from aluno.serializers.TarefaSerializer import TarefaSerializer
from aluno.serializers.AlunoSerializer import AlunoSerializer  # Importe o serializador AlunoSerializer
from rest_framework import status

# Define a classe da visualização AddTarefaView, que herda de APIView
class AddTarefaView(APIView):
    # Define o método POST, que lida com a criação de uma nova tarefa
    def post(self, request, format=None):
        # Cria uma instância do TarefaSerializer com os dados recebidos na requisição
        serializer = TarefaSerializer(data=request.data)

        # Verifica se os dados fornecidos são válidos de acordo com as regras do TarefaSerializer
        if serializer.is_valid():
            # Se os dados são válidos, salva a tarefa no banco de dados
            tarefa = serializer.save()

            # Recupere os IDs dos cursos associados à tarefa
            cursos_ids = tarefa.disciplinas.values_list('id', flat=True)

            # Recupere os objetos completos dos cursos com base nos IDs
            cursos = DisciplinaModel.objects.filter(id__in=cursos_ids)

            # Recupere o objeto completo do aluno
            aluno = AlunoModel.objects.get(id=tarefa.aluno.id)

            # Serializa o aluno para incluí-lo na resposta
            aluno_serializer = AlunoSerializer(aluno)

            # Adicione os objetos de cursos e o aluno à resposta da tarefa
            tarefa_data = serializer.data
            tarefa_data['disciplinas'] = [{"id": curso.id, "nome": curso.nome} for curso in cursos]
            tarefa_data['aluno'] = aluno_serializer.data

            # Retorna uma resposta de sucesso (código 201 - Created) com os dados da tarefa
            return Response(tarefa_data, status=status.HTTP_201_CREATED)
        
        # Se os dados não são válidos, retorna uma resposta de erro (código 400 - Bad Request)
        # com os erros de validação do serializer
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
