import pygame, sys
from pygame.locals import *
pygame.init()
ancho_pantalla=690
alto_pantalla=500
PANTALLA = pygame.display.set_mode((ancho_pantalla, alto_pantalla))
pygame.display.set_caption("Calculadora") #Título del ejecutable

#COLORES
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
CELESTE = (153, 204, 255)
ROJO = (255, 51, 51)
AMARILLO = (255, 255, 102)
VERDE = (153, 255, 204)

#PLANTILLA
PANTALLA.fill(NEGRO)

def resultado(texto1): #Texto de la barra de texto de la calculadora
    if len(texto1) <= 20:
        fuente = pygame.font.Font(None, 70)
        superficie_texto = fuente.render(texto1, 1, NEGRO)
        PANTALLA.blit(superficie_texto,(70, 90))
        pygame.display.flip()
    elif len(texto1) <= 40:
        BARRA() #Borra el cuadro de texto anterior para que se despliegue el texto luego de 20 caracteres, pero no cambia la entrada de datos
        listaTexto=texto1[20:]
        fuente = pygame.font.Font(None, 70)
        superficie_texto = fuente.render(listaTexto, 1, NEGRO)
        PANTALLA.blit(superficie_texto,(70, 90))
        pygame.display.flip()
    elif len(texto1) <= 60:
        BARRA()
        listaTexto=texto1[40:]
        fuente = pygame.font.Font(None, 70)
        superficie_texto = fuente.render(listaTexto, 1, NEGRO)
        PANTALLA.blit(superficie_texto,(70, 90))
        pygame.display.flip()
    elif len(texto1) <= 80: #Límite de 80 caracteres
        BARRA()
        listaTexto=texto1[60:]
        fuente = pygame.font.Font(None, 70)
        superficie_texto = fuente.render(listaTexto, 1, NEGRO)
        PANTALLA.blit(superficie_texto,(70, 90))
        pygame.display.flip()
    else:
        BARRA()
        texto1="Syn Error"
        fuente = pygame.font.Font(None, 70)
        superficie_texto = fuente.render(texto1, 1, NEGRO)
        PANTALLA.blit(superficie_texto,(70, 90))
        pygame.display.flip()

def titulo(texto1, x, y): #Función para crear un texto de tamaño 70
    fuente = pygame.font.Font(None, 70)
    superficie_texto = fuente.render(texto1, 1, NEGRO)
    PANTALLA.blit(superficie_texto,(x, y))
    pygame.display.flip()

def texto(texto1, x, y): #Función para crear un texto de tamaño 35
    fuente = pygame.font.Font(None, 35)
    superficie_texto = fuente.render(texto1, 1, NEGRO)
    PANTALLA.blit(superficie_texto,(x, y))
    pygame.display.flip()

def subtexto(texto1, x, y): #Función para crear un texto de tamaño 20
    fuente = pygame.font.Font(None, 20)
    superficie_texto = fuente.render(texto1, 1, NEGRO)
    PANTALLA.blit(superficie_texto,(x, y))
    pygame.display.flip()

def rectangulo(COLOR, x, y, ancho_rectangulo, alto_rectangulo): #Función para crear un rectángulo
    pygame.draw.rect(PANTALLA, COLOR, (x, y, ancho_rectangulo, alto_rectangulo))

def BARRA(): #Función para crear el rectángulo de la barra de texto
    rectangulo(CELESTE, 50, 50, 590, 100)

#POSICIONES DE LOS BOTONES
ancho = 90 #ancho estándar del botón, con excepciones
alto = 50 #alto estándar del botón, con excepciones
ancho_parentesis = 40 #excepción: PARENTESIS_IZQ, PARENTESIS_DER
#Columnas: posición estándar de los botones en x, con excepciones
columna1 = 50
columna2 = columna1 + 100 #150
columna3 = columna2 + 100 #250
columna4 = columna3 + 100 #350
columna5 = columna4 + 100 #450
columna55 = columna5 + 50 #500, excepción: PARENTESIS_DER
columna6 = columna5 + 100 #550

#Líneas: posición estándar de los botones en y
linea1 = 160
linea2 = linea1 + 60 #220
linea3 = linea2 + 60 #280
linea4 = linea3 + 60 #340
linea5 = linea4 + 60 #400

#Línea 1
def FLECHA_IZQ(COLOR):
    rectangulo(COLOR, columna1, linea1, ancho, alto)
    titulo("«", columna1+ancho/3, linea1)
def FLECHA_DER(COLOR):
    rectangulo(COLOR, columna2, linea1, ancho, alto)
    titulo("»", columna2+ancho/2.7, linea1)
def AC(COLOR):
    rectangulo(COLOR, columna5, linea1, ancho, alto)
    texto("AC", columna5+ancho/3, linea1+alto/3)
def ANS(COLOR):
    rectangulo(COLOR, columna6, linea1, ancho, alto)
    texto("ANS", columna6+ancho/4.5, linea1+alto/3)

#Línea 2
def RAIZ(COLOR):
    rectangulo(COLOR, columna1, linea2, ancho, alto)
    texto("√", columna1+ancho/2.5, linea2+alto/3)
def SIETE(COLOR):
    rectangulo(COLOR, columna2, linea2, ancho, alto)
    texto("7", columna2+ancho/2.2, linea2+alto/3)
def OCHO(COLOR):
    rectangulo(COLOR, columna3, linea2, ancho, alto)
    texto("8", columna3+ancho/2.2, linea2+alto/3)
def NUEVE(COLOR):
    rectangulo(COLOR, columna4, linea2, ancho, alto)
    texto("9", columna4+ancho/2.2, linea2+alto/3)
def PARENTESIS_IZQ(COLOR):
    rectangulo(COLOR, columna5, linea2, ancho_parentesis, alto)
    texto("(", columna5+ancho_parentesis/2.5, linea2+alto/3.5)
def PARENTESIS_DER(COLOR):
    rectangulo(COLOR, columna55, linea2, ancho_parentesis, alto)
    texto(")", columna55+ancho_parentesis/2, linea2+alto/3.5)
def DEL(COLOR):
    rectangulo(COLOR, columna6, linea2, ancho, alto)
    texto("DEL", columna6+ancho/4, linea2+alto/3)

#Línea 3
def LOG(COLOR):
    rectangulo(COLOR, columna1, linea3, ancho, alto)
    texto("log  x", columna1+12, linea3+alto/4)
    subtexto("y", columna1+53, linea3+(alto/4+15))
def CUATRO(COLOR):
    rectangulo(COLOR, columna2, linea3, ancho, alto)
    texto("4", columna2+ancho/2.2, linea3+alto/3)
def CINCO(COLOR):
    rectangulo(COLOR, columna3, linea3, ancho, alto)
    texto("5", columna3+ancho/2.2, linea3+alto/3)
def SEIS(COLOR):
    rectangulo(COLOR, columna4, linea3, ancho, alto)
    texto("6", columna4+ancho/2.2, linea3+alto/3)
def EXPONENCIAL_E(COLOR):
    rectangulo(COLOR, columna5, linea3, ancho, alto)
    texto("e", columna5+ancho/2.2, linea3+alto/3)
    subtexto("x", columna5+(ancho/2.5+20), linea3+(alto/3-8))
def EXPONENCIAL_10(COLOR):
    rectangulo(COLOR, columna6, linea3, ancho, alto)
    texto("10", columna6+ancho/3, linea3+alto/3)
    subtexto("x", columna6+(ancho/3+30), linea3+(alto/3-8))

#Línea 4
def POTENCIA(COLOR):
    rectangulo(COLOR, columna1, linea4, ancho, alto)
    texto("y", columna1+ancho/2.2, linea4+alto/3)
    subtexto("x", columna1+(ancho/2.5+20), linea4+(alto/3-8))
def UNO(COLOR):
    rectangulo(COLOR, columna2, linea4, ancho, alto)
    texto("1", columna2+ancho/2.2, linea4+alto/3)
def DOS(COLOR):
    rectangulo(COLOR, columna3, linea4, ancho, alto)
    texto("2", columna3+ancho/2.2, linea4+alto/3)
def TRES(COLOR):
    rectangulo(COLOR, columna4, linea4, ancho, alto)
    texto("3", columna4+ancho/2.2, linea4+alto/3)
def DIVISION(COLOR):
    rectangulo(COLOR, columna5, linea4, ancho, alto)
    texto("÷", columna5+ancho/2.2, linea4+alto/4)
def MULTIPLICACION(COLOR):
    rectangulo(COLOR, columna6, linea4, ancho, alto)
    texto("x", columna6+ancho/2.2, linea4+alto/4)

#Línea 5
def INVERSO(COLOR):
    rectangulo(COLOR, columna1, linea5, ancho, alto)
    texto("1 / x", columna1+ancho/4.5, linea5+alto/3.5)
def CERO(COLOR):
    rectangulo(COLOR, columna2, linea5, ancho, alto)
    texto("0", columna2+ancho/2.2, linea5+alto/3)
def PUNTO(COLOR):
    rectangulo(COLOR, columna3, linea5, ancho, alto)
    texto(".", columna3+ancho/2.2, linea5+alto/3)
def IGUAL(COLOR):
    rectangulo(COLOR, columna4, linea5, ancho, alto)
    texto("=", columna4+ancho/2.2, linea5+alto/4)
def SUMA(COLOR):
    rectangulo(COLOR, columna5, linea5, ancho, alto)
    texto("+", columna5+ancho/2.2, linea5+alto/4)
def RESTA(COLOR):
    rectangulo(COLOR, columna6, linea5, ancho, alto)
    texto("-", columna6+ancho/2.2, linea5+alto/4)

#OPERACIONES ESPECIALES

#MULTIPLICACIÓN
def multiplicacion10(num):
    resultado=0
    diez=10
    while diez!=0:
        resultado+=num
        diez-=1
    return round(resultado,1)

def decimales(num):
    decimalesNum=0
    while num%1!=0:
        num=multiplicacion10(num) #Le quita los decimales al número
        decimalesNum+=1 #Cuenta los decimales del número
    return num, decimalesNum

def multiplicacion(num1, num2):
    if (type(num1)!=int and type(num1)!=float) or (type(num2)!=int and type(num2)!=float):
        return "Syn Error"
    else:
        resultado=0 #Salida
        decimalesNum1=0
        decimalesNum2=0
        if type(num1)==float:
            tuplaNum1=decimales(num1) #(num, decimalesNum)
            num1=tuplaNum1[0] #num
            decimalesNum1=tuplaNum1[1] #decimalesNum
        if type(num2)==float:
            tuplaNum2=decimales(num2) #(num, decimalesNum)
            num2=tuplaNum2[0] #num
            decimalesNum2=tuplaNum2[1] #decimalesNum
        while num2!=0:
            if num2>=0:
                resultado+=num1
                num2-=1
            else:
                resultado-=num1
                num2+=1
        resultado=division(resultado,(potencia10(decimalesNum1+decimalesNum2))) #resultado/=10**(decimalesNum1+decimalesNum2)
        return resultado

#DIVISIÓN
def multiplicacionUnoNegativo(num):
    resultado=0
    unoNegativo=-1
    while unoNegativo!=0:
        resultado-=num
        unoNegativo+=1
    return resultado

def multiplicacion10(num):
    resultado=0
    diez=10
    while diez!=0:
        resultado+=num
        diez-=1
    return round(resultado,1)

def division(num1, num2):
    if (type(num1)!=int and type(num1)!=float) or (type(num2)!=int and type(num2)!=float):
        return "Syn Error"
    else:
        if num2==0:
            return "Math Error" #No se puede dividir por 0
        else:
            if (num1<0 and num2<0) or (num1>0 and num2>0):
                num1=abs(num1)
                num2=abs(num2)
                resultadoNegativo=False
            else:
                num1=abs(num1)
                num2=abs(num2)
                resultadoNegativo=True
            resultado=0
            while num1>=num2: #num1<num2 no entra
                num1-=num2
                resultado+=1
            if num1!=0: #residuo=num1 o si num1<num2
                t=-1
                i=potencia10(t) #i=0.1
                decimales=0
                while num1!=0 and i>0.00000000001:
                    if num1<num2:
                        num1*=10 #Ejemplo 1/5 = 0.2 o 5/4 = 1.25
                        while num1<num2: #Ejemplo 1/27 = 0.037037037 o 25.1/5 = 5.02
                            num1=multiplicacion10(num1) #num1*=10
                            t-=1
                            i=potencia10(t) #i*=0.1
                    while num1>=num2:
                        num1-=num2
                        decimales+=i
                    resultado+=decimales
                    decimales=0
                    t-=1
                    i=potencia10(t) #i*=0.1
            resultado=round(resultado,10)
            if resultadoNegativo:
                resultado=multiplicacionUnoNegativo(resultado) #resultado*=-1
            return resultado

#POTENCIA
def potencia(numero, potencia):
    if (type(numero)!=float and type(numero)!=int) or (type(potencia)!=float and type(potencia)!=int):
        return "Syn Error"
    else:
        if potencia%1==0:
            resultado=1 #numero**0 = 1
            if potencia!=0:
                potenciaNegativa=False
                numeroNegativo=False
                if potencia<0:
                    potencia=abs(potencia)
                    potenciaNegativa=True
                if numero<0:
                    numero=abs(numero)
                    numeroNegativo=True
                while potencia>0:
                    resultado=multiplicacion(resultado,numero) #resultado*=numero
                    potencia-=1
                if potenciaNegativa:
                    resultado=division(1,resultado)
                if numeroNegativo:
                    resultado=multiplicacionUnoNegativo(resultado)
                return resultado
            else:
                return resultado
        else:
            if potencia==0.5:
                resultado=raiz(numero)
                return resultado
            else:
                return "Syn Error"

#POTENCIA DE EULER
def factorial(i):
    x=1
    if i==0:
        return x
    else:
        while i>0:
            x*=i
            i-=1
    return x

def euler(x):
    if (type(x)!=float and type(x)!=int):
        return "Syn Error"
    else:
        actual=0
        anterior=-100
        i=0
        while(actual-anterior)>=0.00000000001: #Cálculo de euler
            anterior=actual
            actual=actual+(1/factorial(i))
            i+=1
        round(actual, 10)
        resultado=actual**x
        return round(resultado,10)

#POTENCIA DE 10

def multiplicacion10(num):
    resultado=0
    diez=10
    while diez!=0:
        resultado+=num
        diez-=1
    return round(resultado,1)

def potencia10(numero):
    if type(numero)!=int and type(numero)!=float:
        return "Syn Error"
    else:
        resultado=1
        if numero!=0:
            potenciaNegativa=False
            if numero<0:
                numero=abs(numero)
                potenciaNegativa=True
            while numero!=0:
                resultado=multiplicacion10(resultado)
                numero-=1
            if potenciaNegativa:
                resultado=1/resultado
        return resultado

#RAÍZ
def raiz(numero):
    if (type(numero)!=float and type(numero)!=int):
        return "Syn Error"
    else:
        inicio=0
        final=numero
        mitad=0
        while final-inicio>0.00000000001:
            mitad=(inicio+final)/2
            doble=mitad*mitad
            if doble<numero:
                inicio=mitad
            else:
                final=mitad
        return round((inicio+final)/2, 10)

#LOGARITMO
def logaritmo(y, x): #y es la base, log en base y de x
    if (type(y)!=float and type(y)!=int) or (type(x)!=float and type(x)!=int):
        return "Syn Error"
    else:
        try:
            inicio=0
            final=x
            mitad=0
            while final-inicio>0.00000000001:
                mitad=(inicio+final)/2
                if y**mitad < x:
                    inicio=mitad
                else:
                    final=mitad
            return round((inicio+final)/2, 10)
        except OverflowError:
            return logaritmo(2,x)/logaritmo(2,y)

#SUMA

def suma(num1, num2):
    if (type(num1)!=int and type(num1)!=float) or (type(num2)!=int and type(num2)!=float):
        return "Syn Error"
    else:
        resultado=num1+num2
        return resultado

#RESTA

def resta(num1, num2):
    if (type(num1)!=int and type(num1)!=float) or (type(num2)!=int and type(num2)!=float):
        return "Syn Error"
    else:
        resultado=num1-num2
        return resultado

"C A L C U L A D O R A"

BARRA()
texto1=""
resultado(texto1)
respuesta_dada = False #Salida dada (resultado de la operación)
while True: # Bucle del juego
    for event in pygame.event.get():
        #BOTONES
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        resultado_dado = False #Entrada dada
        igual_presionado = False
        #Línea 1
        if columna1+ancho > mouse[0] > columna1 and linea1+alto > mouse[1] > linea1:
            FLECHA_IZQ(VERDE) #Cuando el mouse se posiciona sobre el cuadro
            if click[0] == 1: #Cuando se hace click en el cuadro
                FLECHA_IZQ(NEGRO)
                #No tienen funcionalidad
        elif columna2+ancho > mouse[0] > columna2 and linea1+alto > mouse[1] > linea1:
            FLECHA_DER(VERDE)
            if click[0] == 1:
                FLECHA_DER(NEGRO)
                #No tienen funcionalidad
        elif columna5+ancho > mouse[0] > columna5 and linea1+alto > mouse[1] > linea1:
            AC(VERDE)
            if click[0] == 1:
                AC(NEGRO)
                texto1=""
                resultado(texto1) #Despliega el texto en el cuadro de texto
                print(texto1)
                BARRA() #Borra el cuadro de texto anterior
        elif columna6+ancho > mouse[0] > columna6 and linea1+alto > mouse[1] > linea1:
            ANS(VERDE)
            if click[0] == 1:
                ANS(NEGRO)
                if respuesta_dada: #La respuesta de la operación anterior
                    texto1+=respuesta
                    resultado_dado=True
        #Línea 2
        elif columna1+ancho > mouse[0] > columna1 and linea2+alto > mouse[1] > linea2:
            RAIZ(VERDE)
            if click[0] == 1:
                RAIZ(NEGRO)
                texto1 += "√"
                resultado_dado = True
        elif columna2+ancho > mouse[0] > columna2 and linea2+alto > mouse[1] > linea2:
            SIETE(VERDE)
            if click[0] == 1:
                SIETE(NEGRO)
                texto1 += "7"
                resultado_dado = True
        elif columna3+ancho > mouse[0] > columna3 and linea2+alto > mouse[1] > linea2:
            OCHO(VERDE)
            if click[0] == 1:
                OCHO(NEGRO)
                texto1 += "8"
                resultado_dado = True
        elif columna4+ancho > mouse[0] > columna4 and linea2+alto > mouse[1] > linea2:
            NUEVE(VERDE)
            if click[0] == 1:
                NUEVE(NEGRO)
                texto1 += "9"
                resultado_dado = True
        elif columna5+ancho_parentesis > mouse[0] > columna5 and linea2+alto > mouse[1] > linea2:
            PARENTESIS_IZQ(VERDE)
            if click[0] == 1:
                PARENTESIS_IZQ(NEGRO)
                texto1 += "("
                resultado_dado = True
        elif columna55+ancho_parentesis > mouse[0] > columna55 and linea2+alto > mouse[1] > linea2:
            PARENTESIS_DER(VERDE)
            if click[0] == 1:
                PARENTESIS_DER(NEGRO)
                texto1 += ")"
                resultado_dado = True
        elif columna6+ancho > mouse[0] > columna6 and linea2+alto > mouse[1] > linea2:
            DEL(VERDE)
            if click[0] == 1:
                DEL(NEGRO)
                BARRA()
                texto1 = texto1[0:len(texto1)-1]
                resultado_dado = True
        #Línea 3
        elif columna1+ancho > mouse[0] > columna1 and linea3+alto > mouse[1] > linea3:
            LOG(VERDE)
            if click[0] == 1:
                LOG(NEGRO)
                texto1 += "log("
                resultado_dado = True
        elif columna2+ancho > mouse[0] > columna2 and linea3+alto > mouse[1] > linea3:
            CUATRO(VERDE)
            if click[0] == 1:
                CUATRO(NEGRO)
                texto1 += "4"
                resultado_dado = True
        elif columna3+ancho > mouse[0] > columna3 and linea3+alto > mouse[1] > linea3:
            CINCO(VERDE)
            if click[0] == 1:
                CINCO(NEGRO)
                texto1 += "5"
                resultado_dado = True
        elif columna4+ancho > mouse[0] > columna4 and linea3+alto > mouse[1] > linea3:
            SEIS(VERDE)
            if click[0] == 1:
                SEIS(NEGRO)
                texto1 += "6"
                resultado_dado = True
        elif columna5+ancho > mouse[0] > columna5 and linea3+alto > mouse[1] > linea3:
            EXPONENCIAL_E(VERDE)
            if click[0] == 1:
                EXPONENCIAL_E(NEGRO)
                texto1 += "e^"
                resultado_dado = True
        elif columna6+ancho > mouse[0] > columna6 and linea3+alto > mouse[1] > linea3:
            EXPONENCIAL_10(VERDE)
            if click[0] == 1:
                EXPONENCIAL_10(NEGRO)
                texto1 += "10^"
                resultado_dado = True
        #Línea 4
        elif columna1+ancho > mouse[0] > columna1 and linea4+alto > mouse[1] > linea4:
            POTENCIA(VERDE)
            if click[0] == 1:
                POTENCIA(NEGRO)
                texto1 += "**"
                resultado_dado = True
        elif columna2+ancho > mouse[0] > columna2 and linea4+alto > mouse[1] > linea4:
            UNO(VERDE)
            if click[0] == 1:
                UNO(NEGRO)
                texto1 += "1"
                resultado_dado = True
        elif columna3+ancho > mouse[0] > columna3 and linea4+alto > mouse[1] > linea4:
            DOS(VERDE)
            if click[0] == 1:
                DOS(NEGRO)
                texto1 += "2"
                resultado_dado = True
        elif columna4+ancho > mouse[0] > columna4 and linea4+alto > mouse[1] > linea4:
            TRES(VERDE)
            if click[0] == 1:
                TRES(NEGRO)
                texto1 += "3"
                resultado_dado = True
        elif columna5+ancho > mouse[0] > columna5 and linea4+alto > mouse[1] > linea4:
            DIVISION(VERDE)
            if click[0] == 1:
                DIVISION(NEGRO)
                texto1 += "/"
                resultado_dado = True
        elif columna6+ancho > mouse[0] > columna6 and linea4+alto > mouse[1] > linea4:
            MULTIPLICACION(VERDE)
            if click[0] == 1:
                MULTIPLICACION(NEGRO)
                texto1 += "x"
                resultado_dado = True
        #Línea 5
        elif columna1+ancho > mouse[0] > columna1 and linea5+alto > mouse[1] > linea5:
            INVERSO(VERDE)
            if click[0] == 1:
                INVERSO(NEGRO)
                texto1 += "1/"
                resultado_dado = True
        elif columna2+ancho > mouse[0] > columna2 and linea5+alto > mouse[1] > linea5:
            CERO(VERDE)
            if click[0] == 1:
                CERO(NEGRO)
                texto1 += "0"
                resultado_dado = True
        elif columna3+ancho > mouse[0] > columna3 and linea5+alto > mouse[1] > linea5:
            PUNTO(VERDE)
            if click[0] == 1:
                PUNTO(NEGRO)
                texto1 += "."
                resultado_dado = True
        elif columna4+ancho > mouse[0] > columna4 and linea5+alto > mouse[1] > linea5:
            IGUAL(VERDE)
            if click[0] == 1:
                IGUAL(NEGRO)
                texto1 += "="
                resultado_dado = True
                igual_presionado = True #Para resolver la operación y evaluar texto1
        elif columna5+ancho > mouse[0] > columna5 and linea5+alto > mouse[1] > linea5:
            SUMA(VERDE)
            if click[0] == 1:
                SUMA(NEGRO)
                texto1 += "+"
                resultado_dado = True
        elif columna6+ancho > mouse[0] > columna6 and linea5+alto > mouse[1] > linea5:
            RESTA(VERDE)
            if click[0] == 1:
                RESTA(NEGRO)
                texto1 += "-"
                resultado_dado = True
        else:
            FLECHA_IZQ(BLANCO), FLECHA_DER(BLANCO), AC(AMARILLO), ANS(AMARILLO) #Línea 1
            RAIZ(BLANCO), SIETE(BLANCO), OCHO(BLANCO), NUEVE(BLANCO), PARENTESIS_IZQ(BLANCO), PARENTESIS_DER(BLANCO), DEL(AMARILLO) #Línea 2
            LOG(BLANCO), CUATRO(BLANCO), CINCO(BLANCO), SEIS(BLANCO), EXPONENCIAL_E(BLANCO), EXPONENCIAL_10(BLANCO) #Línea 3
            POTENCIA(BLANCO), UNO(BLANCO), DOS(BLANCO), TRES(BLANCO), DIVISION(BLANCO), MULTIPLICACION(BLANCO) #Línea 4
            INVERSO(BLANCO), CERO(BLANCO), PUNTO(BLANCO), IGUAL(ROJO), SUMA(BLANCO), RESTA(BLANCO) #Línea 5
            #Cuadros de texto sin que ningún botón se presione

        if igual_presionado: #Se resuelve la operación
            try:
                texto2 = texto1 #Para desplegar la operación ingresada más el resultado al final, luego de cambiar texto1
                respuesta = texto1 #Salida
                igual = texto1.find("=") #texto1[:igual]
                texto1 = texto1[:igual] #Borra el igual al final del string
                if texto1.find("+") != -1:
                    signo = texto1.find("+") #Por ejemplo 2+2
                    num1 = float(texto1[:signo]) #2
                    num2 = float(texto1[signo+1:]) #2
                    respuesta = str(suma(num1, num2)) #suma(2, 2)=4, str(4)="4"
                elif texto1.find("-") != -1:
                    signo = texto1.find("-")
                    num1 = float(texto1[:signo])
                    num2 = float(texto1[signo+1:])
                    respuesta = str(resta(num1, num2))
                elif texto1.find("/") != -1: #División e inverso
                    signo = texto1.find("/")
                    num1 = float(texto1[:signo])
                    num2 = float(texto1[signo+1:])
                    respuesta = str(division(num1, num2))
                elif texto1.find("x") != -1:
                    signo = texto1.find("x")
                    num1 = float(texto1[:signo])
                    num2 = float(texto1[signo+1:])
                    respuesta = str(multiplicacion(num1, num2))
                elif texto1.find("log(") != -1:
                    signo = texto1.find("log(")
                    signo_base = texto1.find(")")
                    y = float(texto1[signo+4:signo_base])
                    x = float(texto1[signo_base+1:])
                    respuesta = str(logaritmo(y, x))
                elif texto1.find("√") != -1:
                    signo = texto1.find("√")
                    numero = float(texto1[signo+1:])
                    respuesta = str(raiz(numero))
                elif texto1.find("10^") != -1:
                    signo = texto1.find("10^")
                    numero = float(texto1[signo+3:])
                    respuesta = str(potencia10(numero))
                elif texto1.find("e^") != -1:
                    signo = texto1.find("e^")
                    x = float(texto1[signo+2:])
                    respuesta = str(euler(x))
                elif texto1.find("**") != -1:
                    signo = texto1.find("**")
                    num1 = float(texto1[:signo])
                    num2 = float(texto1[signo+2:])
                    print(num2)
                    respuesta = str(potencia(num1, num2))
                texto1 = texto2 + respuesta #Por ejemplo, "2+2=" + "4"
                BARRA() #Borra el cuadro de texto anterior para dar la respuesta
                respuesta_dada = True #Para el botón de ANS
            except ValueError: #En caso de que se ingrese mal un valor
                texto1="Syn Error" #Cambia texto1
                BARRA() #Borra el cuadro de texto anterior para dar la respuesta
        if resultado_dado:
            resultado(texto1) #Resultado en la pantalla luego de darle el click
            print(texto1)

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()