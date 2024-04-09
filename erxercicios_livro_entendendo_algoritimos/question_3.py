def inferior_number(number: int):
    print(number)
    if number == 1:
        return 
    inferior_number(number - 1)

number = 5
result = inferior_number(number)

print(result)