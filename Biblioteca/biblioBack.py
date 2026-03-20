

class Materiales():
    def __init__ (self, id_Material, titulo, añoPublicación, disponible):
        self.id_Material=id_Material
        self.titulo=titulo
        self.añoPublicación= añoPublicación
        self.disponible=disponible
    
class Libro(Materiales):
    def __init__ (self, autor, genero, id_Material, titulo,añoPublicación, disponible):
        super().__init__(id_Material, titulo, añoPublicación, disponible)
        self.autor=autor
        self.genero=genero

class Revista(Materiales):
    def __init__ (self, edición, periodicidad, id_Material, titulo, añoPublicación, disponible):
        self.edición=edición
        self.periodicidad=periodicidad
        super().__init__(id_Material,titulo, añoPublicación,disponible)

class MaterialDigital(Materiales):
    def __init__(self, id_Material, titulo, añoPublicación, disponible, tipoArchivo, UrlDescarga):
        super().__init__(id_Material,titulo, añoPublicación,disponible)    
        self.tipoArchivo=tipoArchivo
        self.UrlDescarga=UrlDescarga

################Fin de la clase Materiales


class Persona():
    def __init__ (self,nombre, id_persona, rol):
        self.name=nombre
        self.id=id_persona
        self.rol=rol

class Usuario(Persona):
    
    def __init__ (self, limPrestamo, nombre, id_persona, rol):
        super().__init__(nombre,id_persona,rol )
        self.limPrestamo=limPrestamo
        self.LibrosPresta2=[]


class Bibliotecario(Persona):
    def __init__(self,nombre, id_persona, rol ):
        super().__init__(nombre,id_persona,rol )

    def transferirMaterial(self):
        print("Hola estas en la sucursal")


class Sucursal():
    def __init__ (self,sucursal):
        self.sucursal=sucursal
        self.catalogLocal=[]

########################## fin parte 2



class Prestamo():
    def __init__(self, idPrestamo, fechaInicio, fechaDevolucion, usuario, material):
        self.idPrestamo = idPrestamo
        self.fechaInicio = fechaInicio
        self.fechaDevolucion = fechaDevolucion
        self.usuario = usuario
        self.material = material



class Penalizacion():
    def __init__(self, monto, motivo, pagada):
        self.monto = monto
        self.motivo = motivo
        self.pagada = pagada
    
    def calcularMulta(self):
        print("Calculando multa")
    
    def bloquearUsuario(self):
        print("Usuario bloqueado")


class Catalogo():
    def __init__(self, sucursales):
        self.sucursales = sucursales
    
    def buscarPorAutor(self, autor):
        print("Buscando por autor...")
    
    def buscarEnTodasSucursales(self, titulo):
        print("Buscando en todas las sucursales...")


