#01
numero  =  0
while numero  <=  10 :
    imprimir ( numero )
    numero  +=  1

#02
anio  =  2010
while anio  <=  2012 :
    print ( "Informes del Año" , str ( anio ))
    anio  +=  1

#03
numero  =  0
suma  =  0
while numero <=  10 :
    suma  =  numero  +  suma
    numero  +=  1
print ( "La suma es ="  +  ""  +  str ( suma ))

#04
contar  =  0
total  =  0
print ( "Ingresa la nota de un estudiante (-1 para salir):" )
grado  =  int ( entrada ())
while  grado  !=  - 1 :
    total  =  total  +  grado
    contar  =  contar  +  1
    print ( "Ingresa la nota de un estudiante (-1 para salir):" )
    grado  =  int ( entrada ())
promedio  =  total  /  contar
print ( "Promedio de notas del grado escolar es:"  +  str ( promedio ))

#05
contar  =  1
contar2  =  0
total  =   0
notas  =  int ( input ( "¿Cuántas notas desea ingresar? =" ))
while  contar  <=  notas :
    grado  =  int ( input ( "Ingrese la nota =" ))
    total  =  total  +  grado
    contar  +=  1
    contar2  += 1
promedio  =  total  /  contar2
print ( "Promedio de notas del grado escolar:"  +  str ( promedio ))


