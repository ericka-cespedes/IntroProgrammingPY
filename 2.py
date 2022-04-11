def digitos(dig, num):
    if (type(dig)!=int or dig<0 or dig>9) or type(num)!=int:
        return "Los datos ingresados deben ser números enteros. El dígito debe estar entre 0 y 9."
    else:
        A=0
        B=0
        i=1
        t=1
        while num!=0:
            if num<0:
                num=abs(num)
            else:
                ultimoDigito=num%10
                num//=10
                if ultimoDigito>dig:
                    A=A+ultimoDigito*i
                    i=i*10
                else:
                    B=B+ultimoDigito*t
                    t=t*10
        return A,B
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

def multdig(num1,num2):
    if type(num1)!=int or type(num2)!=int:
        return "Datos invalidos."
    else:
        digitos1=contador(num1)
        digitos2=contador(num2)
        if digitos1!=digitos2:
            return "Datos invalidos."
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