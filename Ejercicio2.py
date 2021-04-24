Lista_Notas = []
suma_Notas = 0
Prom = 0

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
                not1 = float(input(f"Ingrese la nota {nota+1}: "))

        notas()
        break
    except (TypeError, ValueError) :
            print('Ocurrio un problema: El valor ingresado es incorrecto\nIngrese un dato correcto')