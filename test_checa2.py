def checa_test(test):
    if test == True:
        aluno = 'voce ja fez o teste'
        
        
    else:
        aluno = 'voce não fez o teste'
    return aluno   
    
def test_checa_teste():
    assert checa_test(True) == 'voce ja fez o teste'
  

 