#1
#Entradas: vector1, vector2
#Salidas: True o False
#Restricciones: vector fila no nulos; vector1=vector2
def validaVector(vector):
    if type(vector)!=list or vector==[]:
        return False
    else:
        return validaVectorAux(vector)

def validaVectorAux(vector):
    if vector==[]:
        return True
    elif type(vector[0]) in [int, float]: #vector fila
        return validaVectorAux(vector[1:])
    else:
        return False

#validaVector() se usa en ejercicio 2

def vectorNoNulo(vector):
    if vector==[]:
        return False
    elif vector[0]!=0: #Encuentra elemento diferente de 0
        return True
    else:
        return vectorNoNulo(vector[1:])

def ortogonales(vector1, vector2):
    if validaVector(vector1)==False or validaVector(vector2)==False:
        raise Exception("Error")
    elif vectorNoNulo(vector1)==False or vectorNoNulo(vector2)==False:
        raise Exception("Error")
    elif len(vector1)!=len(vector2):
        raise Exception("Error")
    else:
        return ortogonalesAux(vector1, vector2, 1, 0)

def ortogonalesAux(vector1, vector2, mult, suma):
    if vector1==[]: #len(vector1)==len(vector2)
        return suma==0
    else:
        mult = vector1[0] * vector2[0]
        return ortogonalesAux(vector1[1:], vector2[1:], 1, suma + mult)

#---------------------------------------------------------------------------

#2
#Entradas: matriz
#Salidas: True o False
#Restricciones: matriz cuadrada de 2 a 10; filas o columnas

def validaMatriz(matriz):
    if type(matriz)!=list or matriz==[]:
        return False
    elif type(matriz[0])!=list: #Para evitar errores con len()
        return False
    else:
        return validaMatrizAux(matriz, len(matriz[0]))

def validaMatrizAux(matriz, largoFila):
    if matriz==[]:
        return True
    elif type(matriz[0])!=list:
        return False
    elif largoFila!=len(matriz[0]): #Para que sea matriz
        return False
    else:
        if validaVector(matriz[0])==False:
            return False
        else:
            return validaMatrizAux(matriz[1:], largoFila)

def trianSup(matriz):
    if validaMatriz(matriz)==False:
        raise Exception("Error")
    elif len(matriz)!=len(matriz[0]): #Matriz cuadrada
        raise Exception("Error")
    elif len(matriz) not in range(2,10):
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