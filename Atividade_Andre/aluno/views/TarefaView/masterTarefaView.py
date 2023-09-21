from aluno.views.TarefaView.addTarefaView import AddTarefaView
from aluno.views.TarefaView.deleteTarefaView import DeleteTarefaView
from aluno.views.TarefaView.getTarefaDetailView import GetTarefaDetailView
from aluno.views.TarefaView.getTarefaView import GetTarefaView
from aluno.views.TarefaView.updateTarefaView import UpdateTarefaView

class MasterTarefaView(
    AddTarefaView,
    DeleteTarefaView,
    GetTarefaDetailView,
    GetTarefaView,
    UpdateTarefaView
):
    pass