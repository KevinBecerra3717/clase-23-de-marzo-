#01
#EJERCICIO PROPUESTO
lista_multiplos = []
agregar = "True"
while agregar == "True": #Un bucle para que calcule todas las veces que requiera el usuario
    tamaño_arreglo = int(input("Ingrese el tamaño del arreglo = "))
    numero_multiplos = int(input("Ingrese el número de múltiplos = "))
    for i in range (1,tamaño_arreglo+1): #Se determina un range el cual va desde 1, y el mimos valor que se ingresa en la variable se va incrementenado en 1.
        lista_multiplos.append(i*numero_multiplos)
    print ("Los" + " " + str(tamaño_arreglo) + " " + "múltiplos de " + " " + str(numero_multiplos) + " " + "son = " + " " + ", ".join(map(str,lista_multiplos)))
    agregar = str(input("Quieres agregar más valores? True or False = "))
print('Ha terminado el programa exitosamente.')

#02
A = int(input("¿Cuántos nombres de personas quieres ingresar? =  "))
B = []
C = []
x=0
y=0
for i in range (0,A): #Range agrega los nombres a la lista hasta el límite que se determina en la variable A.
 B.append(input("Ingresa el nombre de una persona a la que quieras agregrar a la lista = "))
print ("Estos son todos los nombres: " + ", ".join(B) + ":")
for j in range (0,A): #Range cuenta la cantidad de carácteres de cada valor ingresado determinado por la variable A.
 C.append(len(B[j]))
 print("  -  El nombre",B[x],"tiene",C[y],"letras.")
 x=x+1
 y=y+1

 #03
 suma = 0
 materias = ["Matemáticas", "Física", "Química", "Historia", "Lenguaje"]  # lista con las materias principales
 lista = []  # lista en la cual seran almacenados datos
 for subject in materias:  # for el cual sirve para sacar los pbjetod de la lista por orden y almacenarlos en subject
     score = input("¿Qué nota has sacado en " + subject + "? = ")
     suma = suma + int(score)  # es un  acomulador
     lista.append(score)  # agregar valores a la lista
 for i in range(len(materias)):  # sacar el indice(lista) de cada materia y poder sacarlas a pantalla mas adelante
     print(" - En " + materias[i] + " has sacado " + lista[
         i])  # con el indice(lista) almacenado en i podemos sacar en pantalla cada materia
 print("El promedio de todas sus notas es =", suma / 5)

 #04
 # EJERCICIO - MEJORA 1
 datos = []
 limite = int(input("¿Cuántos números desea ingresar? ="))
 for i in range(0, límite):
     n = (int(input("Ingrese un número =")))
     datos.añadir(n)
 print(datos)
# EJERCICIO 2
datoss = [2, - 10, 52, 1012]
for i in range (0, len(datoss)):
    print(datoss[i], end="")
print()
# EJERCICIO 3
datos = []
datoss = datos.insertar(1, 11)
for i in range(0, len(datos)):
    print(datos[i], end="")
print()
# EJERCICIO 4
datos = [1, 5, 99, 2]
datos.quitar(5)
for i in range(0, len(datos)):
    print(datos[i], end="")
print()
# EJERCICIO 5
datos = []
datos = datos + [21, 22]
for i in range (0, len(datos)):
     print(datos[i], end="")
imprimir()

#05
import  string  #Importar la biblioteca de Python.
def  listAlphabet (): # La función llama a string.ascii_lowercase, que es igual al alfabeto.
     return ( cadena . ascii_lowercase )
lisst  =  listAlphabet () # Define la lista.
for  i  in  range ( len ( lisst ), 1 , - 1 ): #Loop para que use range para contar el alfabeto uno por uno.
    if  i  %  3  ==  0 : # Condición si la posición de la letra es múltiplo de 3 desaparece.
        lisst . pop ( i - 1 ) # Elimina esta letra debido a la última condición.
print ( "La lista es =" , "," . join ( lisst ))

#06
agregar  =  "sí"
while  add  ==  "yes" : # El bucle tiene la función de iterar hasta que el usuario lo decida.
    palabra  = entrada ( "Introduzca la palabra =" )
    inverted_word  =  word  # Empareja la nueva variable con la anterior.
    palabra  =  lista ( palabra )
    reversed_word  =  lista ( reversed_word )   #Become una lista.
    palabra_inversa . reverso ()
    if palabra  ==  reversed_word:
        print ( "Es un palíndromo" )
    else:
        print ( "No es un palíndromo" )
    add  =  str ( input ( "¿Quieres añadir una nueva palabra? sí o no =" )) #Esta variable es para continuar o interrumpir el ciclo.
print ( "El programa ha terminado" )

#07
#Creación cuenta
user = input("Ingrese el nombre de usuario que quiera usar para esta cuenta = ")
add = input("¿Desea Crear una contraseña segura? si o no = ")
if add == "si":
    #creacion de un cotraseña aleatoria
    import random #Importan la librería para generar números aleatorios
    lista=[]
    cond="si"
    numero=random.randint(1,100) #Generar números aleatorios.
    while cond=="si":
            cadena=input("Ingrese por favor una frase o letra para tu contraseña aleatoria = ")
            lista.append(cadena) #Se agrega a la lista predeterminada con el .append
            cond=input("¿Quieres ingresar otra frase o letra para tu contraseña? = ")
    lisy= random.sample(lista,1) #Se genera de manera aleatoria.
    print("".join(lisy) + str(numero)) #Se retira los paréntesis
else:
    password_new = input("Ingrese la contraseña = ")
#Validación de datos
user_Inicio = input("Ingrese su nombre de Usuario = ")
password_Incion = input("Ingrese su contraseña = ")
if password_Incion == ("".join(lisy) + str(numero)) and user==user_Inicio: #Se determina una condición para así poder evaluar si los datos ingresados son iguales a los creados anteriorimente.
    print("Datos son correctos, será redirigido a la pantalla principal en pocos minutos.")
elif password_Incion== ("".join(lisy) + str(numero)) and user==user_Inicio:
    print("Datos son correctos, será redirigido a la pantalla principal en pocos minutos.")
else:
    print("Los datos son incorrectos.") 