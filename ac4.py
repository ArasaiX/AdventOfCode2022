#### ADVENT OF CODE DAY 4 ###

f = open("input4.txt", "r")

i = 0
for line in f:
    a, b, x, y = map(int, line.replace(",", "-").split("-"))
    if a <= x and b >= y or x <= a and y >= b:
        i+= 1

print(i)

