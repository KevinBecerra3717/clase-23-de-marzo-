#01
número  =  int ( input ( "Ingrese un número =" ))
if número  %  5  ==  0 and número  %  3  ==  0 :
    print ( "El número cumple." )
else:
    print ( "El número no cumple." )

#02
contador  =  1
suma  =  0
while  contador  <=  3 :
    nota  =  float ( input ( "Ingrese la nota"  +  ""  +  str ( contador ) +  "=" ))
    if ( nota  >=  0 ) and ( nota  <=  10 ):
            if contador  ==  1 :
                suma  +=  nota
            if contador  ==  2 :
                suma  +=  nota
            if  contador  ==  3 :
                suma  +=  nota
            contador  +=  1
            promedio  =  suma  /  3
if promedio  >= 7:
    print ( "Obtuvo un promedio de"  +  str ( promedio ) +  "y es promocionado." )
elif  promedio  >=  4  and  promedio  <  7 :
    print ( "Obtuvo un promedio de"  +  str ( promedio ) +  "y es regular." )
else:
    print ( "Obtuvo un promedio de"  +  str ( promedio ) +  "y no está habilitado." )

#03
nota1  =  int ( input ( "Ingrese la primera nota =" ))
nota2  =  int ( input ( "Ingrese la segunda nota =" ))
nota3  =  int ( input ( "Ingrese la tercera nota =" ))
promedio  = ( nota1  +  nota2  +  nota3 ) /  3
if promedio  >=  7 :
    imprimir ( "Promocionado: D" )
if promedio  >=  4  and  promedio  <  7 :
    imprimir ( "Regular: 7" )
if promedio  <  4 :
    print ( "No habilitado: c" )
