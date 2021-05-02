# Ejercicio1 - Rango del 0 a 9
for i in range ( 10 ):
    imprimir ( i )

imprimir ()

# Ejercicio2 - Rango entre 100 y 199
for i in range  ( 100 , 200 , 1 ):
    imprimir ( n )

imprimir ()

# Ejercicio3 - Rango de 5 inclusivo hasta 20 y que vaya de 3 en 3
for z in range  ( 5 , 20 , 3 ):
    imprimir ( z )

imprimir ()

# Ejercicio4 - Rango con primer número ingresado y que llega hasta menos del doble del mismo
numb1 =  int ( input ( "Ingrese un número =" ))
for h in range ( numb1 , numb1 * 2 ):
    imprimir ( h )

imprimir ()

#Ejercicio 5 y 6 - Contar las vocales
frase  =  input ( "frase:" )
print ( "Las vocales de la frase son:" )
for r in  "aeiou" :
    if r  in  frase :
        imprimir ( r )

imprimir ()

#Ejercicio 7 - Suma total 100
total  =  0
for m in range( 101 ):
    total  +=  m

print ( "Suma total =" , total )

imprimir ()

#Ejercicio 8 - Año
anio1  =  int ( input ( "Ingrese el primer año =" ))
anio2  = int ( input ( "Ingrese el segundo año =" ))

ano = input("Favor ingrese el año: ")
if (ano % 100 != 0):
    if (ano % 4 == 0):
        print("Bisiesto")
    else:
        print("No bisiesto")
elif (ano % 400 == 0):
    print("Bisiesto")
else:
    print("No bisiesto")
print("\n")
print()

# Ejercicio9 - Factorial
numero =  int ( input ( "Número:" ))
hecho = 1
if  numero != 0 :
    for i in range  ( 1 , numero + 1 ):
        hecho = hecho * i  #
print ( "Factorial:" , hecho )

imprimir ()

#Ejercicio 10 - Sucesión de Fibonacci
n1  =  0
n2  =  1
print( n1 )
print( n2 )
for i in range  ( 8 ):
    n3  =  n1  +  n2
    print ( n3 )
    n1  =  n2
    n2  =  n3