def sumar(): #Definimos la función sumar
    x = a + b
    print (("Resultado"), (x))
def restar():#Definimos la función restar
    x = a - b
    print (("Resultado"), (x))
def multiplicar():#Definimos la función multiplicar
    x = a * b
    print (("Resultado"), (x))
def dividir():#Definimos la función dividir
    x = a / b
    print (("Resultado"), (x))

##########################################-2-###################################################
while True: #
    try: #Intentamos obtener los datos de entrada
        a = int(input("Ingresa el primer numero: \n")) #
        b = int(input("Ingresa el segundo numero: \n"))#
        print (("Que cálculo quieres realizar entre"), (a), ("y"), (b), ("?\n")) #
        op = str(input(""" #Ofrecemos las opciones de cálculo que van a llamar a las funciones
        1- Sumar
        2- Restar
        3- Multiplicar
        4- Dividir \n"""))
    except: #En caso de error:
        print ("Error")
        op = '?'
##########################################-3-##################################################
    if op == '1':#
        sumar()
        break
    elif op == '2':#Si el usuario elige opción 1 llamamos a restar
        restar()
        break
    elif op == '3':#
        multiplicar()
        break
    elif op == '4':#Si el usuario elige opción 1 llamamos a dividir
        dividir()
        break
    else:
        print ("""Has ingresado un numero de opcion erroneo""") #En caso que el número no
def sumar(): #Definimos la función sumar
    x = a + b
    print (("Resultado"), (x))
def restar():#Definimos la función restar
    x = a - b
    print (("Resultado"), (x))
def multiplicar():#Definimos la función multiplicar
    x = a * b
    print (("Resultado"), (x))
def dividir():#Definimos la función dividir
    x = a / b
    print (("Resultado"), (x))

##########################################-2-###################################################
while True: #
    try: #Intentamos obtener los datos de entrada
        a = int(input("Ingresa el primer numero: \n")) #
        b = int(input("Ingresa el segundo numero: \n"))#
        print (("Que cálculo quieres realizar entre"), (a), ("y"), (b), ("?\n")) #
        op = str(input(""" #Ofrecemos las opciones de cálculo que van a llamar a las funciones
        1- Sumar
        2- Restar
        3- Multiplicar
        4- Dividir \n"""))
    except: #En caso de error:
        print ("Error")
        op = '?'
##########################################-3-##################################################
    if op == '1':#
        sumar()
        break
    elif op == '2':#Si el usuario elige opción 1 llamamos a restar
        restar()
        break
    elif op == '3':#
        multiplicar()
        break
    elif op == '4':#Si el usuario elige opción 1 llamamos a dividir
        dividir()
        break
    else:
        print ("""Has ingresado un numero de opcion erroneo""") #En caso que el número no
