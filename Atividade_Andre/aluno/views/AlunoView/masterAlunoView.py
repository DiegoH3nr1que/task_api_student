from aluno.views.AlunoView.addAlunoView import AddAlunoView
from aluno.views.AlunoView.deleteAlunoView import DeleteAlunoView
from aluno.views.AlunoView.getAlunoDetailView import GetAlunoDetailView
from aluno.views.AlunoView.getAlunoView import GetAlunoView
from aluno.views.AlunoView.updateAlunoView import UpdateAlunoView

class MasterAlunoView(
    AddAlunoView,
    DeleteAlunoView,
    GetAlunoDetailView,
    GetAlunoView,
    UpdateAlunoView
):
    pass