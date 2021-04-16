#Taller de parctica
#Ejercicio 1
print("escribe tu nombre y tu calificativo")
nombre = input(":")

Calificativo = input(":")
imprimir = nombre + Calificativo
print("tu nombre y tu calificativo", "esto es: ",  imprimir)

#Ejercicio 2
Numero = int(input("introducir un numero: "))
print("El cuadrado de", Numero, "es:" ,Numero ** 2)

#Ejercicio 3
print("escriba dos numeros para sumar")
num1 = int(input())
num2 = int(input())
resultado = num1 + num2
print("la suma de ", num1, "y", num2, "es igual a: ", resultado)

#Ejercicio 4
print("Escriba dos numeros")
num1 = int(input())
num2 = int(input())
resultado1 = num1 + num2
resultado2 = num1 - num2
resultado3 = num1 * num2
resultado4 = num1 / num2
resultado5 = num1 % num2
print("la suma de", num1, "y", num2, "es igual a: ", resultado1)
print("la resta de", num1, "y", num2, "es igual a: ", resultado2)
print("la multiplicacion de", num1, "y", num2, "es igual a: ", resultado3)
print("la division de", num1, "y", num2, "es igual a: ", resultado4)
print("el residuo de", num1, "y", num2, "es igual a: ", resultado5)

#Ejercicio 5
print("ingrese un numero decimal:")
num1 = float(input())
from math import modf
print('{}(F)  (I)'.format(' ' * 10))
for i in range(6):
    print('{}/3 = {}  {}'.format(i, i/3, modf(i//3.0)))

#Ejercicio 6
#Calcular el IVA (19%) de un producto _____ me vi un video (https://youtu.be/uBPno9GOrEM)

def calcular():
    precio = float(input("ingrese el precio de su producto: "))
    IVA = precio * 0.16
    print("El Valor de la venta realizada", precio )
    print("el IVA de su producto es:", IVA)
    PrecioTotal = precio + IVA
    print("el precio total es de:", PrecioTotal)

calcular()
#Ejercicio 7

#Ejercicio 8
from math import pi
r =  float(input("escriba el valor del radio: "))
area = pi * r  ** 2
print("El area del circulo es igual a {:.2f}". format(area))
circunferencia = 2 * pi * r
print("la circunferencia del circulo es igual a {:.2f}". format(circunferencia))

#Ejercicio 9
print("escriba tres numeros")
num1 = float(input())
num2 = float(input())
num3 = float(input())
resultado = (num1 + num2 + num3)/3
print("el promedio de los tres numeros es igual a:", resultado)

#Ejecicio 10
a = float(input("numero 1="))
b = float(input("numero 2="))
c = b
d = a
print(" a era=",a," pero ahora es=",c)
print(" b era=",b," pero ahora es=",d)


#Ejercicio 11

#ejercicio 12
altura = float(input("H:"))
tiempo = (((2*altura)/9.80)**0.5)
print("el tiempo en caer es:",tiempo)

#Ejecicio 13
masa = float(input("masa="))
velocidad = float(input("velocidad="))
energia = (masa*velocidad+velocidad)/2
print("la energia es=", energia, "J")


#Ejercicio 14
"""
escribe un algoritmo  que determine la energía
(en Julios) de un objeto si se conoce la masa de un objeto
(en kg) y la velocidad de la luz (en m/s).
"""
#fórmula  = ( 1 / 2 ) * ( m * c ** 2 )
opcion1 = float(input("desea ingresar la masa \n1. en kg \n o \n2. en lb \n"
                      "elija una opcion: "))
if opcion1 == 1:
    m = float(input("ingrese la masa: "))
    print("la masa es igual a", m)
elif opcion1 == 2:
    lb = float(input(" ingrese la cantidad de lb para convertir a kg: "))
    kilogramos = lb * 0.453592
    print("la masa es igual a", kilogramos)
opcion2 =  float(input("desea saber la velociad \n1. en m/s \n o desea convertir de \n2. km/s a m/s \n "
                       "elija una opcion: "))
if opcion2 == 1:
    V = 299792458.0
    print("la velocidad de la luz en m/s es igual a, 299792458.0")
elif opcion2 == 2:
   velocidad_de_la_luz = 299792.458
   metros_por_segundo = velocidad_de_la_luz * 1000
   V = metros_por_segundo
   print("la velocidad esta representada en m/s y es igual a: ", metros_por_segundo)

m = kilogramos
c = V
formula = (1/2) * (m*c**2)
print("la energia  del objeto es igual a: ", formula)


