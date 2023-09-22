# Importa as bibliotecas necessárias
from django.http import Http404  # Importe a exceção Http404
from rest_framework.views import APIView  # Importe a classe base para visualizações da API
from rest_framework.response import Response  # Importe a classe Response para criar respostas da API
from aluno.models.TarefaModel import TarefaModel  # Importe o modelo TarefaModel
from aluno.serializers.TarefaSerializer import TarefaParcialSerializer, TarefaSerializer  # Importe os serializadores TarefaParcialSerializer e TarefaSerializer
from aluno.models.DisciplinaModel import DisciplinaModel
from aluno.models.AlunoModel import AlunoModel
from aluno.serializers.AlunoSerializer import AlunoSerializer
from rest_framework import status  # Importe os códigos de status HTTP

# Define a classe da visualização UpdateTarefaView, que herda de APIView
class UpdateTarefaView(APIView):
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
        # Obtém a tarefa com base no ID usando o método get_object
        tarefa = self.get_object(id)
        
        # Cria um serializador completo (TarefaSerializer) para a tarefa e obtém os dados serializados
        serializer = TarefaSerializer(tarefa)
        
        # Retorna uma resposta com os dados da tarefa
        return Response(serializer.data)

    # Define o método PUT, que lida com a atualização parcial de uma tarefa com base no ID
    def put(self, request, id, format=None):
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
