from row import Queues


"""def quick_sort(array: list) -> list:
    size_array = len(array)
    if size_array <= 1:
        return array

    pivo =  array[-1]
    smalls_numbers_in_array = []
    bigs_numbers_in_array =  []
    for x in array[:-1]:
        if x <= pivo:
            smalls_numbers_in_array = [x] + smalls_numbers_in_array
        else:
            bigs_numbers_in_array = [x] + bigs_numbers_in_array
        
    return quick_sort(smalls_numbers_in_array) + [pivo] + quick_sort(bigs_numbers_in_array)"""
      




def quick_sort_queue(queue: Queues) -> Queues:
    size_queue = queue.len()
    if size_queue <= 1:
        return queue

    pivot = queue.top()
    smalls_numbers_in_queue = []
    bigs_numbers_in_queue =  []

    while not queue.is_empty():
        if queue.top() <= pivot:
            smalls_numbers_in_queue = [queue.top()] +  smalls_numbers_in_queue
        else:
            bigs_numbers_in_queue = [queue.top()] + bigs_numbers_in_queue
        
        queue.dequeue()

    return quick_sort_queue(smalls_numbers_in_queue) + [pivot] + quick_sort_queue(bigs_numbers_in_queue)


queue = Queues()
queue.push(7)
queue.push(1)
queue.push(3)
queue.push(50)
queue.push(100)
result = quick_sort_queue(queue)
print(result)
print(queue.output())
