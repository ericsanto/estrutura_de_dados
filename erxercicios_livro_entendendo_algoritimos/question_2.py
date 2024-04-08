

def sort_plays_more(array: list) -> list:
    
    size_array = len(array) - 1
    if size_array <= 1:
        return array

    pivot = array[size_array]
    smalls = []
    bigs = []
    
    for i in array:
        if i <= pivot:
            smalls = [i] + smalls
        else:
            bigs = [i] + bigs

    return sort_plays_more(smalls) + sort_plays_more(bigs)

cont_plays = [156, 141, 35, 94, 88, 61, 111]
result = sort_plays_more(cont_plays)
print(result)