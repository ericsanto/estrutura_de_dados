from row import Queues
import time


time_start = time.time()

def queue_order(queue: Queues):
    list_temporary  = []

    while not queue.is_empty():
        list_temporary = list_temporary + [queue.top()]
        queue.dequeue()

    while list_temporary:
        smaller = list_temporary[0]

        for i in list_temporary:
            print(i)
            if i > smaller:
                smaller = i
                print('/',smaller)
        
        queue.push(smaller)
        list_temporary.remove(smaller)

    del list_temporary

    return queue.output()



queue1 = Queues()
queue1.push(4)
queue1.push(1)
queue1.push(9)
queue1.push(5)
queue1.push(2)
queue1.push(7)
print(f'Fila desordenada: {queue1.output()}')

result = queue_order(queue1)


print(f'Fila ordenada: {result}')
time_finish = time.time()

print(f'TEMPO DE EXECUÇÃO DO ALGORITIMO {time_finish - time_start}')
