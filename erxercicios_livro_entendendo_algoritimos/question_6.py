def big_value_in_array(array: list) -> int:
    if not array:
        return None
    
    if len(array) == 1:
        return array[0]
    else:
        big = big_value_in_array(array[1:])
        return array[0] if array[0] > big else big


array = [3, 5, 6, 1, 12, 3, 21, 67, 2]
result = big_value_in_array(array)
print(result)