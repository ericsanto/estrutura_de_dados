def cont_items_array(array:list) -> int:
    size_array = len(array)
    if size_array <= 1:
        return size_array
    return cont_items_array(array[1:]) + 1

array = [1, 3, 4, 5, 6, 7]
result = cont_items_array(array)
print(result)