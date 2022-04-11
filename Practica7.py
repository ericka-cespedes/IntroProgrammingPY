#Ejercicio 1
def validaLista(lista):
    if type(lista)!=list or lista==[]:
        return False
    else:
        return validaListaAux(lista, True)
def validaListaAux(lista, res):
    if lista==[]:
        return res
    elif type(lista[0]) in [int, float]:
        return validaListaAux(lista[1:], res)
    else:
        return validaListaAux(lista[1:], False)

def todosDiv(num, lista):
    if type(num)!=int or validaLista(lista)==False:
        raise Exception("Error")
    else:
        return todosDivAux(num, lista, True)

def todosDivAux(num, lista, res):
    if lista==[]:
        return res
    elif num%lista[0]!=0:
        return todosDivAux(num, lista[1:], False)
    else:
        return todosDivAux(num, lista[1:], res)

#Ejercicio 3
def iota(num):
    if type(num)!=int or num<0:
        raise Exception("Error")
    else:
        return iotaAux(0, num, [])

def iotaAux(i, num, res):
    if i==num:
        return res
    else:
        return iotaAux(i+1, num, res+[i])

#Ejercicio 5
def validaLista(lista):
    if type(lista)!=list or lista==[]:
        return False
    else:
        return validaListaAux(lista, True)

def validaListaAux(lista, res):
    if lista==[]:
        return res
    elif type(lista[0]) in [int, float]:
        return validaListaAux(lista[1:], res)
    else:
        return validaListaAux(lista[1:], False)

def ultimoPar(lista):
    if validaLista(lista)==False:
        raise Exception("Error")
    else:
        return ultimoParAux(lista, 0)

def ultimoParAux(lista, elemento):
    if lista==[]:
        if elemento==0:
            return "No hay ningun par"
        else:
            return elemento
    else:
        if lista[0]%2==0:
            elemento=lista[0]
        return ultimoParAux(lista[1:], elemento)

#Ejercicio 7
def serie(n):
    if type(n)!=int or n<2:
        raise Exception("Error")
    else:
        return serieAux(n, 1, 2, [])

def serieAux(n, i, num, res):
    if n==num:
        return res + [num]
    else:
        if i%2==0:
            return serieAux(n, i+1, num+2, res+[num])
        else:
            return serieAux(n, i+1, num+3, res+[num])

#Ejercicio 9
#Pila
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
            return cuentaElemAux(elemento) + cuentaElemAux(lista[1:])
#Cola
def cuentaElem2(lista):
    if type(lista)!=list:
        raise Exception ("Error")
    else:
        return cuentaElemAux2(lista, 0)

def cuentaElemAux2(lista, res):
    if lista==[]:
        return res
    else:
        elemento=lista[0]
        if type(elemento)!=list:
            return cuentaElemAux2(lista[1:], res+1)
        else:
            return cuentaElemAux2(elemento, 0) + cuentaElemAux2(lista[1:], res)

#En la solucion con recursividad de cola, como la variable se va guardando, se necesita poner un 0 en cuentaElemAux2(elemento, 0), de otra manera se va a sumar el res que
#ya se llevaba mas el de cuentaElemAux2(elemento, 0), de la siguiente manera:

#cuentaElemAux2([1,2,3,4,[5,6,7,8],9,10])
# 1 + 1 + 1 + 1 + cuentaElemAux2([[5,6,7,8],9,10], res)
# res=4 + cuentaElemAux2([5,6,7,8], res=4)
# 4 + (res=4 + 1+1+1+1+1) + cuentaElemAux2([9,10], res)
# 12 + cuentaElemAux2([9,10], res)
# 14

#En si, el algoritmo con recursividad de pila resulta ser mas sencillo de plantear y de entender, pero el de cola no tiene la pila de llamadas que tiene el de pila.

#Ejercicio 10

#Pila

def separa(ele, lista):
    if type(lista)==list:
        if estaEle(ele, lista):
            return separaAux(ele, lista)
        else:
            return lista
    else:
        raise Exception("Error")

def separaAux(ele, lista):
    if lista==[]:
        return []
    else:
        return [obtiene(ele, lista)] + separaAux(ele, lista[cuenta(ele, lista):])

def obtiene(ele, lista):
    if lista==[] or ele==lista[0]:
        return []
    else:
        return [lista[0]] + obtiene(ele, lista[1:])

def cuenta(ele, lista):
    if lista[0]==ele:
        return 1
    else:
        return 1 + cuenta(ele, lista[1:])

def estaEle(ele, lista):
    if lista==[]:
        return False
    elif lista[0]==ele:
        return True
    else:
        return estaEle(ele, lista[1:])

#Cola

def separa2(ele, lista):
    if type(lista)==list:
        return separaAux2(ele, lista, [], [])
    else:
        raise Exception("Error")

def separaAux2(ele, lista, sup, resp):
    if not estaEle(ele, lista):
        return resp + [lista]
    elif lista[0]==ele:
        return separaAux2(ele, lista[1:], [], resp + [sub])
    else:
        return separaAux2(ele, lista[1:], sub + [lista[0]], resp)

#Con un índice

def separa3(ele, lista):
    if type(lista)==list:
        return separaAux3(ele, lista, 0, [], [])
    else:
        raise Exception("Error")

def separaAux3(ele, lista, i, sub, resp):
    if i==largo(lista,0):
        if sub==[]:
            return resp
        else:
            return resp + [sub]
    elif lista[i]==ele:
        return separaAux3(ele, lista, i+1, [] , resp + [sub])
    else:
        return separaAux3(ele, lista, i+1, sub + [lista[i]], resp)

def largo(lista, cont):
    if lista==[]:
        return cont
    else:
        return largo(lista[1:], cont+1)

#Ejercicio 11

def insertData(ref, ele, lista):
    if type(lista)!=list or lista==[]:
        raise Exception("Error")
    if esta(ref, lista)==False:
        raise Exception("Error: ref no esta en la lista.")
    else:
        return insertDataAux(ref, ele, lista, [])

def insertDataAux(ref, ele, lista, res):
    if lista==[]:
        return res
    else:
        if esta(ref, lista)==True:
            indice=donde(ref, lista, 0)
            res+=lista[:indice+1] + [ele]
            return insertDataAux(ref, ele, lista[indice+1:], res)
        else:
            res+=lista
            return insertDataAux(ref, ele, [], res)

def esta(ele, lista, res=False):
    if lista==[]:
        return res
    else:
        if ele==lista[0]:
            return esta(ele, lista[1:], res=True)
        else:
            return esta(ele, lista[1:], res)

def donde(ele, lista, res):
    if ele==lista[0]:
        return res
    else:
        return donde(ele, lista[1:], res+1)

#Ejercicio 12
def raiz3(y, n):
    if type(y) not in [int, float]:
        raise Exception("Error")
    elif type(n)!=int:
        raise Exception("Error")
    elif n<1:
        raise Exception("Error")
    else:
        return raiz3Aux(y, n, 1)

def raiz3Aux(y, n, x):
    if n==x:
        return 0
    else:
        return 1/3*((2*x + y) / x**2) - raiz3Aux(y, n, x+1)

#Ejercicio 13
def misterio(l):
    if l[2:]==[]:
        return l[0]==l[1]
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

#Ejercicio 14

def sumaTC(num):
    if type(num)!=int or num<8:
        raise Exception("Error")
    else:
        return sumaTCAux(num, 0, 0)

def sumaTCAux(num, a, b):
    if num==0:
        return [a,b]
    else:
        if num%5==0:
            num-=5
            return sumaTCAux(num, a, b+1)
        else:
            num-=3
            return sumaTCAux(num, a+1, b)

#Ejercicio 15
def validaLista15(lista):
    if type(lista)!=list or lista==[]:
        return False
    else:
        return validaListaAux15(lista, True)

def validaListaAux15(lista, res):
    if lista==[]:
        return res
    elif type(lista[0])==list:
        if validaListaAuxiliar15(lista[0], True)==True:
            return validaListaAux15(lista[1:], res)
        else:
            return validaListaAux15(lista[1:], res=False)
    else:
        return validaListaAux15(lista[1:], res=False)

def validaListaAuxiliar15(lista, res):
    if lista==[]:
        return res
    elif type(lista[0]) in [int, float]:
        return validaListaAuxiliar15(lista[1:], res)
    else:
        return validaListaAuxiliar15(lista[1:], res=False)

def largoListaIgual(lista, res=True):
    if lista[1:]==[]:
        return res
    elif len(lista[0])==len(lista[1]):
        return largoListaIgual(lista[1:], res)
    else:
        return largoListaIgual(lista[1:], res=False)

def semiMagico(lista):
    if validaLista15(lista)==False:
        raise Exception("Error")
    elif largoListaIgual(lista)==False:
        raise Exception("Error")
    else:
        return semiMagicoAux(lista, True)

def semiMagicoAux(lista, res):
    if lista[1:]==[]:
        return res
    elif sumaLista(lista[0],0)==sumaLista(lista[1],0):
        return semiMagicoAux(lista[1:], res)
    else:
        return semiMagicoAux(lista[1:], res=False)

def sumaLista(lista, res):
    if lista==[]:
        return res
    else:
        return sumaLista(lista[1:], res+lista[0])

#Ejercicio 17
def parejas(num):
    if type(num)!=int or num<2 or num>100:
        raise Exception("Error")
    else:
        return parejasAux(num, 0, [], [])

def parejasAux(num, i, lista, res):
    if num==i: # o num//2 < i y la funcion esta(), no seria necesaria
        return res
    else:
        if esta(i, res)==False:
            lista+=[i]
            lista+=[num-i]
            res+=[lista]
        return parejasAux(num, i+1, [], res)

def esta(ele, lista, res=False):
    if lista==[]:
        return res
    else:
        if type(lista[0])!=list:
            if ele==lista[0]:
                return esta(ele, lista[1:], res=True)
            else:
                return esta(ele, lista[1:], res)
        else:
            return esta(ele, lista[1:], esta(ele, lista[0], res))

#Ejercicio 19

def numeroAmigo(num, i, posibleNumeroAmigo):
    if num//2+1 == i:
        return posibleNumeroAmigo
    else:
        if num%i==0:
            posibleNumeroAmigo+=i
        return numeroAmigo(num, i+1, posibleNumeroAmigo)

def amigos(num):
    if type(num)!=int or num<=0:
        raise Exception("Error")
    else:
        return amigosAux(num)

def amigosAux(num):
    posibleNumeroAmigo=numeroAmigo(num, 1, 0)
    if posibleNumeroAmigo>num:
        return "No tiene numero amigo"
    else:
        numero=numeroAmigo(posibleNumeroAmigo)
        if numero==num:
            return posibleNumeroAmigo
        else:
            return "No tiene número amigo"

#Ejercicio 21

def separar(lista):
    if type(lista)!=list or lista==[]:
        return "Error"
    else:
        listaImpar=[]
        listaPar=[]
        largoLista=len(lista)-1
        while largoLista!=-1:
            if largoLista%2==0:
                listaPar=[lista[largoLista]]+listaPar
            else:
                listaImpar=[lista[largoLista]]+listaImpar
            largoLista-=1
        return [listaImpar, listaPar]

def separar(lista):
    if isinstance(lista, list):
        if lista == []:
            return [[], []]
        else:
            return separarAux(lista, [], [], len(lista)-1)
    else:
        raise Exception ("Error")

def separarAux(lista, pares, impares, largoLista):
    if largoLista==-1:
        return [impares, pares]
    elif largoLista % 2 == 0:
        return separarAux(lista, [lista[largoLista]]+pares, impares, largoLista-1)
    else:
        return separarAux(lista, pares, [lista[largoLista]]+impares, largoLista-1)

#Ejercicio 23

def cuenta_lista_anidada(lista):
    if lista==[]:
        return 1
    else:
        return 1+cuenta_lista_anidadaAux(lista)

def cuenta_lista_anidadaAux(lista):
    if lista==[]:
        return 0
    else:
        elemento=lista[0]
        if type(elemento)!=list:
            return cuenta_lista_anidadaAux(lista[1:])
        else:
            return 1+cuenta_lista_anidadaAux(elemento)+cuenta_lista_anidadaAux(lista[1:])

def getDepth(lista):
    if type(lista)!=list:
        raise Exception("Error")
    else:
        return getDepthAux(lista, 0)

def getDepthAux(lista, res):
    if lista==[]:
        return res
    else:
        if type(lista[0])!=list: #Si el elemento no es una lista
            return getDepthAux(lista[1:], res)
        else:
            tamanoLista=cuenta_lista_anidada(lista[0])
            if tamanoLista>res:
                res=tamanoLista
            return getDepthAux(lista[1:], res)

#Ejercicio 25

def esPrimo(N):
    if N==1 or N==0:
        return False
    elif N==2:
        return True
    else:
        return esPrimoAux(2, N)

def esPrimoAux(num1, num2):
    if num1==num2:
        return True
    else:
        if num2 % num1 == 0:
            return False
        return esPrimoAux(num1+1, num2)

def primo(n):
    return primoAux(2, n, [])

def primoAux(num1, num2, primos):
    if num1==num2+1:
        return primos
    else:
        if esPrimo(num1)==True:
            return primoAux(num1+1, num2, primos+[num1])
        else:
            return primoAux(num1+1, num2, primos)

def esprimo2(N):
    if N==2:
        return True
    else:
        esPrimo=True
        for i in range(2,N):
            if N%i==0:
                esPrimo=False
        return esPrimo

def primo2(n):
    primos=[]
    for i in range(2, n+1):
        if esprimo2(i)==True:
            primos+=[i]
    return primos

def factorPrimo(n):
    if type(n)!=int or n<=0:
        raise Exception("Error")
    elif n>900: #Numero demasiado grande para hacer recursividad
        return factorPrimoAux(n, primo2(n), [])
    else:
        return factorPrimoAux(n, primo(n), [])

def factorPrimoAux(n, numerosPrimos, lista):
    if n==0:
        return lista
    else:
        return factorPrimoAux2(n, numerosPrimos, 0, lista)

def factorPrimoAux2(n, numerosPrimos, i, lista):
    try:
        numero=numerosPrimos[i]
        if len(numerosPrimos)==i:
            return factorPrimoAux(n//numero, numerosPrimos, lista)
        else:
            if n%numero==0:
                return factorPrimoAux(n//numero, numerosPrimos, lista+[numero])
            else:
                return factorPrimoAux2(n, numerosPrimos, i+1, lista)
    except:
        return lista

#Ejercicio 27

def validaLista27(lista):
    if type(lista)!=list:
        return False
    else:
        return validaListaAux27(lista, True)

def validaListaAux27(lista, res):
    if lista==[]:
        return res
    elif type(lista[0])==int:
        return validaListaAux27(lista[1:], res)
    else:
        return validaListaAux27(lista[1:], False)

def validaListaIndices(lista1, lista2, res):
    if lista1==[]:
        if len(lista2)<res:
            return False
        else:
            return True
    else:
        if lista1[0]==0:
            res+=1
            #lista1[0]=1
        return validaListaIndices(lista1[1:], lista2, res+1+lista1[0])

def biSkip(lista1, lista2):
    if validaLista27(lista1)==False:
        raise Exception("Error")
    elif type(lista2)!=list:
        raise Exception("Error")
    elif validaListaIndices(lista1, lista2, 0)==False:
        raise Exception("Error: no se pueden eliminar más elementos que los existentes")
    else:
        return biSkipAux(lista1, lista2, 0)

def biSkipAux(lista1, lista2, i):
    if lista1==[]:
        return lista2
    else:
        if lista1[0]==0:
            return biSkipAux(lista1[1:], lista2, i+1)
        elif lista1[0]==1:
            lista2.remove(lista2[i])
            return biSkipAux(lista1[1:], lista2, i+1)
        else:
            return biSkipAux2(lista1, lista2, i)

def biSkipAux2(lista1, lista2, i):
    if lista1[0]==0:
        return biSkipAux(lista1[1:], lista2, i+1)
    else:
        lista1[0]=lista1[0]-1
        lista2.remove(lista2[i])
        return biSkipAux2(lista1, lista2, i)