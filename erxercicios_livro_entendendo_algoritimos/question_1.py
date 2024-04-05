import random
import time



def search_binary(array: list, number: int) -> int or None:
    end = len(array) - 1
    start = 0
    
    while start <= end:
        quite = (end + start) // 2
        quick = array[quite]
        if quick == number:
            return quite
        if quick > number:
            end = quite - 1
        else:
            start = quite + 1
    return None


array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
number = 45

start_time = time.time()
result = search_binary(array, number)
end_time = time.time()

if result is not None:
    print(f'O numero {number} esta na lista e foi encontrado na posição {result}')
else:
    print(f'O número {number} não está na lista')

time_algoritm_execution = end_time - start_time
print(f'A função search_binary levou {time_algoritm_execution} para ser executada')

print('---------------------------------------------------------------------------------')

def search_item(array: list, number: int) -> int or None:
    cont = -1
    for i in array:
        if i == number:
            return array[cont]
        cont += 1
    return None

array_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
number_2 = 45

start_time_2 = time.time()
result_2 = search_item(array_2, number_2)
end_time_2 = time.time()

if result is not None:
    print(f'O numero {number_2} esta na lista e foi encontrado na posição {result_2}')
else:
    print(f'O número {number_2} não está na lista')

time_algoritm_execution_2 = end_time_2 - start_time_2
print(f'A função search_binary levou {time_algoritm_execution_2} para ser executada')