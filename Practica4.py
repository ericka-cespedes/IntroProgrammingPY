#1
#Entradas: vector (1 columna o 1 fila): [[],[],[]] o [[]]
#Salidas: True (elementos en orden ascendente) o False
def vectorAscendente(vector):
    esVector=True
    if type(vector)!=list:
        esVector=False
    else:
        contador=0
        for lista in vector:
            if type(lista)!=list:
                esVector=False
                break
            contador+=1
            for elemento in lista:
                if type(elemento)!=int:
                    esVector=False
                    break
        if contador>=2:
            for lista in vector:
                if len(lista)!=1:
                    esVector=False
    if esVector==False:
        return "Error"
    else:
        if len(vector)==1: #1 fila
            for lista in vector:
                listaOrdenada=sorted(lista)
                return listaOrdenada == lista
        else: #1 columna
            vectorOriginal=vector #para comparar
            i=0
            while len(vector)>1:
                if vector[i] > vector[i+1]:
                    return False
                vector=vector[1:]
            return True
#2
#Entradas: 2 strings
#Salidas: # de palabras IGUALES que están en f1 y f2

def repetidas(f1,f2):
    if type(f1)!=str or type(f2)!=str:
        return "Error"
    else:
        f1=f1.split(" ")
        f2=f2.split(" ")
        contador=0
        for palabra in f1:
            f3=f2
            while f3!=[]:
                if palabra == f3[0]:
                    contador+=1
                f3=f3[1:]
        return contador
#Ejemplo:
#>>> repetidas("hola mundo feliz feliz", "droppy es un perro feliz feliz")
#4

#3
#Entradas: string
#Salidas: string (caracteres minuscula -> mayuscula, y viceversa)

def mayus(minus):
    minus=minus.upper()
    return minus

def minus(mayus):
    mayus=mayus.lower()
    return mayus

def convertirCaracteres(string):
    if type(string)!=str:
        return "Error"
    else:
        string2=string
        string=""
        for letra in string2:
            if letra.islower()==True:
                letra=mayus(letra)
            else:
                letra=minus(letra)
            string+=letra
        return string

#4
#Entradas: matriz (2 filas min)
#Salidas: reflejo horizontal de esa matriz
#Matriz horizontal: tiene más columnas que filas

def reflejoHorizontal(matriz):
    esMatriz=True
    if type(matriz)!=list:
        esMatriz=False
    else:
        lista0=matriz[0]
        for lista in matriz:
            if type(lista)!=list:
                esMatriz=False
            else:
                if len(lista0)!=len(lista): #len(lista1)=len(lista2)=len(listan)
                    esMatriz=False
                else:
                    for numero in lista: #Para que sea una matriz
                        if type(numero)!=int and type(numero)!=float:
                            esMatriz=False
    if esMatriz==False:
        return "No es una matriz."
    else:
        if len(matriz)<2:
            return "No cumple los requisitos del problema."
        else:
            reflejoHorizontal=[] #reflejoHorizontal=[[fila],[fila],...]
            fila=[]
            i=0
            cantListas=len(matriz)
            while cantListas!=0:
                fila+=matriz[cantListas-1]
                reflejoHorizontal+=[fila]
                fila=[]
                cantListas-=1
            return reflejoHorizontal

#5
#Entradas: matriz nxm A[i][j]
#Salidas: transpuesta de la matriz At[i][j]=A[j][i] mxn

def matrizTranspuesta(matriz):
    esMatriz=True
    if type(matriz)!=list:
        esMatriz=False
    else:
        lista0=matriz[0]
        for lista in matriz:
            if type(lista)!=list:
                esMatriz=False
            else:
                if len(lista0)!=len(lista): #len(lista1)=len(lista2)=len(listan)
                    esMatriz=False
                else:
                    for numero in lista: #Para que sea una matriz
                        if type(numero)!=int and type(numero)!=float:
                            esMatriz=False
    if esMatriz==False:
        return "No es una matriz."
    else:
        matrizTranspuesta=[] #Salida
        fila=[] #matrizTranspuesta=[[fila],[fila],[fila],...]
        i=0
        while len(lista0)>i: #len(lista1)=len(lista2)=len(listan)
            for lista in matriz:
                fila+=[lista[i]]
            matrizTranspuesta+=[fila]
            fila=[]
            i+=1
        return matrizTranspuesta

#6
#Entradas: matriz nxm, vector tamaño n (misma cantidad de filas)
#Salidas: resultado del producto matricial

def esMatriz(matriz):
    esMatriz=True
    if type(matriz)!=list:
        esMatriz=False
    else:
        lista0=matriz[0]
        for lista in matriz:
            if type(lista)!=list:
                esMatriz=False
            else:
                if len(lista0)!=len(lista): #len(lista1)=len(lista2)=len(listan)
                    esMatriz=False
                else:
                    for numero in lista: #Para que sea una matriz
                        if type(numero)!=int and type(numero)!=float:
                            esMatriz=False
    return esMatriz

def esVector6(vector):
    esVector=True
    if type(vector)!=list:
        esVector=False
    else:
        contador=0
        for lista in vector:
            if type(lista)!=list:
                esVector=False
                break
            contador+=1
            for elemento in lista:
                if type(elemento)!=int and type(elemento)!=float:
                    esVector=False
                    break
        if contador>=2:
            for lista in vector:
                if len(lista)!=1:
                    esVector=False
        else:
            esVector=False #Vector fila no cumple los requisitos del problema
    return esVector

def multiplicarVector(lista, vector):
    filaResultado=0
    i=0
    for listaVector in vector:
        for elemento in listaVector: #Tienen que ser matrices conformables
            filaResultado+=elemento*lista[i]
            i+=1
    return filaResultado

def multiplicar(matriz, vector):
    if esMatriz(matriz)==False or esVector6(vector)==False:
        return "Error."
    else:
        if len(matriz)!=len(vector):
            return "No cumple los requisitos del problema."
        elif len(matriz[0])!=len(vector): #Para poder hacer el producto matricial
            return "No cumple los requisitos del problema."
        else:
            resultado=[] #Salida
            i=0
            for listaMatriz in matriz:
                resultado+=[[multiplicarVector(listaMatriz, vector)]]
            return resultado

#7
#Entradas: str1, str2, inicio, fin
#Salidas: indice (str2 in str1)

def find(string1, string2): #string1 en string2
    try:
        largo=len(string1)
        contador=0
        while len(string2)>=contador:
            if string1==string2[contador:contador+largo]:
                return contador
            else:
                contador+=1
    except:
        return -1

def buscar(str1, str2, inicio, fin):
    if type(str1)!=str or type(str2)!=str or type(inicio)!=str or type(fin)!=str:
        return "Error"
    elif str1.find(inicio)==-1 or str1.find(fin)==-1:
            return "Error"
    else:
        start = find(inicio, str1)
        end = find(fin, str1)
        str1 = str1[start:end]
        return find(str2, str1)

#8
#Entradas: 2 arreglos
#Salidas: True o False

def subVector(vec1, vec2):
    if type(vec1)!=list or type(vec2)!=list:
        return "Error."
    else:
        largo=len(vec1)
        contador=0
        while len(vec2)>=contador:
            if vec1==vec2[contador:contador+largo]:
                return True
            else:
                contador+=1
        return False

#9
#Entradas: 2 vectores del mismo tamaño
#Salidas: True o False

def esVector9(vector):
    esVector=True
    if type(vector)!=list:
        esVector=False
    else:
        for elemento in vector:
            if type(elemento)!=int and type(elemento)!=float:
                esVector=False
                break
    return esVector

def unirOrdenar(vector1, vector2):
    if esVector9(vector1)==False or esVector9(vector2)==False:
        return "Error."
    elif len(vector1)!=len(vector2):
        return "Error."
    else:
        resultado=[]
        resultado=vector1[0:len(vector1)]+vector2[0:len(vector2)]
        i=0
        listaOrdenada=False
        while not listaOrdenada:
            cambio=False
            while i<len(resultado)-1:
                if resultado[i] > resultado[i+1]:
                    cambio=True
                    x = resultado[i]
                    resultado[i] = resultado[i+1]
                    resultado[i+1] = x
                i+=1
            i=0
            if cambio==False:
                listaOrdenada=True
        return resultado

#10
#Entradas: matriz cuadrada nxn
#Salidas: vector diagonal principal de la matriz

def esMatrizCuadrada(matriz):
    esMatriz=True
    for lista in matriz:
        if type(lista)!=list:
            esMatriz=False
        else:
            lista0=matriz[0]
            if len(lista0)!=len(matriz): #len(MatA)=len(lista1) #Matriz cuadrada
                esMatriz=False
            else:
                for lista in matriz:
                    if len(lista0)!=len(lista): #len(lista1)=len(lista2)=len(listan)
                        esMatriz=False
                    else:
                        for numero in lista: #Para que sea una matriz
                            if type(numero)!=int and type(numero)!=float:
                                esMatriz=False
    return esMatriz

def diagonalPrincipal(matriz):
    if esMatrizCuadrada(matriz)==False:
        return "No es una matriz cuadrada."
    else:
        i=0
        vector=[]
        for lista in matriz:
            vector+=[lista[i]]
            i+=1
        return vector

#11
#Entradas: 2 matrices
#Salidas: producto matricial

def esMatriz(matriz):
    esMatriz=True
    if type(matriz)!=list:
        esMatriz=False
    else:
        lista0=matriz[0]
        for lista in matriz:
            if type(lista)!=list:
                esMatriz=False
            else:
                if len(lista0)!=len(lista): #len(lista1)=len(lista2)=len(listan)
                    esMatriz=False
                else:
                    for numero in lista: #Para que sea una matriz
                        if type(numero)!=int and type(numero)!=float:
                            esMatriz=False
    return esMatriz

def matrizConformable(A,B):
    matriz=True
    columnasA=len(A[0])
    filasB=len(B)
    if columnasA!=filasB:
        matriz=False
    return matriz

def multiplicarFilaColumna(filaA, B):
    elementoResultado=0
    filaResultado=[]
    i=0
    j=0
    while i<len(filaA): #Matriz conformable
        for filaB in B:
            elemento=filaB[i]*filaA[j]
            elementoResultado+=elemento
            j+=1
        filaResultado+=[elementoResultado]
        elementoResultado=0
        i+=1
        j=0
    return filaResultado

def productoMatriz(A, B):
    if esMatriz(A)==False or esMatriz(B)==False:
        return "A o B no son matrices."
    elif matrizConformable(A,B)==False:
        return "A y B no son matrices conformables."
    else:
        resultado=[]
        for filaA in A:
            resultado+=[multiplicarFilaColumna(filaA, B)]
        return resultado

#12
#Entradas: matriz cuadrada
#Salidas: True o False

def esMatrizCuadrada(matriz):
    esMatriz=True
    for lista in matriz:
        if type(lista)!=list:
            esMatriz=False
        else:
            lista0=matriz[0]
            if len(lista0)!=len(matriz): #len(MatA)=len(lista1) #Matriz cuadrada
                esMatriz=False
            else:
                for lista in matriz:
                    if len(lista0)!=len(lista): #len(lista1)=len(lista2)=len(listan)
                        esMatriz=False
                    else:
                        for numero in lista: #Para que sea una matriz
                            if type(numero)!=int and type(numero)!=float:
                                esMatriz=False
    return esMatriz

def triangularInferior(matriz):
    if esMatrizCuadrada(matriz)==False:
        return "No es una matriz cuadrada."
    else:
        inferior=True
        i=0
        for lista in matriz:
            if lista[i]==0:
                inferior=False #Los elementos de la diagonal no pueden ser iguales a 0
                break
            i+=1
        i=0
        ceros=[]
        for lista in matriz:
            if lista[0:i]!=ceros: #Cantidad de ceros en cada fila para que sea una matriz triangular inferior
                inferior=False
                break
            ceros+=[0]
            i+=1
        return inferior

#13
#Entradas: matriz
#Salidas: reflejo horizontal

def es_matriz(matriz):
    esMatriz=True
    if type(matriz)!=list:
        esMatriz=False
    else:
        lista0=matriz[0]
        for lista in matriz:
            if type(lista)!=list:
                esMatriz=False
            else:
                if len(lista0)!=len(lista): #len(lista1)=len(lista2)=len(listan)
                    esMatriz=False
                else:
                    for numero in lista: #Para que sea una matriz
                        if type(numero)!=int and type(numero)!=float:
                            esMatriz=False
    return esMatriz

def horizontal(matriz):
    if es_matriz(matriz)==False:
        return "No es una matriz."
    else:
        reflejoHorizontal=[] #reflejoHorizontal=[[fila],[fila],...]
        fila=[]
        cantListas=len(matriz)
        while cantListas!=0:
            fila+=matriz[cantListas-1]
            reflejoHorizontal+=[fila]
            fila=[]
            cantListas-=1
        return reflejoHorizontal

#14
#Entradas: matriz
#Salidas: reflejo vertical

def es_matriz(matriz):
    esMatriz=True
    if type(matriz)!=list:
        esMatriz=False
    else:
        lista0=matriz[0]
        for lista in matriz:
            if type(lista)!=list:
                esMatriz=False
            else:
                if len(lista0)!=len(lista): #len(lista1)=len(lista2)=len(listan)
                    esMatriz=False
                else:
                    for numero in lista: #Para que sea una matriz
                        if type(numero)!=int and type(numero)!=float:
                            esMatriz=False
    return esMatriz

def vertical(matriz):
    if es_matriz(matriz)==False:
        return "No es una matriz."
    else:
        reflejoVertical=[]
        for lista in matriz:
            lista=lista[::-1]
            reflejoVertical+=[lista]
    return reflejoVertical

#15
#Entradas: vector
#Salidas: 2 vectores

def esVector15(vector):
    esVector=True
    if type(vector)!=list:
        esVector=False
    else:
        contador=0
        for lista in vector:
            if type(lista)!=list:
                esVector=False
                break
            contador+=1
            for elemento in lista:
                if type(elemento)!=int and type(elemento)!=float:
                    esVector=False
                    break
        if contador>=2:
            for lista in vector:
                if len(lista)!=1:
                    esVector=False
    return esVector, contador

def descomponer(vector):
    if esVector15(vector)[0]==False:
        return "Error."
    else:
        vector1=[]
        vector2=[]
        i=0
        if esVector15(vector)[1]<2: #Vector fila
            for lista in vector:
                largoLista=len(lista)-1
                while i<=largoLista:
                    if i%2==0:
                        vector1+=[lista[i]]
                    else:
                        vector2+=[lista[i]]
                    i+=1
        else:
            largoVector=len(vector)-1
            while i<=largoVector:
                if i%2==0:
                    vector1+=[vector[i]]
                else:
                    vector2+=[vector[i]]
                i+=1
        return {"Vector 1":vector1, "Vector 2": vector2}