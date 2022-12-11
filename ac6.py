### *** ADVENT OF CODE DAY 6 *** ###

markerLenght = 14 #change this for part1 or two (4 or 14)

f = open("input6.txt", "r")

signal = f.read()

for i in range (len(signal) - markerLenght - 1):
    marker = signal[i:i+markerLenght]
    if len(set(marker)) == markerLenght:
        print("The first maker is:" + str(i+markerLenght))
        break
