#----------------------------------------------------------------------------------------------------------------------------------------
# Solución Qüiz Extra
# II semestre 2017
# Realizada por: Ing. Eduardo A. Canessa M., M.Sc.
#----------------------------------------------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------------------------------------------
# Ejercicio 1: Funcion ortogonales(vec1, vec2)
# Entradas: dos vectores
# Salidas: indicación de si los vectores son o no son ortogonales
# Restricciones: los vectores deben de ser numéricos
#----------------------------------------------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------------------------------------------
# Ejercicio 2: Funcion trianSup(matriz)
# Entrada: matriz
# Salida: True o False de acuerdo a si la matriz cumple o no la condicióno de matriz triangular superior
# Restricciones: matriz cuadrada
#----------------------------------------------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------------------------------------------
# ---- CASOS DE PRUEBA ----------------
print("\n**********************************************************************************************************")
print("*************************************INICIO DE PROTOCOLO DE PRUEBAS***************************************")
print("**********************************************************************************************************")
print("=========================================================================================================")
print("Resultados para los casos de prueba Qüiz Extra de Introduccion a la Programación ")
print("=========================================================================================================")
#Inicialización de variables de prueba
errores=0
buenas=0
erroresNoId=0

########################################
# Función de validación de error:
########################################
def validaE(dato,listaE):
    if dato in listaE:
        return True
    else:
        while listaE!=[]:
            if listaE[0] in dato:
                return True
            listaE=listaE[1:]
        return False

########################################
# Fin de Función de validación de error
########################################

# Ejercicio 1: ortogonales(vec1, vec2)
print("\n=========================================================================================================")
print("============================================Ejercicio 1===================================================")
print("=========================================================================================================")
print("Caso 1: Validacion con dos vectores de números enteros ortogonales")
print("ortogonales([1,2,1,4],[-1,-1,-1,1])")
print("Respuesta esperada: True")
try:
    respuesta=ortogonales([1,2,1,4],[-1,-1,-1,1])
    if respuesta==True:
        buenas+=1
        print("Respuesta esperada!! Este caso retorna:",respuesta)
    else:
        print("Errores en la respuesta.  Su respuesta da: ",respuesta)
except Exception as cadena:
    x=cadena.args
    print("**************************************************")
    print("Este ejercicio presenta problemas de ejecución....")
    print("**************************************************")
    erroresNoId+=1
    print("Genera el siguiente error: ",x[0])
print("---------------------------------------------------------------------------------------------------------")
print("Caso 2: Validación con dos vectores de números enteros no ortogonales")
print("ortogonales([1,5,3,1,4,-30,5],[5,4,2,1,1,1,5])")
print("Respuesta esperada: False")
try:
    respuesta=ortogonales([1,5,3,1,4,-30,5],[5,4,2,1,1,1,5])
    if respuesta==False:
        buenas+=1
        print("Respuesta esperada!! Este caso retorna:",respuesta)
    else:
        print("Errores en la respuesta.  Su respuesta da: ",respuesta)
except Exception as cadena:
    x=cadena.args
    print("**************************************************")
    print("Este ejercicio presenta problemas de ejecución....")
    print("**************************************************")
    erroresNoId+=1
    print("Genera el siguiente error: ",x[0])
print("---------------------------------------------------------------------------------------------------------")
print("Caso 3: Validacion con dos vectores de números float ortogonales")
print("ortogonales([0,0,27.34,0,1],[34.6,2.78,0,3.4,0])")
print("Respuesta esperada: True")
try:
    respuesta=ortogonales([0,0,27.34,0,1],[34.6,2.78,0,3.4,0])
    if respuesta==True:
        buenas+=1
        print("Respuesta esperada!! Este caso retorna:",respuesta)
    else:
        print("Errores en la respuesta.  Su respuesta da: ",respuesta)
except Exception as cadena:
    x=cadena.args
    print("**************************************************")
    print("Este ejercicio presenta problemas de ejecución....")
    print("**************************************************")
    erroresNoId+=1
    print("Genera el siguiente error: ",x[0])
print("---------------------------------------------------------------------------------------------------------")
print("Caso 4: Validacion con dos vectores de números float no ortogonales")
print("ortogonales([1,2,3],[-0.4,7.3,-2.5])")
print("Respuesta esperada: False")
try:
    respuesta=ortogonales([1,2,3],[-0.4,7.3,-2.5])
    if respuesta==False:
        buenas+=1
        print("Respuesta esperada!! Este caso retorna:",respuesta)
    else:
        print("Errores en la respuesta.  Su respuesta da: ",respuesta)
except Exception as cadena:
    x=cadena.args
    print("**************************************************")
    print("Este ejercicio presenta problemas de ejecución....")
    print("**************************************************")
    erroresNoId+=1
    print("Genera el siguiente error: ",x[0])

#######################################################
#Inicia sección de pruebas de robustez del ejercicio
#######################################################

print("---------------------------------------------------------------------------------------------------------")
print("Caso 5: Prueba de robustez - Ingreso de vector nulo como primer vector de entrada")
print("ortogonales([0,0,0,0,0,0,0,0,0,0,0,0],[1,-1,1,-1,1,-1,1,-1,1,-1,1,-1])")
print("Respuesta esperada: 'ERROR'")
try:
    respuesta=ortogonales([0,0,0,0,0,0,0,0,0,0,0,0],[1,-1,1,-1,1,-1,1,-1,1,-1,1,-1])
    if validaE(respuesta,['Error','ERROR','error']):
        errores+=1
        print("Correcto!! Retorna como salida: ",respuesta)
    else:
        print("Errores en la respuesta.  Su respuesta da: ",respuesta)
except Exception as cadena:
    x=cadena.args
    if validaE(x[0],['Error','ERROR','error']):
        errores+=1
        print("Correcto!! Retorna la Excepción: ",x[0])
    else:
        print("**************************************************")
        print("Este ejercicio presenta problemas de ejecución....")
        print("**************************************************")
        erroresNoId+=1
        print("Genera el siguiente error: ",x[0])
print("---------------------------------------------------------------------------------------------------------")
print("Caso 6: Prueba de robustez - Ingreso de vector nulo como segundo vector de entrada")
print("ortogonales([1,-1,1,-1,1,-1,1,-1,1,-1,1,-1],[0,0,0,0,0,0,0,0,0,0,0,0])")
print("Respuesta esperada: 'ERROR'")
try:
    respuesta=ortogonales([1,-1,1,-1,1,-1,1,-1,1,-1,1,-1],[0,0,0,0,0,0,0,0,0,0,0,0])
    if validaE(respuesta,['Error','ERROR','error']):
        errores+=1
        print("Correcto!! Retorna como salida: ",respuesta)
    else:
        print("Errores en la respuesta.  Su respuesta da: ",respuesta)
except Exception as cadena:
    x=cadena.args
    if validaE(x[0],['Error','ERROR','error']):
        errores+=1
        print("Correcto!! Retorna la Excepción: ",x[0])
    else:
        print("**************************************************")
        print("Este ejercicio presenta problemas de ejecución....")
        print("**************************************************")
        erroresNoId+=1
        print("Genera el siguiente error: ",x[0])
print("---------------------------------------------------------------------------------------------------------")
print("Caso 7: Prueba de robustez - Ingreso de vectores de longitud diferente")
print("ortogonales([1,1,4,-30,5],[5,4,2,1,1,1,5])")
print("Respuesta esperada: 'ERROR'")
try:
    respuesta=ortogonales([1,1,4,-30,5],[5,4,2,1,1,1,5])
    if validaE(respuesta,['Error','ERROR','error']):
        errores+=1
        print("Correcto!! Retorna como salida: ",respuesta)
    else:
        print("Errores en la respuesta.  Su respuesta da: ",respuesta)
except Exception as cadena:
    x=cadena.args
    if validaE(x[0],['Error','ERROR','error']):
        errores+=1
        print("Correcto!! Retorna la Excepción: ",x[0])
    else:
        print("**************************************************")
        print("Este ejercicio presenta problemas de ejecución....")
        print("**************************************************")
        erroresNoId+=1
        print("Genera el siguiente error: ",x[0])
print("---------------------------------------------------------------------------------------------------------")
print("Caso 8: Prueba de robustez - Ingreso de un string en vez de uno de los vectores")
print("ortogonales([1,1,4,-30,5],'hola')")
print("Respuesta esperada: 'ERROR'")
try:
    respuesta=ortogonales([1,1,4,-30,5],'hola')
    if validaE(respuesta,['Error','ERROR','error']):
        errores+=1
        print("Correcto!! Retorna como salida: ",respuesta)
    else:
        print("Errores en la respuesta.  Su respuesta da: ",respuesta)
except Exception as cadena:
    x=cadena.args
    if validaE(x[0],['Error','ERROR','error']):
        errores+=1
        print("Correcto!! Retorna la Excepción: ",x[0])
    else:
        print("**************************************************")
        print("Este ejercicio presenta problemas de ejecución....")
        print("**************************************************")
        erroresNoId+=1
        print("Genera el siguiente error: ",x[0])
print("---------------------------------------------------------------------------------------------------------")
print("Caso 9: Prueba de robustez - Ingreso de un vector no numérico en uno de los vectores")
print("ortogonales([1,'1',1,1,1,1,1,1,1,1,1,1],[1,-1,1,-1,1,-1,1,-1,1,-1,1,-1])")
print("Respuesta esperada: 'ERROR'")
try:
    respuesta=ortogonales([1,'1',1,1,1,1,1,1,1,1,1,1],[1,-1,1,-1,1,-1,1,-1,1,-1,1,-1])
    if validaE(respuesta,['Error','ERROR','error']):
        errores+=1
        print("Correcto!! Retorna como salida: ",respuesta)
    else:
        print("Errores en la respuesta.  Su respuesta da: ",respuesta)
except Exception as cadena:
    x=cadena.args
    if validaE(x[0],['Error','ERROR','error']):
        errores+=1
        print("Correcto!! Retorna la Excepción: ",x[0])
    else:
        print("**************************************************")
        print("Este ejercicio presenta problemas de ejecución....")
        print("**************************************************")
        erroresNoId+=1
        print("Genera el siguiente error: ",x[0])
print("---------------------------------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------")
print("-------------------  Final de pruebas del ejercicio 1  --------------------------")
print("---------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------")
print(" Respuestas buenas: ", buenas, "\n Excepciones por errores de entrada correctamente identificados: ",errores,"\n Errores no identificados debido a errores del desarrollador: ", erroresNoId)
calif1=round(((buenas+errores/5)/5*100),2)
print(" Calificación Ejercicio #1: ", calif1)
buenas=errores=erroresNoId=0

#Casos de robustez: 5
#Casos de entradas correctas: 4

# Problema 2: trianSup(matriz)
print("\n=========================================================================================================")
print("============================================Ejercicio 2===================================================")
print("=========================================================================================================")
print("Caso 1: Validación para matriz triangular superior de 3x3")
print("trianSup([[1, 8, 3],\n          [0, 5, 4],\n          [0, 0, 5]])")
print("Respuesta esperada: True")
print("Este caso retorna:",trianSup([[1, 8, 3], [0, 5, 4], [0, 0, 5]]))
try:
    respuesta=trianSup([[1, 8, 3], [0, 5, 4], [0, 0, 5]])
    if respuesta==True:
        buenas+=1
        print("Correcto!! Este caso retorna:",respuesta)
    else:
        print("Errores en la respuesta.  Su respuesta da: ",respuesta)
except Exception as cadena:
    x=cadena.args
    print("**************************************************")
    print("Este ejercicio presenta problemas de ejecución....")
    print("**************************************************")
    erroresNoId+=1
    print("Genera el siguiente error: ",x[0])
print("---------------------------------------------------------------------------------------------------------")
print("Caso 2: Validación para matriz triangular superior de 6x6")
print("trianSup([[10, 7, 5, 8, 1, 3],\n          [0, 1, 23, 12, 11, 2],\n          [0, 0, 4, 6, 1, 8],\n          [0, 0, 0, 16, 11, 18],\n          [0, 0, 0, 0, 71, 68],\n          [0, 0, 0, 0, 0, 48]])")
print("Respuesta esperada: True")
try:
    respuesta=trianSup([[10, 7, 5, 8, 1, 3], [0, 1, 23, 12, 11, 2], [0, 0, 4, 6, 1, 8], [0, 0, 0, 16, 11, 18], [0, 0, 0, 0, 71, 68], [0, 0, 0, 0, 0, 48]])
    if respuesta==True:
        buenas+=1
        print("Correcto!! Este caso retorna:",respuesta)
    else:
        print("Errores en la respuesta.  Su respuesta da: ",respuesta)
except Exception as cadena:
    x=cadena.args
    print("**************************************************")
    print("Este ejercicio presenta problemas de ejecución....")
    print("**************************************************")
    erroresNoId+=1
    print("Genera el siguiente error: ",x[0])
print("---------------------------------------------------------------------------------------------------------")
print("Caso 3: Validación para matriz no triangular superior de 6x6 (valores bajo la diagonal diferentes de cero)")
print("trianSup([[10, 7, 5, 8, 1, 3],\n          [0, 1, 23, 12, 11, 2],\n          [0, 0, 4, 6, 1, 8],\n          [0, 1, 0, 16, 11, 18],\n          [0, 0, 0, 0, 71, 68],\n          [0, 0, 0, 0, 0, 48]])")
print("Respuesta esperada: False")
try:
    respuesta=trianSup([[10, 7, 5, 8, 1, 3], [0, 1, 23, 12, 11, 2], [0, 0, 4, 6, 1, 8], [0, 1, 0, 16, 11, 18], [0, 0, 0, 0, 71, 68], [0, 0, 0, 0, 0, 48]])
    if respuesta==False:
        buenas+=1
        print("Correcto!! Este caso retorna:",respuesta)
    else:
        print("Errores en la respuesta.  Su respuesta da: ",respuesta)
except Exception as cadena:
    x=cadena.args
    print("**************************************************")
    print("Este ejercicio presenta problemas de ejecución....")
    print("**************************************************")
    erroresNoId+=1
    print("Genera el siguiente error: ",x[0])
print("---------------------------------------------------------------------------------------------------------")
print("Caso 4: Validación para matriz no triangular superior de 6x6 (valores sobre la diagonal iguales a cero)")
print("trianSup([[10, 7, 5, 8, 1, 3],\n          [0, 1, 23, 12, 11, 2],\n          [0, 0, 4, 6, 1, 8],\n          [0, 0, 0, 16, 11, 0],\n          [0, 0, 0, 0, 71, 68],\n          [0, 0, 0, 0, 0, 48]])")
print("Respuesta esperada: False")
try:
    respuesta=trianSup([[10, 7, 5, 8, 1, 3], [0, 1, 23, 12, 11, 2], [0, 0, 4, 6, 1, 8], [0, 0, 0, 16, 11, 0], [0, 0, 0, 0, 71, 68], [0, 0, 0, 0, 0, 48]])
    if respuesta==False:
        buenas+=1
        print("Correcto!! Este caso retorna:",respuesta)
    else:
        print("Errores en la respuesta.  Su respuesta da: ",respuesta)
except Exception as cadena:
    x=cadena.args
    print("**************************************************")
    print("Este ejercicio presenta problemas de ejecución....")
    print("**************************************************")
    erroresNoId+=1
    print("Genera el siguiente error: ",x[0])


#######################################################
#Inicia sección de pruebas de robustez del ejercicio
#######################################################
print("---------------------------------------------------------------------------------------------------------")
print("Caso 5: Prueba de robustez - Ingreso de matriz de 2x3")
print("trianSup([[10, 7, 5],\n          [12, 11, 2]])")
print("Respuesta esperada: 'ERROR'")
try:
    respuesta=trianSup([[10, 7, 5], [12, 11, 2]])
    if validaE(respuesta,['Error','ERROR','error']):
        errores+=1
        print("Correcto!! Retorna como salida: ",respuesta)
    else:
        print("Errores en la respuesta.  Su respuesta da: ",respuesta)
except Exception as cadena:
    x=cadena.args
    if validaE(x[0],['Error','ERROR','error']):
        errores+=1
        print("Correcto!! Retorna la Excepción: ",x[0])
    else:
        print("**************************************************")
        print("Este ejercicio presenta problemas de ejecución....")
        print("**************************************************")
        erroresNoId+=1
        print("Genera el siguiente error: ",x[0])
print("---------------------------------------------------------------------------------")
print("Caso 6: Prueba de robustez - Ingreso de matriz de 3x2")
print("trianSup([[10, 7],\n          [12, 11],\n          [6, 1]])")
print("Respuesta esperada: 'ERROR'")
try:
    respuesta=trianSup([[10, 7], [12, 11], [6, 1]])
    if validaE(respuesta,['Error','ERROR','error']):
        errores+=1
        print("Correcto!! Retorna como salida: ",respuesta)
    else:
        print("Errores en la respuesta.  Su respuesta da: ",respuesta)
except Exception as cadena:
    x=cadena.args
    if validaE(x[0],['Error','ERROR','error']):
        errores+=1
        print("Correcto!! Retorna la Excepción: ",x[0])
    else:
        print("**************************************************")
        print("Este ejercicio presenta problemas de ejecución....")
        print("**************************************************")
        erroresNoId+=1
        print("Genera el siguiente error: ",x[0])
print("---------------------------------------------------------------------------------")
print("Caso 7: Prueba de robustez - Ingreso de matriz de 11x11")
print("trianSup([[10, 7,  5,  8,  1,  3, 1, 1, 1, 1, 1],\n          [ 0, 1, 23, 12, 11,  2, 1, 1, 1, 1, 1],\n          [ 0, 0,  4,  6,  1,  8, 1, 1, 1, 1, 1],\n          [ 0, 0,  0, 16, 11,  1, 1, 1, 1, 1, 1],\n          [ 0, 0,  0,  0, 71, 68, 1, 1, 1, 1, 1],\n          [ 0, 0,  0,  0,  0, 48, 1, 1, 1, 1, 1],\n          [ 0, 0,  0,  0,  0,  0, 1, 1, 1, 1, 1],\n          [ 0, 0,  0,  0,  0,  0, 0, 1, 1, 1, 1],\n          [ 0, 0,  0,  0,  0,  0, 0, 0, 1, 1, 1],\n          [ 0, 0,  0,  0,  0,  0, 0, 0, 0, 1, 1],\n          [ 0, 0,  0,  0,  0,  0, 0, 0, 0, 0, 1]])")
print("Respuesta esperada: 'ERROR'")
try:
    respuesta=trianSup([[10, 7, 5, 8, 1, 3, 1, 1, 1, 1, 1],[0, 1, 23, 12, 11, 2, 1, 1, 1, 1, 1],[0, 0, 4, 6, 1, 8, 1, 1, 1, 1, 1],[0, 0, 0, 16, 11, 1, 1, 1, 1, 1, 1],[0, 0, 0, 0, 71, 68, 1, 1, 1, 1, 1],[0, 0, 0, 0, 0, 48, 1, 1, 1, 1, 1],[0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],[0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],[0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]])
    if validaE(respuesta,['Error','ERROR','error']):
        errores+=1
        print("Correcto!! Retorna como salida: ",respuesta)
    else:
        print("Errores en la respuesta.  Su respuesta da: ",respuesta)
except Exception as cadena:
    x=cadena.args
    if validaE(x[0],['Error','ERROR','error']):
        errores+=1
        print("Correcto!! Retorna la Excepción: ",x[0])
    else:
        print("**************************************************")
        print("Este ejercicio presenta problemas de ejecución....")
        print("**************************************************")
        erroresNoId+=1
        print("Genera el siguiente error: ",x[0])
print("---------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------")
print("-------------------  Final de pruebas del ejercicio 2  --------------------------")
print("---------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------")
print(" Respuestas buenas: ", buenas, "\n Excepciones por errores de entrada correctamente identificados: ",errores,"\n Errores no identificados debido a errores del desarrollador: ", erroresNoId)
calif2=round(((buenas+errores/3)/5*100),2)
print(" Calificación Ejercicio #2: ", calif2)
buenas=errores=erroresNoId=0
print("---------------------------------------------------------------------------------------------------------")
print("\n**********************************************************************************************************")
print("**************** Resumen de calificaciones de los ítems del Segundo Examen Parcial ***********************")
print("**********************************************************************************************************")
print(" Calificación Ejercicio #1: ", calif1,"%")
print(" Calificación Ejercicio #2: ", calif2,"%")
print("\n**********************************************************************************************************")
print("***********************************FINALIZACION DE PROTOCOLO DE PRUEBAS***********************************")
print("**********************************************************************************************************")