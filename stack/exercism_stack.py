from stac import Stack

stack1 = Stack()

stack1.insert(12)
stack1.insert(5)
stack1.insert(8)
stack1.insert(120)
stack1.insert(-5)
stack1.insert(-1)
stack1.insert(0)
stack1.insert(255)
stack1.insert(180)


"""def sorted_stack(stack: Stack) -> list:
    list_secondary = Stack()

    while not stack.is_empty():
        element = stack.top()
        stack.pop()
        while not list_secondary.is_empty() and list_secondary.top() > element:
            stack.insert(list_secondary.top())
            list_secondary.pop()
        list_secondary.insert(element)
    return list_secondary.output()"""


def quick_sort_stack(array: list) -> list:
    size_stack = len(array)
    if size_stack <= 1:
        return array

    pivot = array[0]
    samlls_numbers_in_stack = []
    bigs_numbers_in_stack = []
    temporary_list = []
    
    for i in array[0:]:
        if i <= pivot:
            samlls_numbers_in_stack = [i] + samlls_numbers_in_stack
        else:
            bigs_numbers_in_stack = [i] + bigs_numbers_in_stack


    return quick_sort_stack(samlls_numbers_in_stack) +  quick_sort_stack(bigs_numbers_in_stack)
    

array = [100, 98, 45, 76, 3, 1, 4, 0, 5, 0.5]
print(f'Array Desordenado {array}')
result = quick_sort_stack(array)
print(f'Array Ordenado {result}' )