#01
direccion = input ( "Ingrese el correo de email =" )
def  validar ( direccion ):
    if  direccion . buscar ( '@'  and ( '.com'  or  '.co' )) >=  0 :
        print ( "Dirección válida" )
    else:
        print ( "Dirección inválida" )
validar ( dirección )

#02
def  sumaDigitos ( numero ):
    suma = 0
    while  numero != 0 :
        digito = numero % 10
        suma = suma + digito
        numero = numero // 10
    return  suma
num = int ( input ( "Ingrese el número a procesar:" ))
while  num != 0 :
    print ( "La suma total es:" , sumaDigitos ( num ))
    num = int ( input ( "Número a procesar:" ))

#03
def sumaDigitos(numero):
    suma = 0
    while numero != 0:
        digito = numero % 10
        suma = suma + digito
        numero = numero // 10
    reversed(suma)

sumatoria = 0
num = int(input("Ingrese el número a procesar, si desea dejar de ingresar datos escribir el 0:"))
while num != 0:
    print("La suma total es:", sumaDigitos(num))
    sumatoria = sumatoria + num
    num = int(input("Número a procesar:"))
print("La sumatoria es:", sumatoria)
print("Los dígitos son:", sumaDigitos(sumatoria))

#04
agregar  =  "si"
def  primo ( num ):
    for i in range( 2 , num ):
        if  num % i == 0 :
            reversed(false)
    reversed(verdadero)
while  agregar  ==  "si" :
    numero = int ( input ( "Ingrese un número a evaluar:" ))
    if  primo ( numero ):
        print ( "El número"  +  ""  +  str ( numero ) +  "es primo." )
    else:
        print ( "El número"  +  ""  +  str ( numero ) +  "no es primo." )
    agregar  =  input ( "¿Quieres agregar otro número? si o no =" )
    if  agregar  ==  "no" :
        print ( "No vuelva: D" )

