#########EJERCICIO 1#########
#Función que calcula el radio y la circunferencia de un círculo
#Entradas: radio
#Salidas: diccionario de dos elementos: {área, circunferencia}
#Restricciones: radio>0; el radio debe ser un número real.
def circulo(radio):
    if (type(radio)!=float and type(radio)!=int) or radio<=0: #Restricciones
        return "El valor del radio debe ser numérico y debe ser mayor a 0."
    else:
        pi=3.14159265359 #Valor de pi
        area=pi*(radio**2) #Área del círculo
        circunferencia=2*pi*radio #Circunferencia del círculo
        return {"Área":area, "Circunferencia":circunferencia}

#########EJERCICIO 2#########
#Función que retorna un número en letras
#Entradas: número
#Salidas: string
#Restricciones: número entero entre 1 y 5

def numLetras(numero):
    if type(numero)!=int or numero<1 or numero>5:
        return "Error en numero de entrada."
    else:
        diccionario={1:"UNO", 2:"DOS", 3:"TRES", 4:"CUATRO", 5:"CINCO"}
        return diccionario[numero]

#########EJERCICIO 3#########
#Función que calcula el área y volumen de una esfera
#Entradas: radio
#Salidas: diccionario de dos elementos: {área, volumen}
#Restricciones: radio>0; el radio debe ser un número real.

def esfera(radio):
    if (type(radio)!=float and type(radio)!=int) or radio<=0: #Restricciones
        return "El valor del radio debe ser numérico y debe ser mayor a 0."
    else:
        pi=3.14159265359 #Valor de pi
        volumen=(4/3)*pi*(radio**3) #Volumen de la esfera
        area=4*pi*(radio**3) #Área de la esfera
        return {"Área": area, "Volumen": volumen}

#########EJERCICIO 4#########
def foo(op):
    return op/7

##    >>> foo(14)
##    >>> 14/7=2.0
##    2.0
##    >>> foo(20+foo(7))
##    >>>foo(20+(7/7=1.0)
##    >>>foo(21.0)
##    >>>21.0/7=3.0
##    3.0

#########EJERCICIO 5#########
#Función que determina si un año es bisiesto o no
#Entradas: año
#Salidas: True o False
#Restricciones: año debe ser un número entero mayor a 0

def bisiesto(año):
    if type(año)!=int and año<0: #Restricciones
        return "El dato ingresado debe ser un número y debe ser mayor a 0."
    else:
        return (año%4==0 and año%100!=0) or año%400==0 #Devuelve True o False

#########EJERCICIO 6#########
#Función que recibe un monto de dinero y lo reparte en diferentes denominaciones
#Entradas: número
#Salidas: menor cantidad posible de cada denominación (cien, cincuenta, veinte, diez, cinco, uno)
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

def desglose(numero):
    if type(numero)!=int and numero<0:
        return "El número debe ser entero y mayor que 0."
    else:
        digitos=contador(numero)
        cien=0
        cincuenta=0
        veinte=0
        diez=0
        cinco=0
        uno=0
        while digitos!=0:
            if digitos>=3: #centenas a miles
                centenas=numero//(1*10**2)
                numero-=(centenas*(1*10**2))
                cien=centenas #denominación cien
                digitos=2 #pasa al elif
            elif digitos==2:
                decenas=numero//(10)
                numero-=decenas*(10)
                while decenas!=0: #si el numero no tiene un dígito en las decenas, no entra
                    if decenas>5: #decenas<=9
                        cincuenta=1 #denominación cincuenta
                        decenas-=5 #0<=decenas<=4
                    else:
                        if decenas%2==0: #si es par
                            veinte=decenas//2 #denominación veinte
                            decenas=0
                        else:
                            diez=decenas #denominación diez
                            decenas=0
                digitos=1 #pasa al else
            else:
                unidades=numero #unidades<=9
                while unidades!=0:
                    if unidades>5:
                        cinco=1
                        unidades-=5 #0<=unidades<=4
                    else:
                        uno=unidades
                        unidades=0
                digitos=0 #sale del while
        return cien, cincuenta, veinte, diez, cinco, uno

#########EJERCICIO 7#########
#Función que devuelve el mediano de 3 argumentos
#Entradas: 3 argumentos numéricos (x,y,z)
#Salidas: el mediano
#Restricciones: los 3 datos ingresados deben ser numéricos

def mediano(x, y, z):
    if type(x)!=int and type(y)!=int and type(z)!=int: #Restricciones
        return "Se deben ingresar tres argumentos numéricos"
    else:
        lista=[x,y,z]
        lista.sort()
        return lista[1] #Se elige el del medio de la lista ordenada

#########EJERCICIO 8#########
#Función que recibe 3 números y los ordena de mayor a menor
#Entradas: 3 números
#Salidas: 3 números en orden descendente
#Restricciones: 3 números deben ser reales; debe devolver una tupla

def orden(num1,num2,num3):
    if (type(num1)!=int and type(num1)!=float) or (type(num2)!=int and type(num2)!=float) or (type(num3)!=int and type(num3)!=float):
        return "Se deben ingresar 3 números."
    else:
        lista=[num1,num2,num3]
        lista.sort()
        lista.reverse()
        lista=tuple(lista)
        return lista

#########EJERCICIO 9#########
#Función que expresa la capacidad de un disco duro en bytes, conociendo la capacidad en gigabytes
#Entradas: capacidad de un disco duro en gigabytes
#Salidas: capacidad de un disco duro en bytes
#Restricciones: la capacidad debe ser un número real y debe ser un número mayor a 0.

def disco(capacidad):
    if (type(capacidad)!=float and type(capacidad)!=int) or capacidad<0: #restricciones
        return "El dato ingresato debe ser un número y debe ser mayor a 0."
    else:
        capacidad=capacidad*1024*1024*1024
        #megabytes=gigabytes*1024
        #kilobytes=megabytes*1024
        #capacidad=kilobytes*1024
        return capacidad

#########EJERCICIO 10#########

def misterio(a,c):
    b=lambda x:a**2
    d=b(c)+10
    return d

##    >>> misterio(2,8)
##    >>> x=8:2**2=4
##    >>>d=4+10=14
##    14
##    >>> misterio(0,4)
##    >>> x=4:0**2=0
##    >>> d=0+10=10
##    10

#########EJERCICIO 11#########
#Función que convierte una cantidad de metros en centímetros, pulgadas, pies o yardas según un indicador de conersión
#Entradas: cantidad de metros y un indicador de conversión
#Salidas: metros convertidos
#Restricciones: cantidad de metros debe ser un número real;
            #indicador de conversión debe ser un número entero entre 1 y 4

def convertir(metros, indicador):
    if (type(metros)!=float and type(metros)!=int) or (type(indicador)!=int or indicador<1 or indicador>4): #Restricciones
        return "La cantidad de metros debe ser un número real. El indicador de conversión debe ser un número entero entre 1 y 4."
    else:
        centimetros=metros*100
        pulgadas=centimetros*2.54
        pies=pulgadas*12
        yardas=pies*3
        if indicador==1:
            return centimetros
        elif indicador==2:
            return pulgadas
        elif indicador==3:
            return pies
        else:
            return yardas

#########EJERCICIO 12#########
#Función que calcula el salario de un trabajador según horas trabajadas y tarifa por hora
#Entradas: cantidad de horas trabajadas (horas) y la tarifa (tarifa)
#Salidas: salario
#Restricciones: horas debe ser un número entero mayor o igual a 0; tarifa debe ser un número entero mayor o igual a 0

def calcSalario(horas, tarifa):
    if (type(horas)!=int or type(tarifa)!=int) or (horas<0 or tarifa<0):
        return "Los datos ingresados deben ser enteros y mayores o iguales a 0."
    else:
        salario=0
        while horas>40: #Si horas<=40, no entra en el while
            salario+=(tarifa*0.5)
            horas-=1
        salario=int(salario)
        while horas>0:
            salario+=tarifa
            horas-=1
        return salario

#########EJERCICIO 13#########
#Función que retorna el salario aumentado y el valor del aumento según el salario actual de un jugador
#Entradas: salario actual de un jugador
#Salidas: tupla de dos elementos: (salario aumentado, valor del aumento)
#Restricciones: el salario actual debe ser un número entero mayor que 0

def aumento(salario):
    if type(salario)!=int or salario<=0: #Restricciones
        return "El salario actual debe ser un número entero y debe ser mayor que 0."
    else:
        if 0<salario<=1000000:
            salario=int(salario+(salario*0.20)) #Se debe devolver un número entero
            return salario, "20%"
        elif 1000001<=salario<=1500000:
            salario=int(salario+(salario*0.10))
            return salario, "10%"
        elif 1500001<=salario<=2000000:
            salario=int(salario+(salario*0.05))
            return salario, "5%"
        else:
            return salario, "No hay aumento."

#########EJERCICIO 14#########
#Función que recibe la hora actual del día en 3 argumentos
#Entradas: horas, minutos, segundos
#Salidas: minutos que faltan para terminar un día
#Restricciones: los 3 argumentos deben ser números reales; 0<=horas<24
        # 0<=minutos<60; 0<=segundos<59

def faltante(horas, minutos, segundos):
    if type(horas)!=int or type(minutos)!=int or type(segundos)!=int or horas<0 or horas>23 or minutos<0 or minutos>59 or segundos<0 or segundos>59:
        return "Los 3 argumentos ingresados deben ser números reales. Horas debe pertener al intervalo [0,24[. Minutos debe pertener al intervalo [0,60[. Segundos debe pertenecer al intervalo [0,60[."
    else:


#########EJERCICIO 15#########
#Función que indica si un número de 5 dígitos es un palíndromo o no
#Entradas: número
#Salidas: True o False
#Restricciones: número entero y de 5 dígitos

#Solución con strings
def palindromo(numero):
    if type(numero)!=int: #Restricciones
        return "Se debe ingresar un número entero."
    else:
        numero=abs(numero) #Para que el número no sea negativo y no se cuente el - al usar la función len()
        numero=str(numero) #Para poder usar la función len()
        if len(numero)!=5: #Restricciones
            return "El número debe tener 5 dígitos."
        else:
            return numero==numero[::-1] #Devuelve True o False

#Solución aritmética
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

def palindromo2(numero):
    if type(numero)!=int: #Restricciones
        return "Se debe ingresar un número entero."
    else:
        digitos=contador(numero) #La cantidad de dígitos que tiene el número
        if digitos!=5: #Restricciones
            return "El número debe tener 5 dígitos."
        else:
            num=numero #numero queda igual para comparar después y num va a cambiar
            numeroInverso=0 #Va a ser el número al revés
            numeroNegativo=False
            while num!=0:
                if num<0:
                    num=abs(num) #Tiene que ser positivo para que num%10 dé el último dígito del número
                    numeroNegativo=True #Para luego multiplicar por -1
                else:
                    ultimoDigito=num%10
                    numeroInverso+=ultimoDigito*10**(digitos-1)
                    digitos-=1
                    num//=10
            if numeroNegativo:
                numeroInverso*=-1 #Para que el número inverso sea negativo, al igual que el ingresado
            return numero==numeroInverso #Devuelve True o False

#########EJERCICIO 16#########
#Función que
#Entradas:
#Salidas:
#Restricciones:

#########EJERCICIO 17#########
#Función que adjunta un dígito a la derecha de un número entero
#Entradas: dos argumentos (numero entero, digito)
#Salidas: un numero que adjunte numero entero con el digito
#Restricciones: los dos argumentos deben ser números enteros
                #digito debe ser mayor o igual a 0 y menor que 10

def adjunto(num, dig):
    if type(num)!=int or (type(dig)!=int or (dig<0 or dig>9)): #Restricciones
        return "Los datos ingresados deben ser enteros y el digito debe ser mayor o igual a 0 y menor que 10."
    else:
        numero=num*10+dig
        return numero

#########EJERCICIO 18#########
#Función que
#Entradas:
#Salidas:
#Restricciones:

#########EJERCICIO 19#########
#Función que determina cuánto dinero se acumulará en una cuenta en el banco
#Entradas: cantidad de dinero depositado inicialmente (P), porcentaje de interés compuesto aplicado (i), años (n)
#Salidas:futura cantidad de dinero (F)
#Restricciones: P y n deben ser un número entero mayor a 0
                # i debe ser un número real entre 0 y 1
                # F debe ser un número entero

def interesCompuesto(P, i , n):
    if (type(P)!=int or P<0) or (type(n)!=int or n<0) or ((type(i)!=float and type(i)!=int) or (i<0 or i>1)): #Restricciones
        return "La cantidad de dinero y los años deben ser números enteros mayores a 0. El porcentaje de interés aplicado debe ser un número real entre 0 y 1."
    else:
        F=int(P*(1+i)**n) #Fórmula para calcular la futura cantidad de dinero
        return F #Futura cantidad de dinero

#########EJERCICIO 20#########
#Función que
#Entradas:
#Salidas:
#Restricciones:

#########EJERCICIO 21#########
#Función que invierte un número de 5 cifras
#Entradas: número cualquiera de 5 cifras
#Salidas: número con cifras invertidas
#Restricciones: número ingresado debe ser un número entero de 5 cifras

#Solución con strings
def invertir(numero):
    if type(numero)!=int: #Restricciones
        return "Se debe ingresar un número entero."
    else:
        numeroNegativo=False
        if numero<0:
            numero=abs(numero) #Para que el número no sea negativo y no se cuente el - al usar la función len()
            numeroNegativo=True #Para luego multiplicar por -1
        numero=str(numero) #Para poder usar la función len()
        if len(numero)!=5: #Restricciones
            return "El número debe tener 5 dígitos."
        else:
            numero=numero[::-1]
            numero=int(numero) #El resultado debe ser un número entero, no un string
            if numeroNegativo:
                numero*=-1 #Para que el número inverso sea negativo, al igual que el ingresado
            return numero #Número con cifras invertidas

#Solución aritmética
def contador(numero): #Contador del ejercicio 15
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

def invertir2(numero):
    if type(numero)!=int: #Restricciones
        return "Se debe ingresar un número entero."
    else:
        digitos=contador(numero) #La cantidad de dígitos que tiene el número
        if digitos!=5: #Restricciones
            return "El número debe tener 5 dígitos."
        else:
            numeroInverso=0 #Va a ser el número al revés
            numeroNegativo=False
            while numero!=0:
                if numero<0:
                    numero=abs(numero) #Tiene que ser positivo para que numero%10 dé el último dígito del número
                    numeroNegativo=True #Para luego multiplicar por -1
                else:
                    ultimoDigito=numero%10
                    numeroInverso+=ultimoDigito*10**(digitos-1)
                    digitos-=1
                    numero//=10
            if numeroNegativo:
                numeroInverso*=-1 #Para que el número inverso sea negativo, al igual que el ingresado
            return numeroInverso #Número con cifras invertidas