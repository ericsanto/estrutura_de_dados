def verifica_parenteses(expressao):
    pilha = []
    for char in expressao:
        if char == '(':
            pilha.append(char)
        elif char == ')':
            if not pilha or pilha.pop() != '(':
                return False
    return len(pilha) == 0


    

expressao1 = "((2 + 3) * 5)"
result = verifica_parenteses(expressao1)
print(result)

expressao2 = ")(2 + 3) * 5("
result2 = verifica_parenteses(expressao2) 
print(result)