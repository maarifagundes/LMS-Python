from django.db import models
from core.models import Resposta,Curso,Turma,Resposta,Matricula,Disciplinaofertada,Questao,Aluno
from datetime import datetime

def FazTeste(user):
    
    if Resposta.objects.filter(idaluno=user.ra):
        return " ja fez o teste"
    else:
        return "teste feito"

    
def Aluno_Envia():

    ListaDosQueFizeram = []
    listaNome=[]
    AlunosResponderam = Resposta.objects.all()
    TodosAlunos = Aluno.objects.all()
    for aluno in TodosAlunos:
        for AlunoRespondeu in AlunosResponderam:
            if aluno.id == AlunoRespondeu.raaluno:
                ListaDosQueFizeram.append(aluno.nome)
    return ListaDosQueFizeram

def Alunos_Nao_Mandaram():
    ListaDosQueFizeram = []
    listaNome=[]
    AlunosResponderam = Resposta.objects.all()
    for AlunoRespondeu in AlunosResponderam:
        ListaDosQueFizeram.append(AlunoRespondeu.raaluno)
    TodosAlunos = Aluno.objects.exclude(id__in=ListaDosQueFizeram)
    return TodosAlunos

def VerificaData(Id):
    dataatual= datetime.now()
    ValidaQuestao = Questao.objects.filter(id=2)
    if ValidaQuestao.data > dataatual:
        return print ( "Passou da data limite")
    else:
        return "Resposta"

def VerificaMatricula(Aluno,IdDisciplina):
    Matriculas = Matricula.objects.all()
    Disciplinas = Disciplinaofertada.objects.all()
    turmas = turma.objects.all()
    for matricula in Matriculas:
        for turma in turmas:
            if matricula.idTurma == turma.idTurma:
                if turma.id_disciplinaofertada == IdDisciplina:
                    print("Ja está matriculado na disciplina")
                    break
                else:
                    print ("Matricula aceita!")

def ConstroiMatricula():
    u = Aluno(ra = "1111",nome = "Nikito",email = "nikito@nikito.com",celular = "1111",idcurso = 1)
    u.save()
    return ("Funcionou")