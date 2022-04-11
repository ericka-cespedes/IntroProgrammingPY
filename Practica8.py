#1
#Entradas: vector (1 columna o 1 fila): [[],[],[]] o [[]]
#Salidas: True (elementos en orden ascendente) o False
def validaVector(vector):
    if type(vector)!=list:
        return False
    else:
        return validaVectorAux(vector, 0)

def validaVectorAux(vector, i):
    if len(vector)-1==i: #Para no cambiar vector
        if i>=2: #Vector columna
            return validaVectorAux2(vector)
        else:
            return True

    else:
        if type(vector[i])!=list: #lista in vector
            return False
        else:
            if validaElementos(vector[i])==False:
                return False
            else:
                return validaVectorAux(vector, i+1)

def validaElementos(lista):
    if lista==[]:
        return True
    elif type(lista[0]) in [int,float]:
        return validaElementos(lista[1:])
    else:
        return False

def validaVectorAux2(vector):
    if vector==[]:
        return True
    elif len(vector[0])!=1:
        return False
    else:
        return validaVectorAux2(vector[1:])

#Función Principal
def vectorAscendente(vector):
    if validaVector(vector)==False:
        raise Exception("Error")
    else:
        if len(vector)==1: #Vector Fila
            vectorOrdenado=[ordenar(vector[0])]
            return vectorOrdenado==vector
        else: #Vector Columna
            return vectorColumna(vector)

def ordenar(lista):
    if estaOrdenada(lista)==True:
        return lista
    else:
        return ordenar(ordenarAux(lista))

def estaOrdenada(lista):
    if lista[1:]==[]:
        return True
    elif lista[0] <= lista[1]:
        return estaOrdenada(lista[1:])
    else:
        return False

def ordenarAux(lista):
    if lista[1:] == []:
        return [lista[0]]
    else:
        if lista[0] > lista[1]:
            m = lista[0]
            lista[0] = lista[1]
            lista[1] = m
        return [lista[0]] + ordenarAux(lista[1:])

def vectorColumna(vector):
    if vector[1:]==[]:
        return True
    elif vector[0][0]>vector[1][0]:
        return False
    else:
        return vectorColumna(vector[1:])

#---------------------------------------------------------------------------------

#2
#Entradas: 2 strings
#Salidas: # de palabras IGUALES que están en f1 y f2

def repetidas(f1, f2):
    if type(f1)!=str or type(f2)!=str:
        raise Exception("Error")
    else:
        return repetidasAux(f1.split(" "), f2.split(" "), 0)

def repetidasAux(f1, f2, contador):
    if f1==[]:
        return contador
    else:
        return repetidasAux2(f1, f2, f2, contador)

def repetidasAux2(f1, f2, f3, contador):
    if f3==[]:
        return repetidasAux(f1[1:], f2, contador)
    else:
        if f1[0] == f3[0]:
            contador+=1
        return repetidasAux2(f1, f2, f3[1:], contador)

#Ejemplo:
#>>> repetidas("hola mundo feliz feliz", "droppy es un perro feliz feliz")
#4

#----------------------------------------------------------------------------------

#3
#Entradas: string
#Salidas: string (caracteres minuscula -> mayuscula, y viceversa)

def swapcase(string):
    if type(string)!=str:
        raise Exception("Error")
    else:
        return swapcaseAux("", string)

def swapcaseAux(string1, string2):
    if string2=="":
        return string1
    else:
        letra=string2[0]
        if letra.islower()==True:
            letra = letra.upper()
        else:
            letra = letra.lower()

        return swapcaseAux(string1 + letra, string2[1:])

#----------------------------------------------------------------------------------

#4
#Entradas: matriz (2 filas min)
#Salidas: reflejo horizontal de esa matriz
#Matriz horizontal: tiene más columnas que filas

def validaMatriz(matriz):
    if type(matriz)!=list or matriz==[] or type(matriz[0])!=list:
        return False
    else:
        return validaMatrizAux(matriz, len(matriz[0]))

def validaMatrizAux(matriz, largoFila):
    if matriz==[]:
        return True
    elif type(matriz[0])!=list:
        return False
    elif largoFila!=len(matriz[0]):
        return False
    else:
        if validaElementos(matriz[0])==False:
            return False
        else:
            return validaMatrizAux(matriz[1:], largoFila)

def validaElementos(lista):
    if lista==[]:
        return True
    elif type(lista[0]) in [int,float]:
        return validaElementos(lista[1:])
    else:
        return False

#Función Principal
def reflejoHorizontal(matriz):
    if validaMatriz(matriz)==False:
        raise Exception("Error")
    elif len(matriz)<2: #2 filas mínimo
        raise Exception("Error: No cumple los requisitos del problema.")
    else:
        return reflejoHorizontalAux(matriz, [], [])

def reflejoHorizontalAux(matriz, fila, rH):
    if matriz==[]:
        return rH #reflejoHorizontal=[[fila],[fila],...]
    else:
        fila+=matriz[-1]
        return reflejoHorizontalAux(matriz[:-1], [], rH+[fila])

#----------------------------------------------------------------------------------

#5
#Entradas: matriz nxm A[i][j]
#Salidas: transpuesta de la matriz At[i][j]=A[j][i] mxn

def matrizTranspuesta(matriz):
    if validaMatriz(matriz)==False:
        raise Exception("Error")
    else:
        return matrizTranspuestaAux(matriz, [], 0, 0, [])

def matrizTranspuestaAux(matriz, fila, i, j, mT):
    if len(matriz[0])==j: #len(lista1)=len(lista2)=len(listan)
        return mT
    elif len(matriz)==i:
        return matrizTranspuestaAux(matriz, [], 0, j+1, mT + [fila])
    else:
        return matrizTranspuestaAux(matriz, fila + [matriz[i][j]], i+1, j, mT)

#----------------------------------------------------------------------------------

#6
#Entradas: matriz nxm, vector fila tamaño n (misma cantidad de filas)
#Salidas: vector

def multiplicar(vector, matriz):
    if validaMatriz(matriz)==False:
        raise Exception("Error")
    elif type(vector)!=list:
        raise Exception("Error")
    elif validaElementos(vector)==False:
        raise Exception("Error")
    elif len(vector)!=len(matriz):
        raise Exception("Error")
    else:
        return multiplicarAux(vector, matriz)

def multiplicarAux(vector, matriz, filaResultado=[]):
    if matriz==[]:
        return filaResultado
    else:
        filaM=matriz[0]
        elemento=vector[0]*filaM[0]
        filaResultado+=[elemento]
        return multiplicarAux(vector[1:], matriz[1:], filaResultado)

#----------------------------------------------------------------------------------
#7
#Entradas: str1, str2, inicio, fin
#Salidas: indice (str2 in str1)

def largo(string, contador=0):
    if string=="":
        return contador
    else:
        return largo(string[1:], contador+1)

#Función Principal
def buscar(str1, str2, inicio, fin):
    if type(str1)!=str or type(str2)!=str or type(inicio)!=int or type(fin)!=int:
        raise Exception("Error")
    elif fin<=inicio:
        raise Exception("Error")
    elif inicio>=largo(str1) or fin>largo(str1):
        raise Exception("Error")
    else:
        str1 = str1[inicio:fin]
        return find(str2, str1, largo(str2))

def find(string1, string2, largo2, contador=0): #string1 en string2
    if largo(string2) < contador:
        return -1
    else:
        if string1==string2[contador:contador+largo2]:
            return contador
        else:
            return find(string1, string2, largo2, contador+1)

#----------------------------------------------------------------------------------

#8
#Entradas: 2 arreglos
#Salidas: True o False

def subVector(vec1, vec2):
    if type(vec1)!=list or type(vec2)!=list:
        raise Exception("Error")
    else:
        return subVectorAux(vec1, vec2, len(vec1))

def subVectorAux(vec1, vec2, largo, contador=0):
    if len(vec2) < contador:
        return False
    else:
        if vec1 == vec2[contador:contador+largo]:
            return True
        else:
            return subVectorAux(vec1, vec2, largo, contador+1)

#----------------------------------------------------------------------------------

#9
#Entradas: 2 vectores del mismo tamaño
#Salidas: True o False

def validaVectorFila(vector):
    if type(vector)!=list:
        return False
    else:
        return validaElementos(vector)

def validaElementos(lista):
    if lista==[]:
        return True
    elif type(lista[0]) in [int,float]:
        return validaElementos(lista[1:])
    else:
        return False

#Función Principal
def unirOrdenar(vector1, vector2):
    if validaVectorFila(vector1)==False or validaVectorFila(vector2)==False:
        raise Exception("Error")
    elif len(vector1)!=len(vector2):
        raise Exception("Error: No cumple los requisitos del problema.")
    else:
        resultado = vector1[0:len(vector1)] + vector2[0:len(vector2)]
        return ordenar(resultado)

def ordenar(lista):
    if estaOrdenada(lista)==True:
        return lista
    else:
        return ordenar(ordenarAux(lista))

def estaOrdenada(lista):
    if lista[1:]==[]:
        return True
    elif lista[0] <= lista[1]:
        return estaOrdenada(lista[1:])
    else:
        return False

def ordenarAux(lista):
    if lista[1:] == []:
        return [lista[0]]
    else:
        if lista[0] > lista[1]:
            m = lista[0]
            lista[0] = lista[1]
            lista[1] = m
        return [lista[0]] + ordenarAux(lista[1:])

#----------------------------------------------------------------------------------

#10
#Entradas: matriz cuadrada nxn
#Salidas: vector diagonal principal de la matriz

def validaMatriz(matriz):
    if type(matriz)!=list or matriz==[] or type(matriz[0])!=list:
        return False
    else:
        return validaMatrizAux(matriz, len(matriz[0]))

def validaMatrizAux(matriz, largoFila):
    if matriz==[]:
        return True
    elif type(matriz[0])!=list:
        return False
    elif largoFila!=len(matriz[0]):
        return False
    else:
        if validaElementos(matriz[0])==False:
            return False
        else:
            return validaMatrizAux(matriz[1:], largoFila)

def validaElementos(lista):
    if lista==[]:
        return True
    elif type(lista[0]) in [int,float]:
        return validaElementos(lista[1:])
    else:
        return False

#Función Principal
def diagonalPrincipal(matriz):
    if validaMatriz(matriz)==False:
        raise Exception("Error")
    elif len(matriz[0])!=len(matriz): #Matriz cuadrada
        raise Exception("Error")
    else:
        return diagonalPrincipalAux(matriz, 0, [])

def diagonalPrincipalAux(matriz, j, vector):
    if matriz==[]:
        return vector
    else:
        return diagonalPrincipalAux(matriz[1:], j+1, vector+[matriz[0][j]])

#----------------------------------------------------------------------------------

#11
#Entradas: 2 matrices
#Salidas: producto matricial

def matrizConformable(A,B):
    columnasA = len(A[0])
    filasB = len(B)
    if columnasA != filasB:
        return False
    else:
        return True

#Función Principal
def productoMatriz(A,B):
    if validaMatriz(A)==False or validaMatriz(B)==False:
        raise Exception("Error")
    elif matrizConformable(A,B)==False:
        raise Exception("Error")
    else:
        return productoMatrizAux(A,B, [])

def productoMatrizAux(A, B , resultado):
    if A==[]:
        return resultado
    else:
        resultado+=[multiplicarFilaColumna(A[0], B)]
        return productoMatrizAux(A[1:], B , resultado)

def multiplicarFilaColumna(filaA, B, elementoResultado=0, filaResultado=[], i=0, j=0):
    if i==len(filaA):
        return filaResultado
    else:
        if j==len(B[i]):
            return multiplicarFilaColumna(filaA, B, 0, filaResultado+[elementoResultado], i+1, 0)
        else:
            filaB=B[j]
            elemento=filaB[i]*filaA[j]
            elementoResultado+=elemento
            return multiplicarFilaColumna(filaA, B, elementoResultado, filaResultado, i, j+1)

#12
#Entradas: matriz
#Salidas: reflejo horizontal

def horizontal(matriz):
    if validaMatriz(matriz)==False:
        raise Exception("Error")
    else:
        return reflejoHorizontalAux(matriz, [], []) #Ejercicio 4

#13
#Entradas: matriz
#Salidas: reflejo vertical

def vertical(matriz):
    if validaMatriz(matriz)==False:
        raise Exception("Error")
    else:
        return reflejoVerticalAux(matriz, [])

def reflejoVerticalAux(matriz, rV):
    if matriz==[]:
        return rV
    else:
        fila=matriz[0]
        fila=fila[::-1]
        return reflejoVerticalAux(matriz[1:], rV+[fila])

#14
#Entradas: vector
#Salidas: 2 vectores

def es_vector_columna(vector, i):
    if vector==[]:
        if i>1:
            return True
        else:
            return False
    else:
        return es_vector_columna(vector[1:], i+1)

def descomponer(vector):
    if validaVector(vector)==False:
        raise Exception("Error")
    else:
        if es_vector_columna(vector, 0)==True: #Vector columna
            if len(vector)%2!=0:
                raise Exception("Error")
            else:
                return descomponerVC(vector, [], [], 0)
        else: #Vector fila
            if len(vector[0])%2!=0:
                raise Exception("Error")
            else:
                return descomponerVF(vector[0], [], [], 0)

def descomponerVC(vector, vector1, vector2, i):
    if len(vector) == i:
        return {"Vector 1": vector1, "Vector 2": vector2}
    else:
        if i%2==0:
            vector1+=[vector[i]]
        else:
            vector2+=[vector[i]]

        return descomponerVC(vector, vector1, vector2, i+1)

def descomponerVF(vector, vector1, vector2, i):
    if len(vector) == i:
        return {"Vector 1":vector1, "Vector 2": vector2}
    else:
        if i%2==0:
            vector1+=[vector[i]]
        else:
            vector2+=[vector[i]]

        return descomponerVF(vector, vector1, vector2, i+1)

#15

#Triangular superior

def trianSup(matriz):
    if validaMatriz(matriz)==False:
        raise Exception("Error")
    elif len(matriz)!=len(matriz[0]): #Matriz cuadrada
        raise Exception("Error")
    else:
        return trianSupAux(matriz, 0, 0)

def trianSupAux(matriz, i, j):
    if len(matriz)==i: #Recorrio todas las filas
        return True
    elif len(matriz)==j: #Recorrio 1 fila
        return trianSupAux(matriz, i+1, 0) #reset j
    else:
        if i<=j:
            if matriz[i][j]==0:
                return False
            else:
                return trianSupAux(matriz, i, j+1)
        else:
            if matriz[i][j]!=0:
                return False
            else:
                return trianSupAux(matriz, i, j+1)

#Triangular inferior

def trianInf(matriz):
    if validaMatriz(matriz)==False:
        raise Exception("Error")
    elif len(matriz)!=len(matriz[0]): #Matriz cuadrada
        raise Exception("Error")
    else:
        return trianInfAux(matriz, 0, 0)

def trianInfAux(matriz, i, j):
    if len(matriz)==i: #Recorrio todas las filas
        return True
    elif len(matriz)==j: #Recorrio 1 fila
        return trianInfAux(matriz, i+1, 0) #reset j
    else:
        if i>=j:
            if matriz[i][j]==0:
                return False
            else:
                return trianInfAux(matriz, i, j+1)
        else:
            if matriz[i][j]!=0:
                return False
            else:
                return trianInfAux(matriz, i, j+1)

#Diagonal

def diagonal(matriz):
    if validaMatriz(matriz)==False:
        raise Exception("Error")
    elif len(matriz)!=len(matriz[0]): #Matriz cuadrada
        raise Exception("Error")
    else:
        return diagonalAux(matriz, 0, 0)

def diagonalAux(matriz, i, j):
    if len(matriz)==i: #Recorrio todas las filas
        return True
    elif len(matriz)==j: #Recorrio 1 fila
        return diagonalAux(matriz, i+1, 0) #reset j
    else:
        if i==j:
            if matriz[i][j]==0:
                return False
            else:
                return diagonalAux(matriz, i, j+1)
        else:
            if matriz[i][j]!=0:
                return False
            else:
                return diagonalAux(matriz, i, j+1)

#Identidad

def identidad(matriz):
    if validaMatriz(matriz)==False:
        raise Exception("Error")
    elif len(matriz)!=len(matriz[0]): #Matriz cuadrada
        raise Exception("Error")
    else:
        return identidadAux(matriz, 0, 0)

def identidadAux(matriz, i, j):
    if len(matriz)==i: #Recorrio todas las filas
        return True
    elif len(matriz)==j: #Recorrio 1 fila
        return identidadAux(matriz, i+1, 0) #reset j
    else:
        if i==j:
            if matriz[i][j]!=1:
                return False
            else:
                return identidadAux(matriz, i, j+1)
        else:
            if matriz[i][j]!=0:
                return False
            else:
                return identidadAux(matriz, i, j+1)

#Nula

def nula(matriz):
    if validaMatriz(matriz)==False:
        raise Exception("Error")
    else:
        return nulaAux(matriz, 0, 0)

def nulaAux(matriz, i, j):
    if len(matriz)==i: #Recorrio todas las filas
        return True
    elif len(matriz[i])==j: #Recorrio 1 fila
        return nulaAux(matriz, i+1, 0) #reset j
    else:
        if matriz[i][j]!=0:
            return False
        else:
            return nulaAux(matriz, i, j+1)