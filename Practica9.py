#1
class Empleado:

    def __init__(self, id_empleado, nombre, salario):
        self.id = id_empleado
        self.nombre = nombre
        self.salario = salario

    def mostrar(self):
        print("Numero de empleado: ", self.id)
        print("Nombre: ", self.nombre)
        print("Salario: ", self.salario)

    def calculoSalario(self, horas):
        salarioxhora = self.salario * horas
        print("Salario: ", salarioxhora)
#2

class Cliente:

    def __init__(self, id_cliente, nombre, saldo):
        self.id = id_cliente
        self.nombre = nombre
        self.saldo = saldo

    def mostrar(self):
        print("Numero de cliente: ", self.id)
        print("Nombre: ", self.nombre)
        print("Saldo: ", self.saldo)

    def registraDoc(self, tipo, monto):
        if tipo=="fa":
            self.saldo += monto
        elif tipo=="re":
            self.saldo -= monto

        if self.saldo<0:
            print("Advertencia: saldo negativo")

        print("Saldo: ", self.saldo)

#3

class Presentacion:

    def __init__(self, nombre, sala, fecha, hora, categoria):
        self.nombre = nombre
        self.sala = sala
        self.fecha = fecha
        self.hora = hora
        self.categoria = categoria

    def mostrar(self):
        print("Numero de la pelicula: ", self.nombre)
        print("Sala: ", self.sala)
        print("Fecha: ", self.fecha)
        print("Hora: ", self.hora)
        print("Categoria ", self.categoria)

    def retornaFecha(self):
        return self.fecha

    def actualizaHora(self, hora):
        self.hora = hora
        print("Hora: ", self.hora)

    def actualizaFecha(self, fecha):
        self.fecha = fecha
        print("Fecha: ", self.fecha)

#4

class Archivo:

    def __init__(self, creador, fechaCreacion):
        self.creador = creador
        self.fechaCreacion = fechaCreacion

    def getCreador(self):
        print("Creador: ", self.creador)

    def getFecha(self):
        print("Fecha: ", self.fechaCreacion)

class ArchivoMusica:

    def __init__(self, creador, fechaCreacion, nombre, genero, duracion, artista):
        Archivo.__init__(self, creador, fechaCreacion)
        self.nombre = nombre
        self.genero = genero
        self.duracion = duracion
        self.artista = artista

    def getNombre(self):
        print("Nombre: ", self.nombre)

    def getGenero(self):
        print("Genero: ", self.genero)

    def getDuracion(self):
        print("Duracion: ", self.duracion)

    def getArtista(self):
        print("Artista: ", self.artista)

class ArchivoWord:

    def __init__(self, creador, fechaCreacion, versionWord, encoding):
        Archivo.__init__(self, creador, fechaCreacion)
        self.versionWord = versionWord
        self.encoding = encoding

    def getVersion(self):
        print("Version: ", self.versionWord)

    def getEncoding(self):
        print("Encoding: ", self.encoding)

class mp3:

    def __init__(self, creador, fechaCreacion, nombre, genero, duracion, artista, rating, bitrate):
        ArchivoMusica.__init__(self, creador, fechaCreacion, nombre, genero, duracion, artista)
        self.rating = rating
        self.bitrate = bitrate

    def getRating(self):
        print("Rating: ", self.rating)

    def getBitrate(self):
        print("Bitrate: ", self.bitrate)

class wma:

    def __init__(self, creador, fechaCreacion, nombre, genero, duracion, artista, licencia, version):
        ArchivoMusica.__init__(self, creador, fechaCreacion, nombre, genero, duracion, artista)
        self.licencia = licencia
        self.version = version

    def getLicencia(self):
        print("Licencia: ", self.licencia)

    def getVersion(self):
        print("Version: ", self.version)

#5

class Persona:

    def __init__(self, nombre, primer_apellido, segundo_apellido, edad):
        self.nombre = nombre
        self.primer_apellido = primer_apellido
        self.segundo_apellido = segundo_apellido
        self.edad = edad

    def imprimir(self):
        print("Nombre: ", self.nombre)
        print("Primer Apellido: ", self.primer_apellido)
        print("Segundo Apellido: ", self.segundo_apellido)
        print("Edad: ", self.edad)

    def getNombre(self):
        return self.nombre

    def getNombreCompleto(self):
        return self.nombre + " " + self.primer_apellido + " " + self.segundo_apellido

    def getEdad(self):
        return self.edad

class Curso:

    def __init__(self, estudiantes):
        self.estudiantes = estudiantes

    def getNombreCompleto(self):
        lista=[]
        i=0
        while i<len(self.estudiantes):
            nombre_completo = self.estudiantes[i].getNombreCompleto()
            lista += [nombre_completo]
            i+=1
        return lista

    #b

    def agregarEst(self, estudiante):
        self.estudiantes+=[estudiante]

    def removeEst(self, nombre):
        i = indice(self.estudiantes, nombre)
        self.estudiantes = self.estudiantes[:i] + self.estudiantes[i+1:]

    #c

    def ordenar(self):
        lista = self.estudiantes
        while estaOrdenada(lista)==False:
            lista = ordenarAux(lista)
        self.estudiantes = lista

# Auxiliar para eliminar estudiantes
def indice(lista, nombre, i=0):
    if lista==[]:
        return -1
    else:
        if lista[0].getNombre() == nombre:
            return i
        else:
            return indice(lista[1:], nombre, i+1)

# Auxiliar para ordenar a los estudiantes por edad
def ordenarAux(lista):
    if lista[1:] == []:
        return lista
    else:
        if lista[0].getEdad() > lista[1].getEdad():
            m = lista[0]
            lista[0] = lista[1]
            lista[1] = m
        return [lista[0]] + ordenarAux(lista[1:])

def estaOrdenada(lista):
    if lista[1:]==[]:
        return True
    elif lista[0].getEdad() <= lista[1].getEdad():
        return estaOrdenada(lista[1:])
    else:
        return False

#6

class Persona2:

    def __init__(self, cedula, nombre, edad):
        self.cedula = cedula
        self.nombre = nombre
        self.edad = edad

    def getInfo(self):
        return {"Nombre":self.nombre, "Cedula":self.cedula, "Edad":self.edad}

    def __str__(self):
        return "Nombre: " + self.nombre + " Cedula:" + str(self.cedula) + " Edad: " + str(self.edad)

class Estudiante(Persona):

    def __init__(self, cedula, nombre, edad, carne, listaDeCursos, listaDeActividadesExtracurriculares):
        Persona2.__init__(self, cedula, nombre, edad)
        self.carne = carne
        self.listaC = listaDeCursos
        self.listaAE = listaDeActividadesExtracurriculares

    #b

    def setCurso(self, curso):
        self.listaC += [curso]

    def setActividad(self, actividad):
        self.listaAE += [actividad]

    def removeCurso(self, curso):
        i = indice(self.listaC, curso)
        self.listaC = self.listaC[:i] + self.listaC[i+1:]

    def removeActividad(self, actividad):
        i = indice(listaAE, actividad)
        self.listaAE = self.listaAE[:i] + self.listaAE[i+1:]

    #c

    def getInfo(self):
        res = Persona2.getInfo(self)
        r = {"Carne":self.carne, "Lista de cursos":self.listaC, "Lista de actividades extracurriculares":self.listaAE}
        res.update(r)
        return res

#7

def multiplos(n):
    lista=[]
    for i in range(2, n//2):
        if n%i == 0:
            lista+=[i]
    return lista


class Carro:

    def __init__(self, marca_carro, modelo_carro, año_carro, km=0):
        self.marca_carro = marca_carro
        self.modelo_carro = modelo_carro
        self.año_carro = año_carro
        self.km = km

    #Getters
    def marca(self):
        return self.marca_carro

    def modelo(self):
        return self.modelo_carro

    def año(self):
        return self.año_carro

    #Setters
    def viaje(self, kms):
        self.km += kms

    #Metodos
    def estado(self):
        if self.km in multiplos(5000):
            return "Revision"
        elif self.km > 100000:
            return "Fuera de Garantia"
        else:
            return "Normal"