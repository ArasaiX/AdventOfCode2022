### *** ADVENT OF CODE DAY 3 *** ###

totalPuntuacion = 0
f = open("input2.txt", "r")


for linea in f:
    line = linea[0:3]
    if line == "A X": #roca vs roca
        totalPuntuacion = totalPuntuacion + 4
    elif line == "A Y": #
        totalPuntuacion = totalPuntuacion + 8
    elif line == "A Z":
        totalPuntuacion = totalPuntuacion + 3
    elif line == "B X":
        totalPuntuacion = totalPuntuacion + 1
    elif line == "B Y":
        totalPuntuacion = totalPuntuacion + 5
    elif line == "B Z":
        totalPuntuacion = totalPuntuacion + 9
    elif line == "C X":
        totalPuntuacion = totalPuntuacion + 7
    elif line == "C Y":
        totalPuntuacion = totalPuntuacion + 2
    elif line == "C Z":
        totalPuntuacion = totalPuntuacion + 6

print("El total de puntuación según la guía es: "+ str(totalPuntuacion))

