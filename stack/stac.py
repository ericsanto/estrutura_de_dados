class Stack:
    def __init__(self):
        self.stack = []
        self.quantity_data = 0

    def insert(self, data)-> None:
        self.stack += [data]
        self.quantity_data += 1

    def pop(self):
        if self.quantity_data > 0:
            self.stack = self.stack[:-1]
            self.quantity_data -= 1
        return None

    def is_empty(self) -> bool:
        if self.quantity_data == 0:
            return True
        return False

    def top(self)-> int or None:
        if self.quantity_data > 0:
            return self.stack[self.quantity_data - 1]
        return None

    def len(self)-> int:
        return self.quantity_data

    def output(self)-> list:
        return self.stack


#INSTANCIANDO A CLASSE
"""tack = Stack()

#INSERINDO DADOS
stack.insert(8)
stack.insert(5)
stack.insert(20)
stack.insert(50)
stack.insert(1)
stack.insert(18)
stack.insert(120)
stack.insert(-1)

#MOSTRANDO PILHA NA TELA
print(stack.output())

#ACESSANDO O TAMANHO DA PILHA
print(stack.len())

#ACESSANDO O ÚTLIMO ELEMENTO DA LISTA SEM REMOVÊ-LO
print(stack.top())

#VERIFICANDO SE A PILHA ESTÁ VAZIA
print(stack.is_empty())


def sorted_stack(pilha: list):
    lista_temporaria = Stack()

    while not pilha.is_empty():
        element = pilha.top() 
        print(element)
        pilha.pop()
        while not lista_temporaria.is_empty() and lista_temporaria.top() > element:
            pilha.insert(lista_temporaria.top())
            lista_temporaria.pop()
        lista_temporaria.insert(element)
    return lista_temporaria.output()

stack_ord = sorted_stack(stack)
print(stack_ord)"""