def sum_array(array: list) -> int:
    size_array = len(array)
    if size_array == 0:
        return 0

    return array[0] + sum_array(array[1:])
    
    
array = [1, 2, 3, 4, 5]
result = sum_array(array)
print(result)