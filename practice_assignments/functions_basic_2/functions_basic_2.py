def countdown(num):
    newList =[]
    for i in range(num, -1, -1):
        newList.append(i)
    return newList
print(countdown(5))
def print_and_return(list):
    print(list[0])
    return list[1]
print(print_and_return([1,2]))

def first_plus_length(list):
    print(list[0])
    return len(list)
print(first_plus_length([1, 2, 3, 4, 5]))
