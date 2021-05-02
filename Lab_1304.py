#Método 1
def  resta (a, b):
    volver (a - b)
print( resta (30, 10 ))
#Metodo 2
operacion = lambda a, b: a - b
print( operacion (30 , 10 ))

#02
result  =  ord ( 'a' ) # La función ord nos retorna un valor respectivo a lo ingresado de acuerdo a la tabla Unicode
print ( result ) #Devuelve el número 97, ya que es respectivo a la letra ingresada
'' '----------------------------------------------- -------------------------------------------------- '' '
result2  =  ord ( '$' ) # La función ord nos retorna un valor respectivo a lo ingresado de acuerdo a la tabla Unicode
print ( result2 ) #Devuelve el número 36, ya que es respectivo al símbolo ingresado

#03
cadena  =  'python'  #Ingresa la cadena
print ( list ( reverse ( cadena ))) # Devuelve el valor de python al revés en forma de lista ['n', 'o', 'h', 't', 'y', 'p'

#04
import  math  #Se importa la librería math de python
a  =  float ( input ()) #Se establece la primera entrada de datos, en este caso el valor a
b  =  float ( input ()) #Se establece la primera entrada de datos, en este caso el valor b
def  suma ( a , b ): #Define la función
    return matemáticas . floor ( a  +  b ) #Return para desarrollara la operación y el uso de la librería importada
print ( suma ( a , b )) #Devuelve la suma respectiva a los valores ingresados

#Deco_1
#Decorador
# a (b) -> c
def  my_costume_decorator ( función ): #Funcion_b = saludar
    def  wrapper ( * args , ** kwargs ): # parámetros argumentos * args, ** kwargs
        return function ( * args, ** kwargs ) #Funcion_b 
     return wrapper
@ my_costume_decorator
def  saludar (): #Saludar por medio de @funcion_a se convierte en el parámetro funcion_b
    print( 'Hola' )
#NUEVO
@ my_costume_decorator
def  suma ( a , b ):
    return  a  +  b
print(suma ( 10 , 30 ))
