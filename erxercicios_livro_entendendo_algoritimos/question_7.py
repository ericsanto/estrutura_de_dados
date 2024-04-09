def duplicate_element_list(array: list) -> list:
    if not array:
        return []
    else:
        return [array[0], array[0]] + duplicate_element_list(array[1:])


array = [3, 5, 6, 1, 12, 3, 21, 67, 2]
result = duplicate_element_list(array)
print(result)