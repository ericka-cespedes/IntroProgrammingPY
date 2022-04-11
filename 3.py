###EJERCICIO 1 ###
#Entradas: 2 elementos (pat, ins) y una lista (lista)
#Salidas: lista
#Restricciones: lista debe ser una lista
def insertar(pat, ins, lista):
    if type(lista)!=list:
        return "El tercer argumento debe ser una lista."
    else:
        if lista.count(pat)!=0:
            ubicacion=lista.index(pat)+1
            copiaLista=lista
            while copiaLista.count(pat)!=0:
                lista.insert(ubicacion, ins)
                copiaLista=lista[ubicacion+1:]
                if copiaLista.count(pat)!=0:
                    ubicacion+=copiaLista.index(pat)+2
        return lista

###Solución usando for

def insertar2(pat, ins, lista):
    if type(lista)!=list:
        return "El tercer argumento debe ser una lista."
    else:
        if lista.count(pat)!=0:
            copiaLista=lista
            ubicacion=0
            for x in lista:
                if x==pat:
                    ubicacion+=copiaLista.index(x)+1
                    lista.insert(ubicacion, ins)
                    copiaLista=lista[ubicacion+1:]
                    ubicacion+=1
        return lista

###EJERCICIO 2 ###
#Entradas: matriz cuadrada: lista de listas: (MatA)
#Salidas: matriz: (matrizResult)
#Restricciones: matA debe ser una matriz cuadrada (m=n)
                #len(lista1)=len(lista2)=len(listan)
                #len(MatA)=len(lista1)
    #matrizResult debe ser una matriz triangular superior
    #numeros debajo de la diagonal igual a 0 y no se toman en cuenta en la suma

def exTrianSup(MatA):
    matriz=True
    lista0=MatA[0]
    if type(MatA)!=list:
        matriz=False
    else:
        for lista in MatA:
            if type(lista)!=list:
                matriz=False
            else:
                if len(lista0)!=len(lista): #len(lista1)=len(lista2)=len(listan)
                    matriz=False
                elif len(lista0)!=len(MatA): #len(MatA)=len(lista1)
                    matriz=False
                else:
                    for numero in lista: #Para que sea una matriz
                        if type(numero)!=int and type(numero)!=float:
                            matriz=False
    if matriz==False:
        return "No es una matriz cuadrada."
    else:
        matrizResult=[]
        listaResult=[]
        ultimoNumero=0
        i=-1
        cuentaCeros=0
        listaCeros=[]
        for lista in MatA:
            for numero in lista:
                if lista.index(numero)>(cuentaCeros-1):
                    numero+=ultimoNumero
                    listaResult+=[numero]
                    i+=1
                    ultimoNumero=listaResult[i]
            matrizResult+=[listaResult]
            i=-1
            listaResult=[]
            listaCeros+=[0]
            cuentaCeros+=1
            i+=cuentaCeros
            listaResult+=listaCeros
        return matrizResult