
import pytest 
import aplicacion as apl

#  Ordenar de forma ascendente una arreglo de n números enteros.
def Ordenar():
    #  print('Ingrese sus numeros: ', end = '')
    #  num = list(map(int, input().split()))
    num = [1, 7, 4, 5]
    num.sort(reverse=False)
    #  print(num)
    y=1
    if y == 1:
        return y

#  Dado un diccionario con la estructura [{nombre:N, edad:M},{nombre:N,edad:M},...], contar el número de personas mayores de edad y devolver el total.

def Mayores(personas):
    numMay = len(personas)
    print('Personas en el diccionario:')
    print(numMay)
    print('Personas mayores de edad en el diccionario:')

    i = 0
    for j in personas:
        if j['edad'] >= 18:
            i += 1
    return i