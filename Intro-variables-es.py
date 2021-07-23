'''
Existen algunas restricciones a la hora de nombrar una variable que hay que tener en cuenta:

    - No pueden empezar por números
    - Si es multipalabra no puede contener espacios
    - No pueden contener caracteres especiales
    - No se pueden utilizar las palabras reservadas de Python 
'''

# Variables con números
v5 = 5  # Si
5v = 5  # No

# Strings / multipalabra
nombreUsuario = "Cristina"  # Si
nombre Usuario = "Cristina" # No


# Palabras reservadas de Python en el módulo Keyword
['False', 'None', 'True', 'and', 'as', 'assert', 
'async', 'await', 'break', 'class', 'continue', 
'def', 'del', 'elif', 'else', 'except', 'finally', 
'for', 'from', 'global', 'if', 'import', 'in', 'is', 
'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 
'return', 'try', 'while', 'with', 'yield']

# Buenas prácticas al definir variables en Python:

# Camel Case.
nombreUsuario = 'a'

# Pascal Case.
NombreUsuario = 'b'

# Snake Case (Recomendado)
nombre_usuario = 'c'

#Kebab Case.
nombre-usuario = 'd'


'''
Creando diferentes tipos de variables como:
string, integer, float.
'''

# Numéricas como enteros: int
n = 2
n  # Salida: 2

# Numéricas como decimales: float
n = 2.0
n  # Salida: 2.0

# Cadenas de texto: string
s = "Hola"
s  # Salida: Hola


'''
En Python no importa el tipo de comillas que utilices a la hora de construir un string, puedes usar 
las dobles "" o simples ''. También puedes utilizar comillas, saltos de línea, tabulación horrizontal 
o backslash dentro del mismo string
'''

# Ejemplo 1
nombre_usuario = "Silvia"
print('Hola ') + nombre_usuario + (' .')  
# Salida: Hola Silvia.

# Ejemplo 2
nombre_usuario = "Daniel"
m = "Hola \"" + nombre_usuario + "\""
print(m)  
# Salida: Hola "Daniel"


'''
En Python como en otros lenguajes de programación existen las listas o Arrays y necesarios para proyectos
de mucho código, aunque la segunda requiere de la librería NumPy.
'''

# Se necesita seguir la secuencia: nombre_usuario = 1 posición, password = 2 posición y role = 3 posición
nombre_usuario, password, role = "SuperBowl", "xxxxxxx", 2


'''
En cuanto a las operaciones entre variables cuyo valor es numérico o entre números, podemos realizar 
desde la más básica a la más compleja. Para realizar operaciones con números complejos deberás de 
importar la librería cmath, en este caso realizaremos una operación básica que estarán implicados 
los operadores de suma + y de resta -.
'''

x = 2
y = 100 + x
y -= 50 
print(y) 
# Salida: (52) de la suma de x + y - 50


'''
Con la función type() podremos saber el tipo de dato que tenemos almacenado en una variable, bien sea int, 
float, str, etc. 
'''

type('Hola') # Salida: str
type(5)      # Salida: int
type(4.)     # Salida: float

# Ejercicio con operaciones
x = 0.5

x = 5 * x * (12 - x)
print(x)
# Salida 28.75

# Operación
12 - x = 11.5
5 * x = 2.5
x = 11.5 * 2.5

print(x)
# salida 28.75
