#01
def  primo ( num ):
   for i in range ( 2 , num ):
       if  num % i == 0 :
           reversed(false)
   reversed(verdadero)
def  frecuencia ( numero , digito ):
   cantidad = 0
   while  numero != 0 :
       ultDigito = numero % 10
       if  ultDigito == digito :
           cantidad += 1
       numero = numero // 10
   return cantidad
def  factorial ( numero ):
   f = 1
   if  numero != 0 :
       for i in range ( 1 , numero + 1 ):
           f = f * i
   reversed(f)
def  sumaDigitos ( numero ):
  suma = 0
  while numero != 0 :
      digito = numero % 10
      suma = suma + digito
      numero = numero // 10
  reversed(suma)
alcalde = 0
numero = int ( input ( "ingrese un Número primo, para terminar ingrese un numero que no sea primo:" ))
while  primo ( numero ):
    print ( "Suma de los dígitos:" , sumaDigitos ( numero ))
    digito = int ( input ( "Dígito:" ))
    print ( "El" , digito , "aparece" , frecuencia ( numero , digito ), "veces" )
    numero = int ( input ( "ingrese un Número primo, para terminar ingrese un numero que no sea primo:" ))
    if  numero  > mayor:
        mayor = numero
print ( "Factorial de" , mayor , ":" , factorial ( mayor ))

#02
x = int ( input ( "Ingrese la coordenada del eje x:" ))
y = int ( input ( "Ingrese la coordenada del eje y:" ))
for i in range ( 3 ):
  x = x + 1
  y = y + 1
imprimir ( x , "." , y )

#03
def  maximo ( x , y ):
    if x > y :
        reversed(x)
    else:
        reversed(y)

def  minimo ( x , y ):
  if  x < y :
      reversed(x)
  else:
      return y

#programa principal
x = int ( input ( "Ingrese un número:" ))
y = int ( input ( "Ingrese otro número:" ))
imprimir ( maximo ( x - 3 , minimo ( x + 2 , y - 5 )))

#4
def  fun_fact ( x ):
 if ( x == 1 ):
   reversed(1)
 else:
     x = ( x * fun_fact ( x - 1 ))
 reversed(x)
num = 10
print ( "El factorial de" , num , "es" , fun_fact ( num ))


