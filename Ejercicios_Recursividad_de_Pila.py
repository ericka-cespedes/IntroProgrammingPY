# Integrantes del grupo 3: Mario Camacho 2016193391 // Ericka Cespedes 2017239557 // Sebastian Solano 2013103709
# Ejercicios 3, 6, 9, 12, 15.
# Entrega 24/10/2017


################ Ejercicio 3 ###################
# Funcion: cuentaPares
# Entradas: lista de numeros enteros
# Salidas: cuenta de los numeros pares de la lista
# Restricciones: lista debe ser un vector
# Estrategia: funcion que valida la entrada como un vector


def valida(lista):
    if not (type(lista) == list):
        raise Exception("Error")
    else:
        return AuxV(lista)



def AuxV(lista):
    if lista == []:
        return True
    elif type(lista[0]) == int:
        return AuxV(lista[1:])
    else:
        return False



def cuentaPares(lista):
    if not (type(lista) == list) or (valida(lista) == False):
        raise Exception("Error")
    else:
        return AuxS(lista)


def AuxS(lista):
    if lista == []:
        return 0
    else:
        if (lista[0] % 2) == 0:
            return 1+ AuxS(lista[1:])
        else:
            return AuxS(lista[1:])



################ Ejercicio 6 ###################
# Funcion: todosPares
# Entradas: lista de numeros enteros
# Salidas: recorre la lista y si encuentra un numero que no es par,
# retorna False, sino retorna True
# Restricciones: lista debe ser un vector
# Estrategia: funcion que valida la entrada como un vector, tomada del ejercicio 3


def todosPares(lista):
    if not (type(lista) == list) or (valida(lista) == False):
        raise Exception("Error")
    else:
        return AuxP(lista)


def AuxP(lista):
    v = True
    if lista == []:
        return v
    else:
        if ((lista[0]) % 2) != 0:
            v = False
            return v
        return AuxP(lista[1:])




################ Ejercicio 9 ###################
# Funcion: elimina
# Entradas: elemento "ele" y  lista "lista"
# Salidas: recorre la lista y elimina todas las apariciones
# del elemento en la lista
# Restricciones: debe ser una lista.



def elimina(ele,lista):
    if not (type(lista) == list):
        raise Exception("Error")
    else:
        return AuxE(ele,lista)


def AuxE(ele,lista):
    if lista == []:
        return lista
    else:
        if (lista[0]) != ele:
            return [lista[0]] + AuxE(ele,lista[1:])
        else:
            return AuxE(ele,lista[1:])








################ Ejercicio 12 ###################
# Funcion: mayor
# Entradas: lista numerica
# Salidas: el elemento mayor de la lista
# Restricciones: debe ser una lista numerica
# Estrategia: funcion que valida lista con numeros


def valida2(lista):
    if not (type(lista) == list):
        raise Exception("Error")
    else:
        return AuxV2(lista)



def AuxV2(lista):
    if lista == []:
        return True
    elif type(lista[0]) == int or type(lista[0]) == float:
        return AuxV2(lista[1:])
    else:
        return False


def mayor(lista):
    if not (type(lista) == list) or (valida2(lista) == False):
        raise Exception("Error")
    else:
        return AuxM(lista)


def AuxM(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        if lista[0] > lista[1]:
            t = lista[0]
            lista[0] = lista[1]
            lista[1] = t
        return AuxM(lista[1:])






################ Ejercicio 15 ###################
# Funcion: cuentaListaAnidada
# Entradas: lista
# Salidas: contador que cuente todos los elementos de la lista,
# incluso las listas anidadas
# Restricciones: debe ser una lista


def cuentaListaAnidada(lista):
    if not (type(lista) == list):
        raise Exception("Entrada debe ser lista")
    else:
        return AuxA(lista)


def AuxA(lista):
    if lista == []:
        return 0
    elif type(lista[0]) == list:
        return AuxA(lista[0]) + AuxA(lista[1:])
    else:
        return 1 + AuxA(lista[1:])