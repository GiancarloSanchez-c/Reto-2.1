lista_notas = []
suma_notas = 0
prom = 0

print()


'''def bienvenida():
    print("'------------------Bienvenido--------------------'\n")
    nombre = input("Ingrese su nombre: ")
    apellido =  input(f"Bienvenido {nombre}.\nIngrese su apellido: ")
    saludo = print(f"Bienvenido {nombre} {apellido}")

bienvenida()
print()'''
print("'-----------------Notas----------------------'\n")

while True:
    try:
        def notas():
            cantidad_notas = int(input(f"¿Cuantas notas tiene el alumno ?\n"))

            for nota in range(cantidad_notas):
                nota = float(input(f"Nota {nota+1}: "))

            
                lista_notas.append(nota)
            
        notas()
        break
    except (TypeError, ValueError) :
            print('Ocurrio un problema: El valor ingresado es incorrecto\nIngrese un dato correcto')

for i in lista_notas:

    suma_notas= suma_notas + i
    prom = suma_notas / len(lista_notas)

    nota_menor= min(lista_notas)
    nota_mayor =max(lista_notas)

print("-------------Lista de Notas---------------------")
print(lista_notas)
print()
print(f'El promedio es: {prom}')
print(f"'Nota mayor: {nota_mayor}'")
print(f"'Nota menor: {nota_menor}'")
