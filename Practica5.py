#Ejercicio 1
def multi(num1, num2):
    if type(num2)!=int:
        raise Exception("Error: segundo argumento debe ser entero")
    else:
        return multiAux(num1, num2)

def multiAux(num1, num2):
    if num2==0:
        return 0
    else:
        if num2>0:
            return num1+multiAux(num1, num2-1)
        else:
            return -num1+multiAux(num1, num2+1)

#Ejercicio 2

def invertir(num):
    if type(num)!=int:
        raise Exception("Error")
    else:
        if num>=0:
            return invertirAux(num)
        else:
            return -1*invertirAux(abs(num))

def invertirAux(num):
    if num==0:
        return 0
    else:
        digitos=contador(num)-1
        ultimoDigito=num%10
        return ultimoDigito*10**digitos + invertirAux(num//10)

def contador(num):
    if num==0:
        return 1
    else:
        return contadorAux(abs(num))

def contadorAux(num):
    if num==0:
        return 0
    else:
        return 1+contadorAux(num//10)

#Ejercicio 3

def sumaDig(num):
    if type(num)!=int and type(num)!=float:
        raise Exception("Error")
    else:
        if type(num)==float:
            num=decimales(num)
        return sumaDigAux(abs(num))

def sumaDigAux(num):
    if num==0:
        return 0
    else:
        ultimoDigito=num%10
        return int(ultimoDigito+sumaDigAux(num//10))

def decimales(num):
    if num%1==0:
        return num
    else:
        return decimales(num*10)

#Ejercicio 5

cociente = lambda i:i/(i*(i+1))

def sumaCoc(n):
    return sumatoria(n, cociente)

def sumatoria(n, func):
    if type(n)!=int:
        raise Exception("Error")
    else:
        return sumatoriaAux(n,func,1)

def sumatoriaAux(n,func,i):
    if n==i:
        return func(n)
    else:
        return func(i)+sumatoriaAux(n,func,i+1)

#Ejercicio 7

def multdig(num1, num2):
    if type(num1)!=int or type(num2)!=int:
        raise Exception("Error")
    elif contador(num1)!=contador(num2):
        raise Exception("Error")
    else:
        return multdigAux(abs(num1), abs(num2))

def multdigAux(num1, num2):
    if num1==0 and num2==0:
        return 0
    else:
        ultimoDigito1=num1%10
        ultimoDigito2=num2%10
        producto = ultimoDigito1 * ultimoDigito2
        if producto>9:
            producto%=10
        return producto + 10*multdigAux(num1//10, num2//10)

def contador(num):
    if num==0:
        return 1
    else:
        return contadorAux(abs(num))

def contadorAux(num):
    if num==0:
        return 0
    else:
        return 1+contadorAux(num//10)

#Ejercicio 9

def numAppend(num1, num2):
    if type(num1)!=int or type(num2)!=int:
        raise Exception("Error")
    else:
        if num1>=0:
            return numAppendAux(abs(num1), abs(num2))
        else:
            return -1*numAppendAux(abs(num1), abs(num2))
        return

def numAppendAux(num1, num2):
    totalDigitos=contador(num1)+contador(num2)-1
    if num1==0 and num2==0:
        return 0
    else:
        if num1==0:
            exponente=10**(contador(num2)-1)
            primerDigito=num2//exponente
            return primerDigito*10**(totalDigitos-1) + numAppendAux(num1, num2%exponente) #totalDigitos-1 porque cuenta al 0 de num1 como 1 digito
        else:
            exponente=10**(contador(num1)-1)
            primerDigito=num1//exponente
            return primerDigito*10**totalDigitos + numAppendAux(num1%exponente, num2)

def contador(num):
    if num==0:
        return 1
    else:
        return contadorAux(abs(num))

def contadorAux(num):
    if num==0:
        return 0
    else:
        return 1+contadorAux(num//10)

#Ejercicio 11

mayor = lambda n:n>5
menor = lambda n:n<=5

def digitos(numero):
    if type(numero)!=int:
        raise Exception("Error")
    else:
        return digitosAux(abs(numero), mayor), digitosAux(abs(numero), menor)

def digitosAux(numero, func):
    if numero==0:
        return 0
    else:
        ultimoDigito=numero%10
        if func(ultimoDigito):
            return 1 + digitosAux(numero//10, func)
        else:
            return 0 + digitosAux(numero//10, func)

#Ejercicio 13

def numPrimos(a,b):
    if type(a)!=int or type(b)!=int:
        raise Exception("Error")
    else:
        return numPrimosAux(a,b)

def numPrimosAux(a,b):
    if a>b:
        return 0
    else:
        if a==0 or a==1:
            return 0 + numPrimosAux(a+1,b)
        elif a==2:
            return 1 + numPrimosAux(a+1,b)
        else:
            if esPrimo(2, a)==True:
                return 1 + numPrimosAux(a+1,b)
            else:
                return 0 + numPrimosAux(a+1,b)

def esPrimo(num1, num2):
    if num1==num2:
        return True
    else:
        if num2 % num1 == 0:
            return False
        return esPrimo(num1+1, num2)

#Ejercicio 15

def shift(num):
    if type(num)!=int:
        raise Exception("Error")
    else:
        if num>=0:
            return shiftAux(num)
        else:
            return -1*shiftAux(abs(num))

def shiftAux(num):
    if num==0:
        return 0
    else:
        exponente=10**(contador(num)-1)
        ultimoDigito=num%10
        return ultimoDigito*exponente + num%(exponente*10)//10 + shiftAux(num//(exponente*10))

#Ejercicio 17

def digAB(num1, num2):
    if type(num1)!=int or type(num2)!=int:
        raise Exception("Error")
    else:
        return digABAux(abs(num1), abs(num2))

def digABAux(num1, num2):
    if num1==0:
        return True
    else:
        ultimoDigito=num1%10 #Ultimo digito de num1
        if esta(ultimoDigito, num2)==False:
            return False
        return digABAux(num1//10, num2)

def esta(dig, num):
    if num==0:
        return False
    else:
        ultimoDigito=num%10 #Ultimo digito num2
        if dig==ultimoDigito: #Ultimo digito de num1 == Ultimo digito de num2
            return True
        return esta(dig, num//10)

#Ejercicio 19

def dectobn(num, base):
    if (type(num)!=int and num<0) or (type(base)!=int and base<0):
        raise Exception("Error")
    else:
        return dectobnAux(num, base)

def dectobnAux(num, base):
    residuo=num%base
    if num/base<base:
        return residuo + 10*(num//base)
    else:
        return residuo + 10*dectobnAux(num//base, base)