class Computer:
    def __init__(self, name, value):
        self.name = name
        self.value = value
    
    def __eq__(self, other):
        return self.name == other.name and self.value == other.value
    
    def __lt__(self, other):
        if self.value < other.value:
            return True
        else:
            return self.name > other.name
    
    def __gt__(self, other):
        if self.value > other.value:
            return True
        else:
            return self.name < other.name


n = int(input())

computers = []


for i in range(n):
    parts = input().split(" ")
    value = int(parts[1])*2 + int(parts[2])*3 + int(parts[3])
    computer = Computer(parts[0], value)
    computers.append(computer)

computers.sort(reverse=True)

print(computers[0].name)
print(computers[1].name)

    


