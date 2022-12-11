### *** ADVENT OF CODE DAY 3 *** ###

priorities = [] 
halfLine = 0
firstItem = []
secondItem = []
suma = 0
listLength = 0

dct = {'a':1, 'b':2,'c':3,'d':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9,'j':10, 'k':11,'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26, 'A': 27, 'B':28, 'C':29, 'D':30, 'E':31, 'F':32,'G':33,'H':34, 'I':35, 'J':36, 'K':37, 'L':38, 'M':39, 'N':40, '0':41,'P':42, 'Q':43, 'R':44, 'S':45, 'T':46, 'U':47, 'V':48, 'W':49, 'X':50, 'Y':51, 'Z':52}


f = open("input3.txt", "r") 
for line in f:
    length = len(line)
    halfLine = int((length / 2))
    firstItem = line[0:halfLine]
    secondItem = line[halfLine:]
    coincidence = ''.join(set(firstItem).intersection(secondItem))
    priorities.append(coincidence)


result = [dct[k] for k in priorities]

listLength = len(priorities)

for i in range (listLength):
    suma = suma + result[i]

print("El número de items es: " + str(suma))



