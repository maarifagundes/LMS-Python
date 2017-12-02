
def prazo(ativo):      
    if ativo == True:
        res_aluno = 'Voce já esta cadastrado'

    else:
        res_aluno = 'Seu usuario não está cadastrado, deseja cadastrar?'
    return res_aluno
    
def test_prazo():
    assert prazo(True) == 'Voce já esta cadastrado'