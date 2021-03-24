for i in range(9):
    print(i)

for i in range(3, 13):
    print(i)

for n in range(3, 13, 2):
    print(n)

for i in range(11,4):
    print(i)

for i in range(11, 4, -1):
    print(i)

for i in range(2, 10, 2):
    print(i)

for i in range(2, 10, 2):
        print(i)

for i in range(2, 10, 3):
    print(i)

for i in range(10, 5, -1):
    print(i)

for i in range(3, -1, -1):
    print(i)

for i in range(21):
    print (i, i ** 3)

for i in range(10, 0, -1):
    print(i)
print("Feliz año nuevo!")

for i in [0,1,2,3,4]:
    print("Hola")

for i in range(5):
  print ("Ahora i vale",i,"y su cuadrado", i**2)

for i in ['JLo', 'Benito', 'Rosalia', 2021]:
  print ("Hola. Ahora i vale",i)

'''
Escribir el código para un bucle tipo for el cual imprime desde número 0 hasta el 7,
utiliza una variable auxiliar llamada n
'''
for n in range(8):
    print(n)

print("------------------------------------------")


for n in range(1,13,):
    print(n)

c = 0
for i in range(1000):
    ultimo_digito = (i ** 3) % 10
    if ultimo_digito == 7:
        c = c + 1
print(c)


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