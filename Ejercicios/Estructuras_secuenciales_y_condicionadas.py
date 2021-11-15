'''
    Ejercicio: 1
    Calcula el área de un trapecio isósceles 
'''

# Entrada
c1 = float(input('Base 1: '))
c2 = float(input('Base 2: '))
c3 = float(input('Base 3: '))

def areaTrapecio(c1,c2,c3): 
    '''
        Para conseguir encontrar el área de un trapecio
        isósceles multiplicaremos primero la altura por sus
        bases y por último lo dividimos entre 2.

    '''
    # Lógica
    b = (c1 - c2) / 2
    h = (c3 ** 2 - b ** 2) ** 0.5
    area = (c2 * h) + (b * h)
    return area

# Asignamos la función a una variable global
area = areaTrapecio(c1, c2, c3)
# Formateamos la salida y redondeamos la salida con la función round()
print('El área del trapecio es {}'.format(round(area, 2)))


'''
    Ejercicio: 2
    Calcula el precio según los kwh que hemos consumido, a mayor
    consumición, menor es el precio * kwh.
'''

# Entrada 
kwh = float(input('Consumo: '))

def factura_electronica(kwh):
    ''' 
        Menos de 1000 kWh 0.14 euros/kWh 
        Igual o más de 1000 y menos de 2000 kWh 0.15 euros/kWh 
        Igual o más de 2000 y menos de 5000 kWh 0.16 euros/kWh 
        Igual o más de 5000 kWh 0.17 euros/kWh 
    '''

    # Lógica
    if kwh < 1000 and kwh > 1:
        price = 0.14
    elif kwh >= 1000 and kwh > 2000:
        price = 0.15
    elif kwh >= 2000 and kwh > 5000:
        price = 0.16
    elif kwh >= 5000 and kwh > 2000:
        price = 0.17
    
    # Operación que calcula lo consumido por el precio
    price = kwh * price
    return price

# Llamada a la función
factura_x = factura_electronica(round(kwh, 2))
print('Su factura es de: {}€'.format(factura_x))


'''
    Ejercicio: 3
    Devuelve la calificación sobre una nota desde la D a A+.
'''

# Entrada
x = float(input('Introduce una nota: '))

def notas(x):
    '''
        Por medio de un condicional y operadores lógicos
        obtendremos la nota según la puntuación del alumno.

        Rango: 
        0 a 1.99 (D)
        2.0 a 2.99 (C)
        3.0 a 3.49 (B)
        3.50 a 3.99 (A)
        4 (A+)
        - 0 O > 4 'Error'
    '''
    
    # Lógica 
    if x >= 0 and x < 2.0:
        print('D')
    elif x >= 2.0 and x < 3.0:
        nota = 'C'
    elif x >= 3.0 and x < 3.49:
        nota = 'B'
    elif x >= 3.50 and x < 3.99:
        nota = 'A'
    elif x == 4.0:
        nota = 'A+'
    else:
        nota = 'Error en nota'
    return nota

# Llamada a la función
nota = notas(x)
print('La nota obtenida es: {}'.format(nota))


'''
    Ejercicio: 4
    Este programa nos dice el tipo de triangulo que es
    según los el valor de sus lados.
'''

# Entrada
a = int(input('Lado A: '))
b = int(input('Lado B: '))
c = int(input('Lado C: '))

def triangulo(a, b, c):
    '''
        Por medio de un condicional obtendremos el tipo
        de triangulo según sus lados.

        Escaleno: lados no iguales
        Equilátero: lados iguales
        Isósceles: 2 lados iguales
    '''
    
    # Lógica
    if a != b and a != c and b != c:
        result = 'Triángulo escaleno'
    elif a == b and a == c and b == c:
        result = 'Triángulo equilátero'
    elif a and b != c:
        result = 'Triángulo Isósceles'
    return result

# Llamada a la función
tipo = triangulo(a, b, c)
print(tipo)


'''
    Ejercicio: 5
    Este programa devuelve un diagnóstico según los valores
    que obtenga, basado en un termómetro.

'''

# Entrada 
x = float(input('Temperatura: '))

def temp(x):
    '''
        El parámetro (x) es la entrada de teclado que
        según lo que devuelva cada condición, la función
        retornará el resultdo en la variable (result).

        Diagnósticos disponibles:
            - Hipotermia 
            - Normal
            - Febrícula
            - Fiebre
        La funcón retornará "Fuera de rango" por debajo de
        30 y por encimma de 46.
    '''
    # Lógica
    if x >= 30.0 and x < 35.5:
        result = 'Hipotermia'
    elif x >= 35.5 and x < 37.2:
        result = 'Normal'
    elif x >= 37.2 and x < 38.0:
        result = 'Febrícula'
    elif x >= 38.0 and x <= 46.0:
        result = 'Fiebre'
    else:
        result = 'Fuera de rango'
    return result

# Llamada a la función
diagnostico = temp(x)
print('El diagnóstico es: {}'.format(diagnostico))
