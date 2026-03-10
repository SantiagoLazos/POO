

class Persona():
    def __init__(self, id, name, mail):
        self.id = id
        self.name = name
        self.mail = mail
    def Login(self):
        print("Bienvenido a la cafeteria")
        correo = input("Ingresa tu correo: ")
        if correo == self.mail:
            print("Bienvenido ", self.name)
        else:
            print("Correo incorrecto, intentalo de nuevo")


    def actualizar_Perfil(self):
        self.name = input("Ingresa tu nuevo nombre: ")
        self.mail = input("Ingresa tu nuevo correo: ")
        print("Perfil actualizado correctamente")

class Cliente(Persona):
    def __init__(self, id, name, mail, puntos):
        super().__init__(id, name, mail)
        self.puntos = puntos
        self.historial_compras = []

    def pedir(self):
        print("¿Qué deseas pedir?")
        pedido = input("Ingresa tu pedido: ")
        self.historial_compras.append(pedido)
        print("Pedido realizado: ", pedido)

    def canjear_Puntos(self):
        print("Tienes ", str(self.puntos), " puntos")
        canjear = input("¿Deseas canjear tus puntos por un descuento? (si/no): ")
        if canjear.lower() == "si":
            if self.puntos >= 100:
                self.puntos -= 100
                print("Has canjeado 100 puntos por un descuento del 10 en tu próxima compra")
            else:
                print("No tienes suficientes puntos para canjear")
        else:
            print("No has canjeado tus puntos")

    def mostrar_Historial(self):
        print("Historial de compras de ", self.name, ":")
        for compra in self.historial_compras:
            print("- ", compra)

class Empleado(Persona):
    def __init__(self, id, name, mail, Rol):
        super().__init__(id, name, mail)
        self.Rol = Rol

    def actualizar_inventario(self):
        print("Inventario actualizado por ", self.name)

    def cambiarEstadoPedido(self, pedido):
        if pedido.estado == "PENDIENTE":
            pedido.estado = "PREPARANDO"
            print("PREPARANDO")
        elif pedido.estado == "PREPARANDO":
            pedido.estado = "Entregado"
            print("Entregado")
        else:
            print("El pedido ya fue entregado")
        

############################################################

class ProductoBase():
    def __init__ (self, id_porducto, nombre, precio):
        self.id_producto = id_porducto
        self.nombre = nombre
        self.precio = precio

class Bebida(ProductoBase):
    def __init__(self, id_producto, nombre, precio, temperatura, modificaciones):
        super().__init__(id_producto, nombre, precio)
        self.temperatura = temperatura
        self.modificaciones = modificaciones

    def agregar_Modificacion(self):
        if self.modificaciones=="NA":
            print("No se ha agregado ninguna modificación a la bebida ", self.nombre)
        else:
            print(f"A la bebida {self.nombre} se le ha agregado la modificación: {self.modificaciones}")
    
    def calcular_Precio(self):
        precio_final = self.precio
        if self.modificaciones != "NA":
            precio_final += 10 #Se le agrega un costo adicional de 5 a la bebida pormodificación
        return precio_final
    
class postre(ProductoBase):
    def __init__(self, id_producto, nombre, precio, vegano, sin_gluten):
        super().__init__(id_producto, nombre, precio)
        self.vegano = vegano
        self.sin_gluten = sin_gluten


#################################################################################

class Pedido():
    def __init__(self, idPedido, estado):
        self.idPedido = idPedido     
        self.productos = []           
        self.estado = estado
        self.total = 0

    def calcular_Total(self):
        total = 0
        for producto in self.productos:  #
            total += producto.precio
        self.total = total
        return self.total

    def validarStock(self, inventario):
        for producto in self.productos:
            if producto.nombre in inventario.ingredientes:
                if inventario.ingredientes[producto.nombre] > 0:
                    print(f"{producto.nombre} disponible en stock")
                else:
                    print(f"{producto.nombre} sin stock")
            else:
                print(f" {producto.nombre} no está registrado en el inventario")

class Inventario():
    def __init__(self):
        self.ingredientes = {
            "cafe": 100,
            "leche": 50,
            "azucar": 200,
            "chocolate": 30,
            "vainilla": 20
        }

    def Reducir_Stock(self, producto):
        if producto.nombre in self.ingredientes:
            if self.ingredientes[producto.nombre] > 0:
                self.ingredientes[producto.nombre] -= 1
                print(f"Stock actualizado: {producto.nombre} ahora tiene {self.ingredientes[producto.nombre]} unidades")
            else:
                print(f"No hay suficiente stock de {producto.nombre} para actualizar")
        else:
            print(f"{producto.nombre} no está registrado en el inventario")

    def notificar_Baja_Stock(self):
        for ingrediente, cantidad in self.ingredientes.items():
            if cantidad < 10:
                print(f"Alerta: El ingrediente {ingrediente} tiene un stock bajo ({cantidad} unidades restantes)")



        