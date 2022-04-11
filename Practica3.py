###EJERCICIO 1###
#Función que indica si todos los números de una lista son divisores de un número
#Entradas: número, lista
#Salidas: True o False
#Restricciones: número debe ser entero, lista debe ser una lista que contenga números
def todosDiv(num, lista):
    if type(num)!=int or type(lista)!=list or lista==[]:
        return "Datos inválidos"
    else:
        for numero in lista:
            if type(numero)!=int and type(numero)!=float:
                return "Datos inválidos"
        divisor=True
        for numero in lista:
            if num%numero!=0:
                divisor=False
        return divisor

###EJERCICIO 3###
#Función que obtenga una lista en orden ascendente de números naturales menores al número dado
#Entradas: número
#Salidas: lista
#Restricciones: número y los números de la lista deben ser un números naturales

def iota(num):
    if type(num)!=int or num<0:
        return "Error"
    else:
        lista=[]
        for numero in range(0,num):
            lista+=[numero]
        return lista

###EJERCICIO 5###
#Función que obtenga cuántos estudiantes aprobaron el curso, cuántos reprobaron y el promedio de notas
#Entradas: lista
#Salidas: diccionario: {"Aprobados":A, "Reprobados":R, "Promedio general":P}
#Restricciones: lista debe ser una lista que contenga números, los números deben estar entre 0 y 100

def notas(lista):
    if type(lista)!=list or lista==[]:
        return "Error"
    else:
        for numero in lista:
            if (type(numero)!=int and type(numero)!=float) or (numero<0 or numero>100):
                return "Error"
        A=0 #Aprobados
        R=0 #Resprobados
        P=0 #Promedio
        for numero in lista:
            P+=numero
            if numero>=70:
                A+=1
            else:
                R+=1
        P/=len(lista)
        return {"Aprobados":A, "Reprobados":R, "Promedio general":P}

###EJERCICIO 7###
#Sucesión de Ulam
#Entradas: número
#Salidas: número: 1
#Restricciones: número debe ser entero y mayor a 0

def ulam(n):
    if type(n)!=int or n<=0:
        return "Error"
    else:
        while n!=1:
            if n%2==0:
                n//=2
            else:
                n=n*3+1
        return n

###EJERCICIO 9###
#Función que invierte el orden de los elementos de una lista
#Entradas: lista
#Salidas: lista nueva
#Restricciones: lista debe ser una lista

def invertirSimple(lista):
    if type(lista)!=list:
        return "Eroor"
    else:
        listaNueva=[]
        while lista!=[]:
            listaNueva=[lista[0]]+listaNueva
            lista=lista[1:]
        return listaNueva

###EJERCICIO 11###
# n = 3 *a + 5 *b
#Función que devuelva posibles valores de a y b
#Entradas: número
#Salidas: lista [a,b]
#Restricciones: número debe ser mayor o igual a 8

def sumaTresCinco(num):
    if type(num)!=int or num<8:
        return "Error"
    else:
        a=0
        b=0
        while num!=0:
            if num%5==0:
                num-=5
                b+=1
            else:
                num-=3
                a+=1
        return [a, b]

###EJERCICIO 13###
#Función que verifique si los elementos de una lista son alternados entre pares e impares
#Entradas: lista
#Salidas: True o False
#Restricciones: lista debe ser una lista y no debe ser nula, sus elementos deben ser números enteros

def par(elemento):
    if elemento%2==0:
        elementoPar=True
    else:
        elementoPar=False
    return elementoPar

def alternada(lista):
    if type(lista)!=list or lista==[]:
        return "Error"
    else:
        for elemento in lista:
            if type(elemento)!=int:
                return "Error"

        elementoAlternado=True
        while len(lista)!=1:
            if par(lista[0])==par(lista[1]):
                elementoAlternado=False
            lista=lista[1:]
        return elementoAlternado

###EJERCICIO 15###
#Función que encuentra las parejas de números amigos que son inferiores a un número
#Entradas: número
#Salidas: números amigos
#Restricciones: número debe ser un número entero mayor a 0

def numeroAmigo(num):
    posibleNumeroAmigo=0
    for numero in range(1,num//2+1):
        if num%numero==0:
            posibleNumeroAmigo+=numero
    return posibleNumeroAmigo

def amigos(num):
    if type(num)!=int or num<=0:
        return "Error"
    else:
        posibleNumeroAmigo=numeroAmigo(num)

        if posibleNumeroAmigo>num:
            return "No tiene número amigo"
        else:
            numero=numeroAmigo(posibleNumeroAmigo)
            if numero==num:
                return posibleNumeroAmigo
            else:
                return "No tiene número amigo"

###EJERCICIO 17###
#Función que separe una lista en 2 dependiendo del lugar que ocupan sus elementos
#Entradas: lista
#Salida: 2 listas dentro de una lista [[listaImpar, listaPar]]
#Restricciones: lista debe ser una lista y no puede ser nula

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

###EJERCICIO 19###
#Función que muestre los factores primos de un número
#Entradas: número
#Salidas: lista con factores primos
#Restricciones: número debe ser un entero positivo

def esprimo(N):
    if N==2:
        return True
    else:
        esPrimo=True
        for i in range(2,N):
            if N%i==0:
                esPrimo=False
        return esPrimo

def primo(n):
    primos=[]
    for i in range(2, n+1):
        if esprimo(i)==True:
            primos+=[i]
    return primos

def factorPrimo(n):
    if type(n)!=int or n<=0:
        return "Error"
    else:
        lista=[] #Salida
        numerosPrimos=primo(n)
        while n!=0:
            for numero in numerosPrimos:
                if n%numero==0:
                    lista+=[numero]
                    break
            n//=numero
        return lista