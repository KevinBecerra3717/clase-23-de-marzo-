#ejercicio 1
nombre = int(input("ingrese un numero:"))
if nombre % 5 == 0 and nombre % 3 == 0:
    print("el numero cumple.")
else:
    print("el numero no cumple")

#ejercicio 2
nota1 = float(input("ingrese la primera nota:"))
nota2 = float(input("ingrese la segunda nota:"))
nota3 = float(input("ingrese la tercera nota:"))
promedio = (nota1 + nota2 + nota3) / 3
if promedio>=7:
    print("promocionado", promedio)
if promedio>=4 and promedio<7:
    print("regular")
if promedio<4:
    print("no habilitado")

#ejercicio 3
nota1 = float(input("ingrese la primera nota:"))
nota2 = float(input("ingrese la segunda nota:"))
nota3 = float(input("ingrese la tercera nota:"))
promedio = (nota1 + nota2 + nota3) / 3
if promedio>=7:
    print("promedio", promedio)
elif promedio>=4 and promedio<7:
    print("regular")
else:
    print("no habilitado")
#
listaCuadrados = [x*x for x in range(1,11) if x%2 !=0]
print(listaCuadrados)