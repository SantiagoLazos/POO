from Cafe_Back import *

clientes = [
    Cliente(1, "Ana García", "ana@mail.com", 50),
    Cliente(2, "Carlos López", "carlos@mail.com", 120),
    Cliente(3, "María Martínez", "maria@mail.com", 30),
    Cliente(4, "Pedro Sánchez", "pedro@mail.com", 200),
    Cliente(5, "Laura Torres", "laura@mail.com", 75),
    Cliente(6, "Diego Ramírez", "diego@mail.com", 10),
    Cliente(7, "Sofía Herrera", "sofia@mail.com", 90),
    Cliente(8, "Andrés Flores", "andres@mail.com", 150),
    Cliente(9, "Valentina Cruz", "vale@mail.com", 60),
    Cliente(10, "Miguel Ángel", "miguel@mail.com", 0)
]

empleados = [
    Empleado(11, "Roberto Díaz", "roberto@cafe.com", "BARISTA"),
    Empleado(12, "Patricia Ruiz", "patricia@cafe.com", "MESERO"),
    Empleado(13, "Fernando Vega", "fernando@cafe.com", "GERENTE"),
    Empleado(14, "Claudia Mora", "claudia@cafe.com", "BARISTA"),
    Empleado(15, "Javier Reyes", "javier@cafe.com", "MESERO"),
    Empleado(16, "Isabella Núñez", "isabella@cafe.com", "BARISTA"),
    Empleado(17, "Sebastián Gil", "sebas@cafe.com", "MESERO"),
    Empleado(18, "Camila Ortiz", "camila@cafe.com", "GERENTE"),
    Empleado(19, "Tomás Vargas", "tomas@cafe.com", "BARISTA"),
    Empleado(20, "Daniela Ríos", "daniela@cafe.com", "MESERO")
]

pedidos=[]

def buscar_usuario(id, clientes, empleados):
    for cliente in clientes:
        if cliente.id == id:
            return cliente
    for empleado in empleados:
        if empleado.id == id:
            return empleado
    return None

