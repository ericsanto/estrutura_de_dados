def duplicate_first_element_array(array: list) -> list:
    if not array:
        return []
    else:
        return [array[0], array[0]] + array[1:]


array = [3, 5, 6, 1, 12, 3, 21, 67, 2]
result = duplicate_first_element_array(array)
print(result)