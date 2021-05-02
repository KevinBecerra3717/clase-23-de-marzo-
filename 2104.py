#01
datos  = [ 0 , 0 , 0 , 0 , 0 , 0 ]
for i in range ( 1 , 7 ):
    datos [ i - 1 ] =  int ( input ( "Dime el dato número {}:" . formato ( i )))
print ( "Los datos al revés son:" )
for i in range( 6 , 0 , - 1 ):
    imprimir ( datos [ i - 1 ])

#02
#En Python, los arrays pueden ir aumentando de tamaño.
datos  = []
for i in range( 1 , 7 ):
    nuevoDato  =  int ( input ( "Dime el dato número {}:" . format ( i )))
    datos . añadir ( nuevoDato )
print ( "Los datos al revés son:" )
for i in range( 6 , 0 , - 1 ):
    imprimir ( datos [ i - 1 ])

#03
datos = [5, 6, 7, 8, 9]
for i in range(0, 5):
    print(datos[i], end="")
print()

datos.eliminar(6)
for i in range(0, len(datos)):
    print(datos[i], end="")
print()

datos[0] = - 2
for i in range(0, len(datos)):
    print(datos[i], end="")
print()

datos.insertar(1, 23)
for i in range(0, len(datos)):
    print(datos[i], end="")
print()

datos = datos + [31, 32, 33]
for i in range(0, len(datos)):
    print(datos[i], end="")
print()

#04
datos  = [ 0  for i in range ( 20 )]
for i in range( 0 , len ( datos )):
    datos [ i ] =  int ( input ( "Dime el dato numero {}:" . formato ( i + 1 )))
print ( "Los datos al reves son:" )
for i in range( len ( datos ), 0 , - 1 ):
    print( datos [ i - 1 ])

#05
datos  = {}
for i in range ( 1 , 7 ):
    datos [ i - 1 ] =  int ( input ( "Dime el dato numero {}:" . formato ( i )))
print ( "Los datos al reves son:" )
for i in range( 6 , 0 , - 1 ):
    print( datos [ i - 1 ])

#06
datos  = [
    [ "uno" , 2 ],
    [ "a" , "b" , "c" ]
]
print( datos )

#07
datos  = [[ 0  for colmna in range ( 0 , 5 )] for fila in range ( 0 , 4 )]
datos [ 0 ] [ 2 ] =  5
imprimir ( datos )


