#Taller de parctica
#Ejercicio 1
print("escribe tu nombre y tu calificativo")
nombre = input(":")
Calificativo = input(":")
imprimir = nombre + Calificativo
print("tu nombre y tu calificativo", "esto es: ",  imprimir)
print("\n")

#Ejercicio 2
Numero = int(input("introducir un numero: "))
print("El cuadrado de", Numero, "es:" ,Numero ** 2)
print("\n")

#Ejercicio 3
print("escriba dos numeros para sumar")
num1 = int(input())
num2 = int(input())
resultado = num1 + num2
print("la suma de ", num1, "y", num2, "es igual a: ", resultado)
print("\n")

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
print("\n")

#Ejercicio 5
decimal  =  float ( input ( "Ingrese un número decimal =" ))
imprimir ()
#Proceso separar parte entera
entero  =  int ( decimal )
print ( "La parte entera es ="  +  str ( entero ) +  " \ n " )
#Proceso para separar la parte decimal de la entera
decimal2  =  float ( entero  -  decimal )
print ( "La parte decimal es ="  +  str ( decimal2 ) +  " \ n " )
print("\n")

#Ejercicio 6
precio = float(input("ingrese el valor total de su compra: "))
IVA = precio * 0.19
print("el valor de la venta realizada", precio)
print("El IVA de su producto es: ",IVA)
print("Recuer que si su compra excede los 150000 tendra un descuento hasta de un 5% de su compra en total \nno dejes pasar esta gran oferta")
precioTotal = precio + IVA
print("EL precio total de su compra es de:", precioTotal)
print("\n")

#Ejercicio 7
Pi  =  3,1416
radio  =  float ( input ( "Ingrese el valor del radio del área =" ))
#Ecuaciones
areaCirculo  =  Pi  *  pow ( radio , 2 )
print ( "El área del círculo es ="  +  str ( areaCirculo ) +  " \ n " )
#Condiciones
perimetro  =  str(input( "¿Quieres hallar el perímetro con el diámetro o con el radio ?, 1 o 2 =" ))
if perimetro  ==  "1" :
    perimetroRadio  = 2 * Pi * radio
    print ( "El perímetro del círculo es ="  +  str ( perimetroRadio ) +  " \ n " )
else:
    diametro  = float(input( "Ingrese el valor del diámetro =" ))
    perimetroDiametro  =  Pi  * ( diametro / 2 )
    print ( "El perímetro del círculo es ="  +  str ( perimetroDiametro ) +  " \ n " )

print ( "¡El programa ha finalizado con éxito!" )
print("\n")

#Ejercicio 8
from math import pi
r =  float(input("escriba el valor del radio: "))
area = pi * r  ** 2
print("El area del circulo es igual a {:.2f}". format(area))
circunferencia = 2 * pi * r
print("la circunferencia del circulo es igual a {:.2f}". format(circunferencia))
print("\n")

#Ejercicio 9
print("escriba tres numeros")
num1 = float(input())
num2 = float(input())
num3 = float(input())
resultado = (num1 + num2 + num3)/3
print("el promedio de los tres numeros es igual a:", resultado)
print("\n")

#Ejecicio 10
a = float(input("numero 1="))
b = float(input("numero 2="))
c = b
d = a
print(" a era=",a," pero ahora es=",c)
print(" b era=",b," pero ahora es=",d)
print("\n")

#Ejercicio 11
altura = float(input("H:"))
tiempo = (((2*altura)/9.80)**0.5)
print("el tiempo en caer es:",tiempo)
print("\n")

#ejercicio 12
altura = float(input("H:"))
tiempo = (((2*altura)/9.80)**0.5)
print("el tiempo en caer es:",tiempo)
print("\n")

#Ejecicio 13
masa = float(input("masa="))
velocidad = float(input("velocidad="))
energia = (masa*velocidad+velocidad)/2
print("la energia es=", energia, "J")
print("\n")

#Ejercicio 14
opcion = float(input("Ingrese la masa del objeto, ¿desea ingresarla en: \n1. lb \n2. kg \n"
                     "elija una opcion: "))
if opcion == 1:
    lb = float(input("ingrese la cantidad de lb para convertir a kg: "))
    kilogramos = lb * 0.453592
    m = kilogramos
    print("la masa del objeto es igual a", kilogramos, "kg")
elif opcion == 2:
    m = float(input("Ingrese la masa: "))
    print("la masa del objeto es igual a", m, "kg")
v = 299792458.0
print("la velocidad de la luz es igual a", v, "m/s")
formula = m * v**2
print("la energia del objeto es igual a", formula,"J")
print("\n")

#Ejercicio 15
print("ingrese las coordenadas de x1,x2 y las coordenanas de y1,y2")
print("ingrese solo valores positivos.")
coordenadas_x1 = float(input("coordenadas de x1: "))
coordenadas_y1 = float(input("coordenadas de y1: "))
coordenadas_x2 = float(input("coordenadas de x2: "))
coordenadas_y2 = float(input("coordenadas de y2: "))
distancia1 = coordenadas_x1 - coordenadas_y1
distancia2 = coordenadas_x2 - coordenadas_y2
print("la distancia entre x1 y y1 es:", distancia1)
print("la distancia entre x2 y y2 es:", distancia2)
print("\n")

#Ejercicio 16
segundos = float(input("ingrese la cantidad de segundos: "))
Hora = segundos * 0.000277778
print(segundos,"representan", Hora, "Horas")
print("\n")

#Ejercicio 17
segundos = float(input("ingrese la cantidad de segundos: "))
minutos = segundos * 0.0166667
print(segundos,"representan", minutos, "minutos")
print("\n")

#Ejercicio 18 Pendiente con el tutor
HoraDelDia = int(input("ingrese los segundos: "))
hora = HoraDelDia/3600
parteDecimal1 = hora-int(hora)
minutos = parteDecimal1*3600/60
parteDecimal2 = minutos/60
segundos = parteDecimal2*60
print(int(hora),":",int(minutos),":",int(segundos))
#Ejercicio 19 Pendiente con el tutor--------------------------------------------------------------------------------------------------------------------------------------------------------------
print("\n")

#Ejercicio 20
# Definir variables, acumuladores
valor = 0
cien = 0
cincuenta = 0
veinte = 0
diez = 0
cinco = 0
mil = 0
#Proceso
valor = int(input("Ingrese la cantidad de dinero = "))
if valor >= 1:
    # Billete 100.000
    cien = int(valor / 100000)
    reserva = valor % 100000
    #Billete 50.000
    cincuenta = int(reserva / 50000)
    reserva = reserva % 50000
    #Billete 20.000
    veinte = int(reserva / 20000)
    reserva = reserva % 20000
    #Billete 10.000
    diez = int(reserva / 10000)
    reserva = reserva % 10000
    #Billete 5.000
    cinco = int(reserva / 5000)
    reserva = reserva % 5000
    #Billete 1.000
    mil = int(reserva / 1000)
    reserva = reserva % 1000
    #IMPRIMIR
    print("La cantidad mínima de cada billete son:")
    print(str(cien) + " de 100.000" + "\n"+ str(cincuenta) + " de 50.000" + "\n" + str(veinte) + " de 20.000" + "\n" + str(diez) + " de 10.000" + "\n" + str(cinco) + " de 5.000" + "\n" + str(mil)+ " de 1.000" )
else:
    print("La cantidad de billetes ingresados es incorrecta, no se permiten valores negativos.")
print("\n")

#Ejercicio 21
numero = 0
numero = int(input("introuzca un numero!"))
if numero%2 == 0:
    print("El numero: %d es par!" %numero)
else:
    print("Uyyy, el numero: %d no es par! entonces, es impar!" % numero)
print("\n")
#Ejercicio 22
n = int(input("ingrese un numero: "))
if n == 0:
    print("el numero",n,"es neutro")
else:
    if n < 0:
        print("el numero",n,"es negativo")
    else:
        print("el numero",n,"es positivo")
print("\n")

# Ejercicio 23
n = int(input("ingrese un numero: "))
if n%2 == 0 and n >= 0:
    print("el numero: %d es par positivo!" %n)
elif n%2 == 0 and n < 0:
    print("el numero: %d es par negativo!" %n)
elif n < 0:
    print("el numero: n es impar negativo!", n)
else:
    print("el numero: n es impar positivo!", n)
print("\n")

#Ejercicio 24
precio = float(input("ingrese el valor total de su compra: "))
IVA = precio * 0.19
print("el valor de la venta realizada", precio)
print("El IVA de su producto es: ",IVA)
print("Recuer que si su compra excede los 150000 tendra un descuento hasta de un 5% de su compra en total \nno dejes pasar esta gran oferta")
precioTotal = precio + IVA
if precioTotal >= 150000:
    descuento = precioTotal * 0.05
    print("el desucento de su compra es de:", descuento)
    print("Precio total con el respectivo descuento es de:", precioTotal - descuento)
else:
    print("EL precio total de su compra es de:", precioTotal)
print("\n")

#Ejercicio 25
ecuacion = int(input("ingrese un numero: "))
if ecuacion >= 10:
    print(ecuacion * 3)
else:
    print(ecuacion/4)
print("\n")

#Ejercicio 26
nota1 = 0.15
nota2 = 0.20
nota3 = 0.15
nota4= 0.30
nota5 = 0.20
nota6 = int(input("Ingrese su nota: "))
nota7 = int(input("Ingrese su nota: "))
nota8 = int(input("Ingrese su nota: "))
nota9 = int(input("Ingrese su nota: "))
nota10 = int(input("Ingrese su nota: "))

promedio = ((nota1* nota6) + (nota2*nota7) +(nota3*nota8) +(nota4*nota9)+(nota5*nota10))
print(promedio)

if promedio > 45:
    print("aprobo, felicitaciones has sido el mejor")
if promedio >= 30 and promedio <= 45:
    print("aprobo.")
if promedio < 30:
    print("reprobo")
if promedio < 20:
    print("no puede habilitar ")
print("\n")

#Ejercicio 27
num1 = float(input("ingrese un numeros: "))
num2 = float(input("ingrese un numeros: "))
if num1 > num2:
    print(num1)
if num2 > num1:
    print(num2)
if num1 == num2:
    print("usted a ingresado dos numeros iguales")
print("\n")

#Ejercicio 28
number  =  int ( input ( "Ingrese el número que desea convertir un decimal =" ))
#Proceso
decimal  =  float(number)
print ( "El número con cifras decimales es =" , decimal )
print("\n")

#Ejercicio 29
num1 = float(input("ingrese un numeros: "))
num2 = float(input("ingrese un numeros: "))
num3 = float(input("ingrese un numeros: "))
if num1 > num2 and num2 > num3:
    print("el numero mayor es",num1,"El numero menor es",num3)
if num1 > num2 and num3 > num2:
    print("el numero mayor es",num1,"El numero menor es",num2)
if num1 < num2 and num1 < num3:
    print("el numero mayor es",num2,"El numero menor es",num1)
if num1 < num2 and num1 > num3:
    print("el numero mayor es",num2,"El numero menor es",num3)
if num3 > num2 and num2 > num1:
    print("el numero mayor es",num3,"El numero menor es",num1)
if  num3 > num2 and num2 < num1:
    print("el numero mayor es",num3,"El numero menor es",num2)
if num1 == num2 and num2 == num3:
    print("usted a ingresado dos numeros iguales")
print("\n")
#Ejercicio 30
num1 = float(input("ingrese un numeros: "))
num2 = float(input("ingrese un numeros: "))
num3 = float(input("ingrese un numeros: "))
if num1 + num2 > num3:
    print(num1, "+", + num2, "es mayor que ", num3)
if num1 + num2 < num3:
    print(num1, "+",num2,"es menor que ",num3)
if num1 + num2 == num3:
    print(num1,"+",num2,"es igual que ",num3)
print("\n")

#Ejercicio 31
#Ejercicio 32
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

#Ejercicio 31
#Definir variables
distancia = int(input("Ingrese la distancia que se recorrió = "))
dias = int(input("Ingrese el número de días de estancia = "))
km = 5000 #Mínimo a cobrar 100.000
#Procesos
total = (distancia * 5000)
if (distancia < 1000) and (dias < 7):
    print("El valor del pasaje es = $" + str(total) + " " + "y su estancia fue de" + " " + str(dias) +  " " + "días")
else:
    if (distancia > 1000) and (dias > 7):
        total = total - (total * 0.15)
        print("Le valor del pasa es = $" + str(total) + " (con descuento del 15%) " +  "y su estancia fue de" + " " + str(dias) + " " + "dias.")
print("\n")

#Ejercicio 32
a = int(input("Escriba el año que desea saber si es bisiesto :"))
if a % 4 == 0 and a % 100 != 0:
    print("El año es Bisiesto")
else:
    if a % 4 == 0 and a % 100 == 0 and a % 400 == 0:
        print("El año es Bisiesto")
    else\
            :print("El año no es Bisiesto")
print("\n")

#Ejercicio 33
a  =  float ( input ( "Ingrese el número de a =" ))
b  =  float ( input ( "Ingrese el número de b =" ))
c  =  float ( input ( "Ingrese el número de c =" ))
#Definir proceso
discriminante  = ( b  **  2 ) -  4  *  a  *  c
if discriminante  <  0 :
    print ( "La ecuación no tiene soluciones reales" )
elif  discriminante  ==  0 :
    x  =  - b  / ( 2 * a )
    print ( "La solución es =" , x )
else:
    x1  = ( - b  - ( discriminante  **  0.5 )) / ( 2  *  a )
    x2  = ( - b  + ( discriminante  **  0.5 )) / ( 2  *  a )
    print ( "Las dos soluciones reales son ="  +  str ( x1 ) +  "y"  +  str ( x2 ))
print("\n")

#Ejercicio 34
usuario = "KevinBecerra"
contra = "Kevin3717"
u = str(input("¿Cual es el usario? "))
c = str(input("¿Cual es la contraseña? "))
if u == usuario and c == contra:
    print("Ha ingresado a la cuenta correctamente")
else:print("El usuario o contraseña esta incorrecto, vuelva a intentar")
print("\n")

#Ejercicio 35
number  =  int ( input ( "Ingrese un número entre 0 y 10 =" ))
nombreNumber  = [ 'Cero' , 'Uno' , 'Dos' , 'Tres' , 'Cuatro' , 'Cinco' , 'Seis' , 'Siete' , 'Ocho' , 'Nueve' , 'Diez' ]
print ( "El nombre del número"  +  ""  +  str (number) +  ""  +  "es ="  +  str ( nombreNumber [ number]))
print("\n")

#Ejercicio 36
number  =  int ( input ( "Ingrese un número menor a 100000 =" )) # Definir Entrada
contador  =  0
while numero != 0:
    número  =  número  //  10
    contador  +=  1
print ( "La cantidad de dígitos del número ingresado son ="  +  str ( contador ) +  ""  +  "dígitos" )
print("\n")

#Ejercicio 37
nota1 = int(input("Ingrese su nota: "))
nota2 = int(input("Ingrese su nota: "))
nota3 = int(input("Ingrese su nota: "))
if nota1 == nota2 == nota3:
    print(nota1, nota2, nota3, "ni se incrementa ni se disminuye")
if nota1 > nota2 > nota3:
    print(nota1,nota2,nota3,"esta disminuyendo")
if nota1 > nota3 > nota2:
    print(nota1,nota2,nota3,"ni se incrementa ni se disminuye")
if nota2 > nota1 > nota3:
    print(nota1,nota2,nota3,"ni se incrementa ni se disminuye")
if nota2 > nota3 > nota1:
    print(nota1,nota2,nota3,"ni se incrementa ni se disminuye")
if nota3 > nota1 > nota2:
    print(nota1,nota2,nota3,"ni se incrementa ni se disminuye")
if nota3 > nota2 > nota1:
    print(nota1,nota2,nota3,"esta incrementando")
print("\n")

#Ejercicio 38
num1 = int(input("ingrese un numero: "))
num2 = int(input("ingrese un numero: "))
if (num1 and num2) > 0 and (num1 and num1) < 5:
    print("True")
if (num1 and num2) > 5:
    print("False")
print("\n")

#Ejercicio 39
nombreDias  = [ 'Ninguno' , 'Lunes' , 'Martes' , 'Miércoles' , 'Jueves' , 'Viernes' , 'Festivo' , 'Festivo' ] #lista para determinar el día
number  =  int ( input ( "Ingrese el número de la semana para conocer el nombre del día =" )) #Definir entrada
print ( "El nombre del día número"  +  ""  + str ( número ) +  "es ="  +  str ( nombreDias [ número ]))
print("\n")

#Ejercicio 40
num1 = int(input("ingrese un numero: "))
num2 = int(input("ingrese un numero: "))
num3 = int(input("ingrese un numero: "))
if num1 == num2:
    print(num1,"es igual a", num2)
if num1 == num3:
    print(num1,"es igual a", num2)
if num2 == num3:
    print(num2,"es igual a", num3)
print("\n")
#Ejericio 41
for  i  in  range ( 11 ):
    print ( "Los primeros números naturales son =" , i )
print("\n")

#Ejericio 42
for i in range ( 1 , 20 ):
    if  i  %  2  != 0:
        print ( "Los primeros 10 número impares =" , i )
print("\n")

#Ejericio 43
for i in range( 1 , 21 ):
    if  i  %  2  ==  0 :
        print ( "Los primero 10 número pares son =" , i )
print("\n")

#Ejericio 44
n  =  int ( input ( "Ingrese un número =" ))
for i in range( n ):
    print ( "Los primeros números naturales del número ingresado son =" , i )
print("\n")

#Ejericio 45 ---------------------------------------------------------------------------------------------------------------------------
print("\n")

#Ejericio 46---------------------------------------------------------------------------------------------------------------------------
number1  =  int ( input ( "Ingrese el primer número =" ))
number2  =  int ( input ( "Ingrese el segundo número =" ))
if number2  >  number1 :
    for i in  range ( number1 , number2 ):
        print ( "Los números naturales que hay entre los números ingresados ​​son ="  +  ""  +   str ( i ))
else:
    print ( "El segundo número debe ser mayor que el primero porque es el límite." )
print("\n")

#Ejericio 47
suma = 0
number1 = int(input("Ingrese el primer número = "))
number2 = int(input("Ingrese el segundo número = "))
if number2 > number1:
    for i in range(number1,number2):
        suma = suma + i
    print("La suma de los números naturales que hay entre los dos números ingresados es = ", suma)
else:
    print("El segundo número debe ser mayor que el primero porque es el límite.")
print("\n")

#Ejericio 48---------------------------------------------------------------------------------------------------------------------------
contador  =  1
suma  =  0
while  contador  <=  10 : #Ciclo
    number  =  int ( input ( "Ingrese la nota"  +  ""  +  str ( contador ) +  "=" ))
    if  contador  ==  1 :
        suma  +=  número
    if  contador  ==  2 :
        suma  +=  número
    if  contador  ==  3 :
        suma  +=  número
    if  contador  ==  4 :
        suma  +=  número
    if  contador  ==  5 :
        suma  +=  número
    if  contador  ==  6 :
        suma  +=  número
    if  contador  ==  7 :
        suma  +=  número
    if  contador  ==  8 :
        suma  +=  número
    if  contador  ==  9 :
        suma  +=  número
    if  contador  ==  10 :
        suma  +=  número
    contador  +=  1
print ( "El promedio de las notas es ="  +  ""  + str ( suma / 10 ))
print("\n")

#Ejericio 49---------------------------------------------------------------------------------------------------------------------------
suma  =  0
contador  =  0
promedio  =  0
mas  =  "verdadero"
while  mas  ==  "true" : #Bucle para volver a pedir notas hasta que el usuario lo desee
    nota2  =  float ( input ( "Ingrese la nota =" ))
    if  nota2  >  0 :
        suma  =  suma  +  nota2
        contador +=  1
    mas  =  str ( input ( "¿Quieres ingresar más notas? true o false =" ))
    if  mas  ==  "falso" :
        break
print ( "El promedio de notas es ="  +  "" +  str ( suma / contador ))
print("\n")

#Ejericio 50---------------------------------------------------------------------------------------------------------------------------
contador1  =  0
suma1  =  0
contador2  =  0
suma2  =  0
contador3  =  1
mas  =  "si"
while  mas  ==  "si" : #Bucle para que itere hasta que el usuario lo desee
    number  =  int ( input ( "Ingrese un número #"  +  str ( contador3 ) +  "=" ))
    mas  =  str ( input ( "¿Quieres ingresar más números? si o no =" ))
    if  mas  ==  "si" :
        if  número  %  2  ==  0 :
            suma1  =  suma1  +  número
            contador1  +=  1
        else:
            suma2  =   suma2  +  número
            contador2  +=  1
        contador3  +=  1
promedioPar  =  suma1  /  contador1
promedioImpar  =  suma2  /  contador2
print ( "El promedio de los números pares es ="  +  ""  +  str ( promedioPar ) +  "y"  +  "el promedio de los números impares es ="  +  ""  +  str ( promedioImpar ))
print("\n")

#Ejericio 51---------------------------------------------------------------------------------------------------------------------------
agregar  =  "si"
while  agregar  ==  "si" :
    number  =  int ( input ( "Ingrese un número =" ))
    if número  >  0 :
        print ( "El número ingresado es =" , number )
        break
    else:
        print ( "No se pueden ingresar número negativos, vuélvalo a intentar" )
print("\n")

#Ejericio 52---------------------------------------------------------------------------------------------------------------------------
contador  =  1
contador2  =  0
contador3  =  0
menores  = []
mayores  = []
agregar  =  "si"
while  agregar  ==  "si" :
    number  =  int ( input ( "Ingrese un número"  +  ""  +  str ( contador ) +  "=" ))
    agregar  =  str ( input ( "¿Quieres ingresar otro número? si o no =" ))
    if número  >  100 :
        mayores . añadir ( número )
        contador2  +=  1
    else:
        if  número  <  100 :
            menores . añadir ( número )
            contador3  +=  1
    contador  +=  1
    if agregar  ==  "no" :
        break
print ( "Hay"  +  ""  +  str ( contador3 ) +  ""  +  "números menores a 100 y estos son ="  +  str ( menores ))
print ( "Hay"  +  ""  +  str ( contador2 ) +  ""  +  "números mayores a 100 y estos son ="  +  str ( mayores ))
print("\n")

#Ejericio 53---------------------------------------------------------------------------------------------------------------------------
contador = 1
contador2 = 0
contador3 = 0
contador4 = 0
contador5 = 0
negativos = []
pares = []
impares = []
mOcho = []
agregar = "si"
while agregar == "si":
    number = int(input("Ingrese un número " + " " + str(contador) + " = "))
    agregar = str(input("¿Quieres ingresar otro número? si o no = "))
    if number < 0:
        negativos.append(number)
        contador2 += 1
    else:
        if (number % 2 == 0) and (number // 8 != 0):
            pares.append(number)
            contador3 += 1
            mOcho.append(number)
            contador5 += 1
        else:
            if number % 2 != 0:
                impares.append(number)
                contador4 += 1
    contador += 1
    if agregar == "no":
        break
print("Hay" + " " + str(contador2) + " " + "números negativos y esos son =" + str(negativos))
print("Hay" + " " + str(contador3) + " " + "números pares y esos son =" + str(pares))
print("Hay" + " " + str(contador5) + " " + "números múltiplos de ocho y esos son =" + str(mOcho))
print("Hay" + " " + str(contador4) + " " + "números impares y esos son =" + str(impares))
print("\n")

#Ejericio 54---------------------------------------------------------------------------------------------------------------------------
contador  =  0
contadorPar  =  0
contadorImpar  =  0
contadorCinco  =  0
agregar  =  "si"
while  agregar  ==  "si" :
    number  =  int ( input ( "Ingrese un número para calcular los 10 números pares (se puede ingresar varias veces el 5)" +  ""  +  str ( contador ) +  "=" ))
    if  número  %  2  ==  0 :
        contadorPar  +=  1
    else:
        if  número  ==  5 :
            contadorCinco  +=  1
        else:
            if  número  %  2  !=  0 :
                contadorImpar  +=  1
    contador  +=  1
    if  contadorPar  ==  10 :
        break
    if  contadorCinco  ==  20 :
        break
print ( "Hay"  +  ""  +  str ( contador ) +  ""  +  "números en total."  +  " \ n "  +  "Hay"  +  ""  +  str ( contadorPar ) +  ""  +  "números pares."  +  " \ n "  +  "Hay"  +  ""  +  str ( contadorImpar ) +  ""  +  "números impares. "  +  " \ n " +  "Hay"  +  "" +  str ( contadorCinco ) +  ""  +  "números 5." )
print("\n")

#Ejericio 55---------------------------------------------------------------------------------------------------------------------------
número1  = []
agregar  =  "si"
while  agregar  ==  "si" :
    number  =  int ( input ( "Ingrese un número =" ))
    for i in range (1 , número  +  1 ):
        if número  %  i  ==  0 :
            número1 . añadir ( i )
    print ( "Los divisores de"  +  ""  +  str ( número ) +  ""  +  "son ="  +  str ( número1 ))
    agregar  =  str ( input ( "¿Quieres ingresar un nuevo número? si o no =" ))
    if agregar  ==  "no" :
        break
print ( "El programa ha finalizado." )
print("\n")

#Ejericio 56---------------------------------------------------------------------------------------------------------------------------
cadena = input("Ingrese una oración para mostrarla a la inversa = ")
for i in reversed(cadena):
    print("La cadena a la inversa es = ",i)
print("\n")

#Ejericio 57---------------------------------------------------------------------------------------------------------------------------
for  i  in range( 1 , 10 + 1 ):
    for  j  in range( 1 , i + 1 ):
        print ( j , end = "" )
    imprimir ( "" )
print("\n")





