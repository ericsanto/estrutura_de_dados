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


def sorted_stack(stack: Stack) -> list:
    list_secondary = Stack()

    while not stack.is_empty():
        element = stack.top()
        stack.pop()
        while not list_secondary.is_empty() and list_secondary.top() > element:
            stack.insert(list_secondary.top())
            list_secondary.pop()
        list_secondary.insert(element)
    return list_secondary.output()


stack2 = sorted_stack(stack1)
print(stack2)
    

