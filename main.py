n = int(input())

best_value = [-1,-1]
best_computer = [None,None]


def replace(index, name, value):
    best_computer[1] = best_computer[0]
    best_value[1]=best_value[0]
    best_computer[index] = name
    best_value[index] = value


for i in range(n):
    computer = input().split(" ")
    value = int(computer[1])*2 + int(computer[2])*3 + int(computer[3])
    if value > best_value[0]: # the value is larger then the first computer
        replace(0, computer[0],value)
    elif value == best_value[0]: # the value equals to the first computer
        if computer[0] < best_computer[0]: # the current name is smaller than the first computer
            replace(0, computer[0], value)
        elif value > best_value[1]: # the value is equal to the first but larger than the second
            replace(1, computer[0], value)
        elif value == best_value[1]: # the value equals to both first and second computers.
            if computer[0] < best_computer[1]: # the current name is smaller than the second computer
                replace(1, computer[0], value)
    else: # the value is smaller than the first computer
        if value > best_value[1]: # the value is larger than the second.
            replace(1, computer[0], value)
        elif value == best_value[1]:
            if computer[0] < best_computer[1]:
                replace(1, computer[0], value)

print(best_computer[0])
print(best_computer[1])

