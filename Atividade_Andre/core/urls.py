"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# Importação dos endpoints de tarefa
from aluno.views.TarefaView.masterTarefaView import AddTarefaView
from aluno.views.TarefaView.masterTarefaView import DeleteTarefaView
from aluno.views.TarefaView.masterTarefaView import GetTarefaDetailView
from aluno.views.TarefaView.masterTarefaView import GetTarefaView
from aluno.views.TarefaView.masterTarefaView import UpdateTarefaView

# Importação dos endpoints de aluno
from aluno.views.AlunoView.masterAlunoView import AddAlunoView
from aluno.views.AlunoView.masterAlunoView import DeleteAlunoView
from aluno.views.AlunoView.masterAlunoView import GetAlunoDetailView
from aluno.views.AlunoView.masterAlunoView import GetAlunoView
from aluno.views.AlunoView.masterAlunoView import UpdateAlunoView

# Importação dos endpoints de Disciplina
from aluno.views.DisciplinaView.masterDisciplinaView import AddDisciplinaView
from aluno.views.DisciplinaView.masterDisciplinaView import DeleteDisciplinaView
from aluno.views.DisciplinaView.masterDisciplinaView import GetDisciplinaDetailView
from aluno.views.DisciplinaView.masterDisciplinaView import GetDisciplinaView
from aluno.views.DisciplinaView.masterDisciplinaView import UpdateDisciplinaView


urlpatterns = [
    path('admin/', admin.site.urls),
    # urls da tarefa
    path('add_tarefa/', AddTarefaView.as_view(), name='add_tarefa'),
    path('delete_tarefa/<int:id>/', DeleteTarefaView.as_view(), name='delete_tarefa'),
    path('get_tarefa/<int:id>/', GetTarefaDetailView.as_view(), name='get_tarefa_detail'),
    path('get_tarefa/', GetTarefaView.as_view(), name='get_tarefa'),
    path('update_tarefa/<int:id>/', UpdateTarefaView.as_view(), name='update_tarefa'),

    # urls de aluno
    path('add_aluno/', AddAlunoView.as_view(), name='add_aluno'),
    path('delete_aluno/<int:id>/', DeleteAlunoView.as_view(), name='delete_aluno'),
    path('get_aluno/<int:id>/', GetAlunoDetailView.as_view(), name='get_aluno_detail'),
    path('get_aluno/', GetAlunoView.as_view(), name='get_aluno'),
    path('update_aluno/<int:id>/', UpdateAlunoView.as_view(), name='update_aluno'),

    #urls de disciplina
    path('add_disciplina/', AddDisciplinaView.as_view(), name='add_disciplina'),
    path('delete_disciplina/<int:id>/', DeleteDisciplinaView.as_view(), name='delete_disciplina'),
    path('get_disciplina/<int:id>/', GetDisciplinaDetailView.as_view(), name='get_disciplina_detail'),
    path('get_disciplina/', GetDisciplinaView.as_view(), name='get_tarefa'),
    path('update_disciplina/<int:id>/', UpdateDisciplinaView.as_view(), name='update_disciplina'),

]
