#Ejercicio 1
def validaLista(lista):
    if type(lista)!=list or lista==[]:
        return False
    else:
        return validaListaAux(lista)

def validaListaAux(lista):
    if lista==[]:
        return True
    elif type(lista[0]) in [int, float]:
        return validaListaAux(lista[1:])
    else:
        return False

def todosDiv(num, lista):
    if type(num)!=int or validaLista(lista)==False:
        raise Exception("Error")
    else:
        return todosDivAux(num, lista)

def todosDivAux(num, lista):
    if lista==[]:
        return True
    elif num%lista[0]!=0:
        return False
    else:
        return todosDivAux(num, lista[1:])

#Ejercicio 3

def iota(num):
    if type(num)!=int or num<0:
        raise Exception("Error")
    else:
        return iotaAux(0, num)

def iotaAux(i, num):
    if i==num:
        return []
    else:
        return [i] + iotaAux(i+1, num)

#Ejercicio 5

def validaLista5(lista):
    if type(lista)!=list or lista==[]:
        return False
    else:
        return validaListaAux5(lista)

def validaListaAux5(lista):
    if lista==[]:
        return True
    elif type(lista[0]) in [int, float] and 0<=lista[0]<=100:
        return validaListaAux5(lista[1:])
    else:
        return False

def notas(lista):
    if validaLista5(lista)==False:
        raise Exception("Error")
    else:
        A = lambda n:n>=70 #Aprobados
        R = lambda n:n<70 #Reprobados
        return {"Aprobados":notasAux(lista, A), "Reprobados":notasAux(lista, R), "Promedio general":(notasAuxSumatoria(lista)/len(lista))}

def notasAux(lista, func):
    if lista==[]:
        return 0
    else:
        if func(lista[0]):
            return 1 + notasAux(lista[1:], func)
        else:
            return notasAux(lista[1:], func)

def notasAuxSumatoria(lista):
    if lista==[]:
        return 0
    else:
        return lista[0] + notasAuxSumatoria(lista[1:])

#Ejercicio 7

def ulam(n):
    if type(n)!=int or n<=0:
        raise Exception("Error")
    else:
        return ulamAux(n)

def ulamAux(n):
    if n==1:
        return n # o return 1
    else:
        if n%2==0:
            return ulamAux(n//2)
        else:
            return ulamAux(n*3+1)

#Ejercicio 9

def i(l1, l2):
    if l1==[]:
        return l2
    elif l2==[]:
        return l1
    else:
        return [l1[0] + l2[0]] + i(l1[1:], l2[1:])

# i([1,3,5],[2,4,6])
# [1+2] + i([3,5],[4,6])
# [ 3 ] + [3+4] + i([5],[6])
# [ 3 ] + [ 7 ] + [5+6]
# [3, 7, 11]

#La funcion suma los elementos que se encuentran en el mismo indice y forma una nueva lista con el resultado de la suma de los indices

#Suma de vectores o suma de las filas de dos matrices

## A = [1 3 5]
##    [X X X]
##    [X X X]
## B = [2 4 6]
##    [X X X]
##    [X X X]
## C = A+B = [3 7 11]
##          [X X X ]
##          [X X X ]

#Ejercicio 11

def cuentaElem(lista):
    if type(lista)!=list:
        raise Exception ("Error")
    else:
        return cuentaElemAux(lista)

def cuentaElemAux(lista):
    if lista==[]:
        return 0
    else:
        elemento=lista[0]
        if type(elemento)!=list:
            return 1+cuentaElemAux(lista[1:])
        else:
            return cuentaElemAux(elemento)+cuentaElemAux(lista[1:])

#Ejercicio 13

def misterio(l):
    if l[2:] == []:
        return l[0] == l[1]
    else:
        return misterio(l[1:])

# misterio([8, 6, 4, 8, 1, 1])
# if [4, 8, 1, 1] == []:
# else:
# misterio([6, 4, 8, 1, 1])
# if [8, 1, 1] == []:
# else:
# misterio([4, 8, 1, 1])
# if [1, 1] == []:
# else:
# misterio([8, 1, 1])
# if [1] == []:
# else:
# misterio([1, 1])
# if [] == []:
# 1 == 1
# True

# misterio([5, 6, 14, 8, 10, 1])

# if [14, 8, 10, 1] == []:
# else:
# misterio([6, 14, 8, 10, 1])
# if [8, 10, 1] == []:
# else:
# misterio([14, 8, 10, 1])

# if [10, 1] == []:
# else:
# misterio([8, 10, 1])
# if [1] == []:
# else:
# misterio([10, 1])
# if [] == []:
# 10 == 1
# False

#La funcion compara si los ultimos dos numeros de una lista son iguales o no

#Ejercicio 15

def validaLista15(lista):
    if type(lista)!=list or lista==[]:
        return False
    else:
        return validaListaAux15(lista)

def validaListaAux15(lista):
    if lista==[]:
        return True
    elif type(lista[0])==list:
        if validaListaAuxiliar15(lista[0])==True:
            return validaListaAux15(lista[1:])
        else:
            return False
    else:
        return False

def validaListaAuxiliar15(lista):
    if lista==[]:
        return True
    elif type(lista[0]) in [int, float]:
        return validaListaAuxiliar15(lista[1:])
    else:
        return False

def largoListaIgual(lista):
    if lista[1:]==[]:
        return True
    elif len(lista[0])==len(lista[1]):
        return largoListaIgual(lista[1:])
    else:
        return False

def semiMagico(lista):
    if validaLista15(lista)==False:
        raise Exception("Error")
    elif largoListaIgual(lista)==False:
        raise Exception("Error")
    else:
        return semiMagicoAux(lista)

def semiMagicoAux(lista):
    if lista[1:]==[]:
        return True
    elif sumaLista(lista[0])==sumaLista(lista[1]):
        return semiMagicoAux(lista[1:])
    else:
        return False

def sumaLista(lista):
    if lista==[]:
        return 0
    else:
        return lista[0] + sumaLista(lista[1:])

#Ejercicio 17

def validaLista17(lista):
    if type(lista)!=list or lista==[]:
        return False
    else:
        return validaListaAux17(lista)

def validaListaAux17(lista):
    if lista==[]:
        return True
    elif type(lista[0])==int:
        return validaListaAux17(lista[1:])

def coincide(lista):
    if validaLista17(lista)==False:
        raise Exception("Error")
    else:
        return coincideAux(lista)

def coincideAux(lista):
    if lista==[]:
        return False
    elif lista[-1]==sumaLista(lista[:-1]):
        return True
    else:
        return coincideAux(lista[:-1])

def sumaLista(lista):
    if lista==[]:
        return 0
    else:
        return lista[0] + sumaLista(lista[1:])

#Ejercicio 19

def validaLista(lista):
    if type(lista)!=list or lista==[]:
        return False
    else:
        return validaListaAux(lista)

def validaListaAux(lista):
    if lista==[]:
        return True
    elif type(lista[0]) in [int, float]:
        return validaListaAux(lista[1:])
    else:
        return False

def calificacion(lista):
    if validaLista(lista)==False:
        raise Exception("Error")
    elif len(lista)!=10: #10 jueces
        raise Exception("Error")
    else:
        return calificacionAux(lista)

def calificacionAux(lista):
    if len(lista)==8:
        return sumaLista(lista)/8
    else:
        lista=ordenar(lista)
        lista=lista[1:-1]
        return calificacionAux(lista)

def ordenar(lista):
    if validaLista(lista)==False:
        raise Exception("ErrorE")
    else:
        return ordenarAux1(lista)

def ordenarAux1(lista):
    if estaOrdenada(lista)==True:
        return lista
    else:
        return ordenarAux1(ordenarAux2(lista))

def estaOrdenada(lista):
    if lista[1:]==[]:
        return True
    elif lista[0] <= lista[1]:
        return estaOrdenada(lista[1:])
    else:
        return False

def ordenarAux2(lista):
    if lista[1:] == []:
        return [lista[0]]
    else:
        if lista[0] > lista[1]:
            m = lista[0]
            lista[0] = lista[1]
            lista[1] = m
        return [lista[0]] + ordenarAux2(lista[1:])

#Ejercicio 21

def concordar(patron, sustitucion, original):
    if type(patron)!=list or type(sustitucion)!=list or type(original)!=list:
        raise Exception("Error")
    elif len(patron)!=len(sustitucion):
        raise Exception("Error")
    else:
        return concordarAux(patron, sustitucion, original, 0)

def concordarAux(patron, sustitucion, original, i):
    if i==len(original):
        return original
    else:
        if original[i] in patron:
            indice = buscarIndice(original[i], patron, 0) #Indice del elemento en la lista patron
            original[i] = sustitucion[indice]

        return concordarAux(patron, sustitucion, original, i+1)

def buscarIndice(ele, lista, i): #Para saber en que indice esta el elemento
    if i==len(lista):
        return 0
    else:
        if ele==lista[i]:
            return i
        else:
            return buscarIndice(ele, lista, i+1)

#Ejercicio 23

def validaLista23(lista):
    if type(lista)!=list or lista==[]:
        return False
    else:
        return validaListaAux(lista)

def validaListaAux23(lista):
    if lista==[]:
        return True
    elif type(lista[0])==int:
        return validaListaAux(lista[1:])
    else:
        return False

def mitades(lista):
    if validaLista23(lista)==False:
        raise Exception("Error")
    else:
        if len(lista)%2==0:
            return mitadesAux(lista)
        else:
            return mitadesAux(lista[0:len(lista)//2]+lista[len(lista)//2+1:])

def mitadesAux(lista):
    if lista==[]:
        return True
    else:
        if sumaLista(lista[0:len(lista)//2]) == sumaLista(lista[len(lista)//2:]):
            return mitadesAux([])
        else:
            return False

def sumaLista(lista):
    if lista==[]:
        return 0
    else:
        return lista[0] + sumaLista(lista[1:])