###proyecto final
import datetime

personas=[]
libros=[]
LibrosEnPrestamo=[]

class Libro:
    def __init__ (self,idLibro,nombre,genero,autor):
        self.idLibro=idLibro
        self.nombre=nombre
        self.genero=genero
        self.autor=autor
        self.existencias=2

    def imprimirLibro(self):
        print("El ID del libro es: "+self.idLibro+" con el nombre: "+self.nombre+" su genero es: "+self.genero+" ,su Autor es: "+self.autor+" y existen: "+str(self.existencias))
    
    def imprimirNomLibro(self):
        print("El nombre del libro en prestamo es: "+self.nombre)
class LibroPrestado:
    def __init__(self,libro,usuario):
        self.libro=libro
        self.usuario=usuario
        self.fechadevolución=datetime.datetime.now()

    def imprimirLibroPrestado(self):
        print("El libro "+self.libro.nombre+" esta prestado a "+self.usuario.nombre+" y la fecha de devolución es: "+str(self.fechadevolución))  
class usuario:
    def __init__(self,codigo,nombre,correo):
        self.codigo=codigo
        self.nombre=nombre
        self.correo=correo
    
    def imprimirUsuario(self):
        print("el Id del usuario es: "+self.codigo+" con nombre: "+self.nombre+" correo electronico del usuario: "+self.correo)

def CargarPersonas():
    usuario1 = usuario("01","Aaron Castillo Marin","acastillo@uni.cr")
    personas.append(usuario1)
    usuario2 = usuario("02","Bryan Briones Garita","bbriones@uni.cr")
    personas.append(usuario2)
    usuario3 = usuario("03","Carmen Alpizar Trigueros","calpizar@uni.cr")
    personas.append(usuario3)
    usuario4 = usuario("04","Carolina Benavides Venegas","cbenavides@uni.cr")
    personas.append(usuario4)
    usuario5 = usuario("05","Christian Camacho Cerdas","ccamacho@uni.cr")
    personas.append(usuario5)
    usuario6 = usuario("06","Cliffort Bamert Soto","cbamert@uni.cr")
    personas.append(usuario6)
    usuario7 = usuario("07","Daniel Samper Villareal","dsamper@uni.cr")
    personas.append(usuario7)
    usuario8 = usuario("08","Eddy Alvarez Zapata","ealvarez@uni.cr")
    personas.append(usuario8)
    usuario9 = usuario("09","Enrique Briceno Martinez","ebriceno@uni.cr")
    personas.append(usuario9)
    usuario10 = usuario("10","Jesus Bavaresco Rodríguez","jbavaresco@uni.cr")
    personas.append(usuario10)
    usuario11 = usuario("11","Jose Carvajal Molina","jcarvajal@uni.cr")
    personas.append(usuario11)
    usuario12 = usuario("12","Jose Ignacio Acuna Sanchez","jacuna@uni.cr")
    personas.append(usuario12)
    usuario13 = usuario("13","Josue Somarribas Aragón","jsomarribas@uni.cr")
    personas.append(usuario13)
    usuario14 = usuario("14","Luis Fernando Ramirez Gutirrez","lramirez@uni.cr")
    personas.append(usuario14)
    usuario15 = usuario("15","Mariano Castro Aguilar","mcastro@uni.cr")
    personas.append(usuario15)
    usuario16 = usuario("16","Mariela Sanchez Fallas ","msanchez@uni.cr")
    personas.append(usuario16)
    usuario17 = usuario("17","Mario Castillo Blanco ","mcastillo@uni.cr")
    personas.append(usuario17)
    usuario18 = usuario("18","Rebecca Campos Barrientos","rcampos@uni.cr")
    personas.append(usuario18)
    usuario19 = usuario("19","Rosemary Ballestero Barquero","rballestero@uni.cr")
    personas.append(usuario19)
    usuario20 = usuario("20","Sebastián Barranco Vega","sbarranco@uni.cr")
    personas.append(usuario20)
    usuario21 = usuario("21","Valery Campos Vasquez","vcampos@uni.cr")
    personas.append(usuario21)
    usuario22 = usuario("22","Wilmer Blandon Cabrera","wblandon@uni.cr")
    personas.append(usuario22)

def cargarLibros():
    libro1=Libro("01","Cien Años de Soledad","novela","Gabriel Garcia Marquez")
    libros.append(libro1)
    libro2=Libro("02","Don Quijote de la Mancha","Aburrido","Miguel de Cervantes")
    libros.append(libro2)
    libro3=Libro("03","Hamlet","teatro","William Shakespeare")
    libros.append(libro3)
    libro4=Libro("04","El Principito","Fantasia","Antoine de Saint Exupery")
    libros.append(libro4)
    libro5=Libro("05","Orgullo y Prejuicio","Romantico","Jane Austen")
    libros.append(libro5)
    libro6=Libro("06","1984","Misterio","George Orwell")
    libros.append(libro6)
    libro7=Libro("07","La Odisea","Poesía","Homero")
    libros.append(libro7)
    libro8=Libro("08","El retrato de Dorian Grey","Fantasía","Oscar Wilde")
    libros.append(libro8)
    libro9=Libro("09","Lo que el viento se llevó","Drama","Margaret Mitchell")
    libros.append(libro9)
    libro10=Libro("10","Moby-Dick","Fantasía","Herman Melville")
    libros.append(libro10)
    
def verPersonas ():
    for usuario in personas:
        usuario.imprimirUsuario()

def buscarLibroxNombre(LibroaBuscar):
    for libro in libros:
        if(LibroaBuscar==libro.nombre):
            return libro
    return None

def buscaPersonaxNombre(nombreaBuscar):
    for usuario in personas:
        if(nombreaBuscar==usuario.nombre):
            return usuario
    return None

def buscarPersonas():
    nombreBuscar = input("Digite el nombre del usuario que desea buscar: ")
    usuario=buscaPersonaxNombre(nombreBuscar)
    if usuario==None:
        return "El usuario no se encuentra en la lista"
    else:
        return "el usuario tiene por nombre "+usuario.nombre+" su ID o Código es "+usuario.codigo+" y su correo es: "+usuario.correo

def buscarLibro():
    libBuscar = input("Digite el nombre,genero o autor del libro que desea ver: ")
    for libro in libros:
        if(libro.nombre==libBuscar):
            return "El libro es: "+libro.nombre+" Su ID es:"+libro.idLibro
        if(libro.genero==libBuscar):
            return "El libro es: "+libro.nombre+" Su ID es:"+libro.idLibro
        if(libro.autor==libBuscar):
           return "El libro es: "+libro.nombre+" Su ID es:"+libro.idLibro
    return ("El libro no se encuentra en la lista")

def Verfichapersona():
    idBuscar = input("Digite el ID del usuario que desea ver: ")
    for usuario in personas:
        if(usuario.codigo == idBuscar):
            return "El usuario "+usuario.nombre+" tiene el id "+usuario.codigo+" y su correo electronico es: "+usuario.correo
    return("El usuario no se encuentra en la lista")

def verFichaLibro():
    libBuscar = input("Digite el ID del libro que desea buscar: ")
    for libro in libros:
        if(libro.idLibro==libBuscar):
            return "El libro es: "+libro.nombre+" El ID del libro es: "+libro.idLibro+" su genero es: "+libro.genero+" y su Autor es: "+libro.autor 
    return ("El libro no se encuentra en la lista")

def verLibros():
    for libro in libros:
        libro.imprimirLibro()

def restarExitenciasLibro(libroRestar):
    for libro in libros:
        if(libro==libroRestar):
            libro.existencias=libro.existencias-1

def aumentarExitenciasLibro(libroSumar):
    for libro in libros:
        if(libro.nombre==libroSumar):
            libro.existencias=libro.existencias+1

def prestarLibro():
    nombre=input(" Digite el nombre del usuario que solicta el libro: ")
    usuario=buscaPersonaxNombre(nombre)
    if usuario==None:
        return "El usuario no esta en la lista"
    else:
        libroquequiere=input("Indique el nombre del libro que desea el usuario: ")
        libro=buscarLibroxNombre(libroquequiere)
        if libro == None or libro.existencias==0:
            return "el libro no esta disponible"
        else:
            librop=LibroPrestado(libro,usuario)
            restarExitenciasLibro(libro)
            LibrosEnPrestamo.append(librop)
            return "se realizo la entrega del libro"
        
def BuscarPrestamoxLibroyUsuario(nombrelibro,nombreusuario):
    for libro in LibrosEnPrestamo:
        if libro.libro.nombre==nombrelibro and libro.usuario.nombre==nombreusuario:
            return libro 
    return None

def devolverLibro():
    libroaDevolver= input("cual es el libro que desea devolver: ")
    usuarioQueDevuelve= input("cual es el nombre del usuario que devuelve el libro: ")
    libroPrestado=BuscarPrestamoxLibroyUsuario(libroaDevolver,usuarioQueDevuelve)
    if libroPrestado==None:
        return "El libro no se encuentra en prestamo a ese usuario"
    else:
        LibrosEnPrestamo.remove(libroPrestado)
        aumentarExitenciasLibro(libroPrestado.libro.nombre)
        return "Devolución exitosa"

def verLibrosPrestados():
    print("Seleccione a para imprimir listado completo, b para imprimir lista por libro o c para imprimir lista por usuario: ")
    decision=input()
    if decision == "a":
        for LibroPrestado in LibrosEnPrestamo:
            LibroPrestado.imprimirLibroPrestado()
    if decision == "b":
        nomLibro=input("Cual es el nombre del libro: ")
        for libroPrestado in LibrosEnPrestamo:
            if libroPrestado.libro.nombre==nomLibro:
                libroPrestado.imprimirLibroPrestado()
    if decision == "c":
        nomUsuario=input("Cual es el nombre del usuario: ")
        for libroPrestado in LibrosEnPrestamo:
            if libroPrestado.usuario.nombre==nomUsuario:
                libroPrestado.imprimirLibroPrestado()

        
opcion = "z"
CargarPersonas()
cargarLibros()
while opcion != "j":
    print("Seleccione una opción del menu","a,b,c,d,e,f,g,h,i,j")
    print("a.Ver lista de Personas: ")
    print("b.Buscar persona: ")
    print("c.Ver ficha de persona: ")
    print("d.Ver lista de libros: ")
    print("e.Buscar libro: ")
    print("f.Ver ficha tecnica de libro: ")
    print("g.Prestar libro: ")
    print("h.Devolver libro: ")
    print("i.Ver libros prestados: ")
    print("j.salir del programa")
    opcion=(input("indique una opción: "))
    if opcion == "a":
        verPersonas()
    if opcion == "b":
        print(buscarPersonas())
    if opcion == "c":
        print(Verfichapersona())
    if opcion == "d":
        verLibros()
    if opcion == "e":
        print(buscarLibro())
    if opcion == "f":
        print(verFichaLibro())
    if opcion == "g":
        print(prestarLibro())
    if opcion == "h":
        print(devolverLibro())
    if opcion == "i":
        verLibrosPrestados()
    if opcion == "j":
        print("Fin del Programa.... GRACIAS....")
    else: 
        print("Ingrese una opción del Menú")