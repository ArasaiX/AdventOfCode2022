### *** ADVENT OF CODE 2022 DAY 1 *** ###
#Search the elve with more calories

f = open("input1.txt", "r")
suma = 0
total_sumas = []

for linea in f:
    if linea != '\n':
        suma = suma + int(linea)
    elif linea == '\n':
        total_sumas.append(suma)
        suma = 0

indexMax = total_sumas.index(max(total_sumas))
print("El elfo número: "+ str(indexMax)+" lleva más calorias")
total_sumas.sort(reverse=True)
maxCalorias = max(total_sumas)
print("EL total de calorias que lleva el elfo "+ str(indexMax)+" son "+ str(maxCalorias))

#Second part 

suma3= total_sumas[0]+total_sumas[1]+total_sumas[2]
print("El total de la suma de las calorias de los tres elfos que llevan más es "+str(suma3))


