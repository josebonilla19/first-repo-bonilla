# Autor: José Alejandro Bonilla Carrera
# Fecha: 05/08/2026
contador = 0
suma = 0
 
nota = int(input("Ingresa una nota (o -1 para terminar): "))
 
while nota != -1:
    if nota < 0 or nota > 100:
        print("Nota fuera de rango, intenta de nuevo.")
    else:
        contador = contador + 1
        suma = suma + nota
    nota = int(input("Ingresa una nota (o -1 para terminar): "))
 
promedio = suma / contador
 
print()
print("Notas ingresadas:", contador)
print("Promedio:", promedio)