import re

f = open("input6.txt", "r")
i = 0
for element in f:
    string = element
for i in range(0, len(string)):
    
    first = string[i]
    print(first)
    second = string[i+1]
    third = string[i+2]
    fourth = string[i+3]
    print(second,third,fourth)
    if first == second or first == third or first == fourth or second == third or second == fourth or third == fourth:
        print("finding...")
    else:
        print(i)
        f = open("output6.txt", "a")
        f.write(first)
        f.write(second)
        f.write(third)
        f.write(fourth)
        f.write("\n")
        f.write(str(i))
        f.close()
    
