numbers = [5, 15, 4, 12, 6, 18, 21]

def find_max(list):
    current_max = list[0]
    for n in list:
        if n > current_max:
            current_max = n
    return current_max

numbers = find_max(numbers)
print(numbers)