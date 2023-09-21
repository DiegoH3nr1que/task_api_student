from aluno.views.DisciplinaView.addDisciplinaView import AddDisciplinaView
from aluno.views.DisciplinaView.deleteDisciplinaView import DeleteDisciplinaView
from aluno.views.DisciplinaView.getDisciplinaDetailView import GetDisciplinaDetailView
from aluno.views.DisciplinaView.getDisciplinaView import GetDisciplinaView
from aluno.views.DisciplinaView.updateDisciplinaView import UpdateDisciplinaView

class MasterDisciplinaView(
    AddDisciplinaView,
    DeleteDisciplinaView,
    GetDisciplinaDetailView,
    GetDisciplinaView,
    UpdateDisciplinaView
):
    pass