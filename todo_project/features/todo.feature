Feature: Todo List
    Scenario: Criar uma todo list
        Given Que eu esteja na página "todo"
        When Criar um todo
            """
            {
                "nome": "Dormir",
                "descricao": "é bom"
            }
            """
        Then o todo dever estar na planilha "A fazer"