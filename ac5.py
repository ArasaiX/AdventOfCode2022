### *** ADVENT OF CODE DAY 5 *** ###

stack = [
            ['Q','W','P','S','Z','R','H','D'],
            ['V','B','R','W','Q','H','F'],
            ['C','V','S','H'],
            ['H','F','G'],
            ['P','G','J','B','Z'],
            ['Q','T','J','H','W','F','L'],
            ['Z','T','W','D','L','V','J','N'],
            ['D','T','Z','C','J','G','H','F'],
            ['W','P','V','M','B','H']
        ]

f = open("input5.txt", "r")

for line in f:
    if line.__contains__("move"):
        moves = line.replace("move ","")
        moves = moves.replace("from","")
        moves = moves.replace("to","")
        moves = moves.replace("\n", "")
        moves = moves.replace("  ", "-")
        numberOfMov, fromStack, toStack = map(str, moves.replace(" ", "-").split("-"))
        intStackTo = int(toStack) - 1
        intStackFrom = int(fromStack) - 1
        for i in range(int(numberOfMov)):
            if stack[intStackFrom]:
                x = stack[intStackFrom].pop()
                stack[intStackTo].append(x)

lenght = len(stack)
print("The result is: ", end='')
for i in range(lenght):
    print(stack[i][-1], end='')
print("")

