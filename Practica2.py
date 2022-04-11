###EJERCICIO 1###
#Función que implementa la multiplicación por medio de sumas sucesivas
#Entradas: 2 números: num1, num2
#Salidas: número (resultado de la multiplicación)
#Restricciones: num1 y num2 deben ser números; num2 debe ser entero
def multi(num1, num2):
    if (type(num1)!=int and type(num1)!=float):
        return "Error: el primer argumento debe ser un número."
    elif type(num2)!=int:
        return "Error: segundo argumento debe ser entero."
    else:
        numero = 0 #Salida
        while num2!=0:
            if num2>=0:
                numero+=num1
                num2-=1
            else:
                numero-=num1
                num2+=1
        return numero

###EJERCICIO 2###
#Función que recibe un número entero e invierte sus dígitos
#Entradas: número: num
#Salidas: número invertido: resultado
#Restricciones: num debe ser un número entero

def contador(num):
    contador=0
    if num==0:
        contador=1
        return contador
    else:
        while num!=0:
            if num<0:
                num=abs(num)
            else:
                num//=10
                contador+=1
        return contador

def invertir(num):
    if type(num)!=int:
        return "El número ingresado debe ser entero."
    else:
        resultado=0
        numeroNegativo=False
        if num<0:
            num=abs(num)
            numeroNegativo=True
        while num!=0:
            ultimoDigito=num%10
            digitos=contador(num)
            resultado+=ultimoDigito*10**(digitos-1)
            digitos-=1
            num//=10
        if numeroNegativo:
            resultado*=-1
        return resultado
###EJERCICIO 3###
#Función que suma los dígitos de un número
#Entradas: número: num
#Salidas: número (resultado de la suma)
#Restricciones: num debe ser un número real o entero

def sumaDig(num):
    if type(num)!=int and type(num)!=float:
        return "El número debe ser entero o real."
    else:
        numero=0 #Salida
        while num!=0:
            if num<0:
                num=abs(num) #Para que ultimoDigito=num%10 funcione
            if type(num)==float: #num=122.45
                while num%1!=0: #num%1=0.45
                    num*=10  #Luego de 2 veces, num=12245.0, num%1=0
            ultimoDigito=num%10
            numero+=ultimoDigito
            num//=10
        numero=int(numero)
        return numero

###EJERCICIO 4###
#Función que determina si un número es un palíndromo o no
#Entradas: número: num
#Salidas: True o False
#Restricciones: número entero

def contador(numero):
    if numero==0:
        contador=1
        return contador
    elif numero>0:
        contador=0
    else:
        numero=abs(numero)
        contador=0
    while numero!=0:
        numero//=10
        contador+=1
    return contador

def palindromo(num):
    if type(num)!=int:
        return "Se debe ingresar un número entero."
    else:
        digitos=contador(num)
        numero=num
        numeroInverso=0
        numeroNegativo=False
        if num<0:
            num=abs(num)
            numeroNegativo=True
        while numero!=0:
            ultimoDigito=numero%10
            numeroInverso+=ultimoDigito*10**(digitos-1)
            digitos-=1
            numero//=10
        if numeroNegativo:
            numeroInverso*=-1
        return num==numeroInverso

###EJERCICIO 5###
#Función que calcula el resultado de una sumatoria
#Entradas: límite superior de una sumatoria: n
#Salidas: resultado de la sumatoria: resultado
#Restricciones: n debe ser un número entero mayor a 0

def sumaCoc(n):
    if type(n)!=int or n<=0:
        return "El dato ingresado debe ser entero y mayor 0."
    else:
        resultado=0
        for i in range(1,n+1):
            resultado+=i/i*(i+1)
        return resultado

###EJERCICIO 6###
#Función que calcula la aproximación de euler
#Entradas: exponente de e^x (x) y el límite superior de la sumatoria n (n)
#Salidas: aproximación del número
#Restricciones: x y n deben ser números enteros

def factorial(i):
    x=1
    if i==0:
        return x
    else:
        while i>0:
            x=x*i
            i-=1
    return x

def calculoE(x,n):
    if type(x)!=int and type(n)!=int:
        return "Los datos ingresados deben ser enteros."
    else:
        resultado=0
        i=0
        while n>i:
            resultado+=(x**i)/factorial(i)
            i+=1
        return resultado

def calculoE2(x,n):
    if type(x)!=int and type(n)!=int:
        return "Los datos ingresados deben ser enteros."
    else:
        resultado=0
        for i in range(0,n+1):
            resultado+=(x**i)/factorial(i)
        return resultado

###EJERCICIO 7###
#Función que forma un nuevo número con la multiplicación de cada dígito de 2 números
#Entradas: 2 números: num1, num2
#Salidas: número (resultado de la multiplicación)
#Restricciones: num1 y num2 deben ser números enteros del mismo tamaño

def contador(num):
    contador=0
    if num==0:
        contador=1
        return contador
    else:
        while num!=0:
            if num<0:
                num=abs(num)
            else:
                num//=10
                contador+=1
        return contador

def multdig(num1, num2):
    if type(num1)!=int or type(num2)!=int:
        return "Los datos ingresados deben ser números enteros."
    else:
        digitos1=contador(num1)
        digitos2=contador(num2)
        if digitos1!=digitos2:
            return "Los dos números deben ser del mismo tamaño."
        else:
            i=1
            num1=abs(num1)
            num2=abs(num2)
            numero=0 #Salida
            while num1!=0 and num2!=0:
                ultimoDigito1=num1%10
                ultimoDigito2=num2%10
                num1//=10
                num2//=10
                producto=ultimoDigito1*ultimoDigito2
                if producto>9:
                    producto%=10
                numero=numero+producto*i
                i=i*10
            return numero

###EJERCICIO 8###
#Función que determina el número de hormigas que existen al cabo de n periodos
#Entradas: n
#Salidas: número de hormigas engendradas (resultado)
#Restricciones: número debe ser un entero positivo

def hormiguitas(n):
    if type(n)!=int or n<0:
        return "El número ingresado debe ser un entero positivo."
    else:
        resultado=15
        for i in range(1,n+1):
            if resultado%2!=0:
                resultado-=1
            resultado/=2
            resultado*=3
        resultado=int(resultado)
        return resultado

###EJERCICIO 9###
#Función que encadena los dígitos del segundo número con el primer número
#Entradas: 2 números: num1, num2
#Salidas: número (resultado de la encadenación)
#Restricciones: num1 y num2 deben ser números enteros mayores o iguales a 0

def contador(num):
    contador=0
    if num==0:
        contador=1
        return contador
    else:
        while num!=0:
            if num<0:
                num=abs(num)
            else:
                num//=10
                contador+=1
        return contador

def numAppend(num1, num2):
    if type(num1)!=int or type(num2)!=int:
        return "Los datos ingresados deben ser números enteros."
    elif num1<0 or num2<0:
        return "Los datos ingresados deben ser mayores a 0."
    else:
        #El algoritmo es similar al ejercicio 17 de la práctica 1
        digitos2=contador(num2)
        numero = num1*10**digitos2 + num2
        return numero

###Función que toma en cuenta todos los números reales
#Entradas: 2 números: num1, num2
#Salidas: número (resultado de la encadenación)
#Restricciones: num1 y num2 deben ser números

###Si num1 es negativo, entonces numero es negativo.
###Si num1 es positivo y num2 es negativo, entonces numero es positivo.
###La función toma en cuenta sólo el signo de num1 para determinar si la salida es positiva o negativa

def contador(num):
    contador=0
    if num==0:
        contador=1
        return contador
    else:
        while num!=0:
            if num<0:
                num=abs(num)
            else:
                num//=10
                contador+=1
        return contador

def decimales(num):
    decimalesNum=0
    while num%1!=0:
        num*=10 #Le quita los decimales al número
        decimalesNum+=1 #Cuenta los decimales del número
    return num, decimalesNum

def numAppend2(num1, num2):
    if (type(num1)!=int and type(num1)!=float) or (type(num2)!=int and type(num2)!=float):
        return "Los datos ingresados deben ser números."
    else:
        numero = 0 #Salida
        decimalesNum1=0
        decimalesNum2=0
        numeroConDecimales=False
        if num2<0: # Para los casos numAppend2(124,-56)
            num2=abs(num2)
        if num1<0: # Para los casos numAppend2(-124,56) o numAppend2(-124,|-56|)
            num2*=-1
        if type(num1)==float:
            tuplaNum1=decimales(num1) #(num, decimalesNum)
            num1=tuplaNum1[0] #num
            decimalesNum1=tuplaNum1[1] #decimalesNum
            numeroConDecimales=True
        if type(num2)==float:
            num2=decimales(num2)[0] #num de (num, decimalesNum); no es necesario contar los decimales porque luego se le cuentan los dígitos al número
            numeroConDecimales=True
        digitos2=contador(num2)
        numero = num1*10**digitos2 + num2
        if numeroConDecimales:
            numero/=(1*10**(decimalesNum1+digitos2)) #Los digitos de num2 quedan en los decimales de num1, si num1 es un número con decimales
        return numero

###EJERCICIO 10###
#Función que retorna un número dividio truncado en cada uno de sus dígitos
#Entradas: dígito (dig) y número (num)
#Salidas: número
#Restricciones: dígito debe ser entero y estar entre 1 y 9, número debe ser entero

##def div(dig, num):
##    if type(dig)!=int

###EJERCICIO 11###
#Función que cuenta los dígitos de un número mayores a 5 y menores o iguales a 5
#Entradas: número
#Salidas: tupla (cantidad-dígitos-mayores-que-5, cantidad-dígitos-menores-o-iguales-que-5):
          # (a, b)
#Restricciones: número debe ser entero

def digitos(numero):
    if type(numero)!=int:
        return "El dato ingresado debe ser un número entero."
    else:
        a=0 #cantidad-dígitos-mayores-que-5
        b=0 #cantidad-dígitos-menores-o-iguales-que-5
        while numero!=0:
            if numero<0:
                numero=abs(numero)
            ultimoDigito=numero%10
            numero//=10
            if ultimoDigito>5:
                a+=1
            else:
                b+=1
        return a,b

###EJERCICIO 13###
#Función que determina la cantidad de números primos que existen entre 2 números
#Entradas: 2 números: a, b
#Salidas: cantidad de números primos: cantidad
#Restricciones: a y b deben ser números enteros mayores o iguales a 0

def numPrimos(a, b):
    if type(a)!=int or type(b)!=int:
        return "Los datos ingresados deben ser números enteros."
    elif a<0 or b<0:
        return "Los datos ingresados deben ser mayores o iguales a 0."
    else:
        cantidad=0
        for i in range(a, b+1):
            if i==0 or i==1:
                cantidad+=0
            elif i==2:
                cantidad+=1
            else:
                esPrimo=True
                for x in range(2, i):
                    if i % x == 0:
                        cantidad+=0
                        esPrimo=False
                if esPrimo:
                    cantidad+=1
        return cantidad


###EJERCICIO 15###
#Función que mueva cada dígito de un número, una posición hacia la derecha,
    #el dígito menos significativo se pone como más significativo
#Entradas: número: num
#Salidas: número: num
#Restricciones: número debe ser un número entero

def contador(num):
    contador=0
    if num==0:
        contador=1
        return contador
    else:
        while num!=0:
            if num<0:
                num=abs(num)
            else:
                num//=10
                contador+=1
        return contador

def shift(num):
    if type(num)!=int:
        return "El dato ingresado debe ser un número entero."
    else:
        numeroNegativo=False
        if num<0:
            num=abs(num)
            numeroNegativo=True
        digitos=contador(num)
        ultimoDigito=num%10
        num//=10
        num+=ultimoDigito*10**(digitos-1)
        if numeroNegativo:
            num*=-1
        return num

###EJERCICIO 17###
#Función que determina si todos los dígitos del primer número están contenidos en el segundo número
#Entradas: 2 números: num1, num2
#Salidas: True o False
#Restricciones: num1 y num2 deben ser números enteros

def esta(dig, num):
    digitoContenido=False
    while num!=0:
        ultimoDigito=num%10 #Último dígito de num2
        num//=10
        if dig==ultimoDigito: #Último dígito de num1 == Último dígito de num2
            digitoContenido=True
    return digitoContenido

def digAB(num1, num2):
    if type(num1)!=int or type(num2)!=int:
        return "Los datos ingresados deben ser números enteros."
    else:
        if num1<0 or num2<0:
            num1=abs(num1)
            num2=abs(num2)

        digitoContenido = True

        while num1!=0:
            ultimoDigito=num1%10 #Último dígito de num1
            num1//=10
            if esta(ultimoDigito, num2)==False:
                digitoContenido=False
        return digitoContenido



###EJERCICIO 19###
#Función que convierte un número decimal en una base
#Entradas: número decimal y una base: num, base
#Salidas: número
#Restricciones: num y base deben ser números enteros mayores a 0

def dectobn(num, base):
    if (type(num)!=int and num<0) or (type(base)!=int and base<0):
        return "Los datos ingresados deben ser números enteros mayores a 0."
    else:
        numero = 0 #Salida
        i=1
        while num/base>=base:
            residuo=num%base
            num//=base
            numero+=residuo*i
            i*=10
        residuo=num%base
        numero+=residuo*i
        i*=10
        numero+=(num//base)*i
        return numero