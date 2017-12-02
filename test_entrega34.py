def entrega(entrega):
    if entrega == True:
        entrega = 'Parabens voce entregou a tarefa'        
    else:
        entrega = 'Que feio voce nao entregou as tarefas'
    
    return entrega   
    
def test_entrega():
    assert entrega(False) == 'Parabens voce entregou a tarefa'      
  
