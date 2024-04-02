from row import Queues


queue = Queues()
queue.push(5)
queue.push(8)
queue.push(11)
queue.push(157)

def reverse_queue(queue: Queues):
    list_temporary = []

    while not queue.is_empty():
        element = queue.top()
        queue.dequeue()
        list_temporary = [element] + list_temporary
    
    for i in list_temporary:
        queue.push(i)
    
    del list_temporary

    return queue

queue1 = reverse_queue(queue)
print(queue1.output())




