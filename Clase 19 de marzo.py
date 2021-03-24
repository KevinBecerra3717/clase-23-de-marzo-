for i in range(9):  # Va de 0 hasta 8 siendo el 9 exclusivo
    print(i)

for i in range(3, 13): #Va de 3 hasta 12, y el 13 es exclusivo
    print(i)

for n in range(3, 13, 2): #Va de 3 hasta 11, porque va de 2 en 2
    print(n)

for i in range(11,4): #Nada, porque la salida no es correcta.
    print(i)

for i in range(11, 4, -1): # Va desde 11, porque al ingresar un -1 vamos de derecha a izquierda(decreciendo).
    print(i)

for i in range(2, 10, 2): # Va desde 2 hasta 8  y va de 2 en 2, siendo 10 exclusivo.
    print(i)

for i in range(2, 10, 2):  # Va desde 2 hasta 8  y va de 2 en 2, siendo 10 exclusivo.
        print(i)

for i in range(2, 10, 3): # Va desde 2 hasta 8 y va de 3 en 3, siendo 10 exclusivo.
    print(i)

for i in range(10, 5, -1): #Va desde 10 hasta 5, pero el 5 es exclusivo y va de derecha a izquierda.
    print(i)

for i in range(3, -1, -1): # Va desde 3 hasta -1, siendo -1 exclusivo, y yendo de derecha a izquierda
    print(i)

for i in range(21): #Se utiliza el for para darle a la variable i un rango hasta 21
    print (i, i ** 3)  #Se imprime el número que se va elevando, y seguido de eso el resultado de esta operación.

for i in range(10, 0, -1): #Se utiliza el rango para darle a la variable i un rango de (10,0,-1)
    print(i)  #Se imprime los números del 10 hasta el 1 siendo 0 exclusivo.
print("Feliz año nuevo!") #Seguido de lo anterior se imprime la frase: Feliz año nuevo!

for i in [0,1,2,3,4]: #Se utiliza el for para darle a la variable i un rango de [0,1,2,3,4]
    print("Hola") #Imprime la  cadena o número que esté dentro del print la cantidad de veces determinadas

for i in range(5): #Se utiliza el for para darle a la variable i un rango de 5,siendo 5 exclusivo
  print ("Ahora i vale",i,"y su cuadrado", i**2)#Se imprime la variable i junto con su resultado elevado al cuadrado

for i in ['JLo', 'Benito', 'Rosalia', 2021]: #Se utiliza el for para darle a la variable i en este caso una lista
  print ("Hola. Ahora i vale",i) #Se imprime cada elemento de la lista asignado para la variable i junto con  el mensaje

'''
Escribir el código para un bucle tipo for el cual imprime desde número 0 hasta el 7,
utiliza una variable auxiliar llamada n
'''
for n in range(8):
    print(n)

print("------------------------------------------")

#Modifica el rango del bucle anterior para que ahora imprima del número 1 hasta el 12
for n in range(1,13,):
    print(n)

c = 0 #Se inicializa la variable en 0 para que acumule
for i in range(1000): #Se utiliza el for para darle a la variable i un rango de 1000,siendo 1000 exclusivo
    ultimo_digito = (i ** 3) % 10 #Se define una nueva variable que almacena una operación para ver cuáles número naturales menores 1000 tiene un cubo terminado en 7
    if ultimo_digito == 7:
        c = c + 1 #Si el residuo de la operación anterior es igual a 7 se le suma al contador un 1, contando cada número natural
print(c) #Se imprime por pantalla la cantidad de números que hay en el contador


''' 
Se desarrolla un for que de un rango hasta 3, siendo 3 exclusivo y cada uno de los números se repitan dos veces(contabilizados)
'''
for i in range (3):
  for j in range (2):
    print ("i vale", i, "y j vale", j)

''' 
La variable i toma los valores de 0 a 3 y la variable j toma los valores de 0 a i, 
por lo que cada vez el bucle interno se ejecuta un número diferente de veces
'''
for i in range (4):
  for j in range(i):
    print ("i vale", i, "y j vale", j)


#Ejemplo 1 de bucle for anidado
dibujo=''
anchura=int(input("Ingrese el valor del ancho = "))
altura=int(input("Ingrese el valor de la altura = "))

for i in range(0,altura):

    for j in range(0,anchura):
        if i ==0 or i == altura-1:
            dibujo+='*'
        elif j ==0 or j==anchura-1:
            dibujo+='*'
        else:
            dibujo +='-'
    dibujo+='\n'

print ("\n"*2)
print (dibujo)

#Ejemplo 2 de bucle for anidado
for i in [1, 2, 3]:
    for j in [11, 12]:
        print(j, end=" ")
    print(i, end=" ")