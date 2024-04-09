import time

def multiplication_self_elements_array_one(array: list) -> list:
    if not array:
        return []
    else:
        return [array[0] * array[0]] + multiplication_self_elements_array_one(array[1:])


start_one = time.time()
array_one = [3, 5, 6, 1, 12, 3, 21, 67, 2, 100, 333, 555, 1000]
result_one = multiplication_self_elements_array_one(array_one)
print(result_one)
finish_one = time.time()
print(f'Tempoo de Execução: {finish_one - start_one}')




def multiplication_self_elements_array(array: list) -> list:
    array_temporary = []
    for i in array:
        x = i * i
        array_temporary = array_temporary + [x]

    return array_temporary


start = time.time()
array = [3, 5, 6, 1, 12, 3, 21, 67, 2, 100, 333, 555, 1000]
result = multiplication_self_elements_array(array)
print(result)
finish = time.time()
print(f'Tempoo de Execução: {finish - start}')
