class Stack:
    def __init__(self):
        self.stack = []
        self.quantity_data = 0

    def insert(self, data)-> None:
        self.stack += [data]
        self.quantity_data += 1

    def pop(self)-> None:
        if self.quantity_data > 0:
            self.stack = self.stack[:-1]
            self.quantity_data -= 1

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
stack = Stack()

#INSERINDO DADOS
stack.insert(8)
stack.insert(5)
stack.insert(20)
stack.insert(50)

#MOSTRANDO PILHA NA TELA
print(stack.output())

#ACESSANDO O TAMANHO DA PILHA
print(stack.len())

#ACESSANDO O ÚTLIMO ELEMENTO DA LISTA SEM REMOVÊ-LO
print(stack.top())

#VERIFICANDO SE A PILHA ESTÁ VAZIA
print(stack.is_empty())

