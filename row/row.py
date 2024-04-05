class Queues:
    def __init__(self):
        self.queue = []
        self.size = 0

    def push(self, data):
        self.queue = [data] + self.queue
        self.size += 1

    def is_empty(self):
        if self.size == 0:
            return True
        return False

    def dequeue(self):
        if self.size > 0:
            self.queue = self.queue[1:]
            self.size -= 1
        return None

    def top(self):
        return self.queue[0]

    def len(self):
        return self.size
    
    def output(self):
        return self.queue
        


queue = Queues()

#INSERINDO VALORES NA FILA
queue.push(9)
queue.push(8)
queue.push(10)
queue.push(1)
queue.push(-1)

"""#CONSULTANDO TAMANHO DA FILA
print(f'O tamanho da fila é: {queue.len()}')

#VERIFICANDO O PRIMEIRO ELEMENTO DA FILA
print(f'O primeiro elemento da fila é: {queue.top()}')

#VERIFICANDO SE A FILA ESTÁ VAZIA
if not queue.is_empty():
    print('A fila não está  vazia')
else:
    print('A fila está vazia')

#DESENFILEIRANDO
queue.dequeue()

#RETORNANDO TODA A FILA
print(queue.output())"""
