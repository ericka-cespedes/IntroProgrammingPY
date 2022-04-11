#1
#Entradas: lista
#Salidas: True o False
#Restricciones: lista de números enteros, lista no puede estar vacía
def validaLista(lista):
    if type(lista)!=list or lista==[]:
        return False
    else:
        return validaListaAux(lista)

def validaListaAux(lista):
    if lista==[]:
        return True
    elif type(lista[0])==int:
        return validaListaAux(lista[1:])
    else:
        return False

def coincide(lista):
    if validaLista(lista)==False:
        raise Exception("Error")
    else:
        return coincideAux(0, lista)

def coincideAux(suma, lista):
    if lista==[]:
        return False
    elif lista[0]==suma:
        return True
    else:
        return coincideAux(suma+lista[0], lista[1:])

#---------------------------------------------------------------------

def coincidePila(lista):
    if validaLista(lista)==False:
        raise Exception("Error")
    else:
        return coincideAuxPila(lista)

def coincideAuxPila(lista):
    if lista==[]:
        return False
    elif lista[-1]==suma(lista[:-1]):
        return True
    else:
        return coincideAuxPila(lista[:-1])

def suma(lista):
    if lista==[]:
        return 0
    else:
        return lista[0] + suma(lista[1:])

#---------------------------------------------------------------------
#2
#Entradas: dígito (dig), número (num)
#Salidas: (A,B), A:mayores que dig, B:menores o iguales a dig
#Restricciones: dig: número entero 0<=dig<10 ; num: número entero

def digitos(dig, num):
    if type(dig)!=int or dig<0 or dig>10:
        raise Exception("Error")
    elif type(num)!=int:
        raise Exception("Error")
    else:
        return digitosAuxA(dig, abs(num)), digitosAuxB(dig, abs(num))

def digitosAuxA(dig, num):
    if num==0:
        return 0
    else:
        if num%10>dig:
            return num%10 + 10*(digitosAuxA(dig, num//10))
        else:
            return digitosAuxA(dig, num//10)

def digitosAuxB(dig, num):
    if num==0:
        return 0
    else:
        if num%10<=dig:
            return num%10 + 10*(digitosAuxB(dig, num//10))
        else:
            return digitosAuxB(dig, num//10)