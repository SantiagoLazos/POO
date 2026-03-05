from datetime import date
from Cine import Usuario, Empleado, Administrador, Sala, Comida, Pelicula, Funcion, Promocion, Reserva #Resivar el nombre del archivo y juntar ambos enla misma carpeta
#jalo las clases

#funcion inicial que muestra ek menu
def menu():


    while True:
        print("========================================")
        print("        CINE - SISTEMA DE RESERVAS      ")
        print("========================================")
        print("  1. Ver usuarios")
        print("  2. Ver empleados")
        print("  3. Ver salas")
        print("  4. Ver zonas de comida")
        print("  5. Ver peliculas")
        print("  6. Ver funciones del dia")
        print("  7. Ver promociones")
        print("  8. Hacer una reserva")
        print("  9. Panel de empleado (admin)")
        print("  0. Salir")
        print("========================================")

        opcion = input("Selecciona una opcion: ")


        if opcion == "1":
            mostrar_usuarios()
        
        elif opcion == "2":
            mostrar_empleados()
        elif opcion == "3":
            mostrar_salas()
        
        elif opcion == "4":
            mostrar_zonas()
        elif opcion == "5":
            mostrar_peliculas()
        elif opcion == "6":
            mostrar_funciones()
        
        elif opcion == "7":
            mostrar_promociones()
        elif opcion == "8":
            hacer_reserva()
        elif opcion == "9":
            panel_empleado()
        elif opcion == "0":
            print("Saliendo del sistema...")
            break
        else:
            print("Opcion no valida, intenta de nuevo")



# 19 usuarios
u1 = Usuario("Carlos Mendoza", 1, "carlos@mail.com", "5550001", 500, 150)
u2 = Usuario("Ana Garcia", 2, "ana@mail.com", "5550002", 300, 60)
u3 = Usuario("Luis Torres", 3, "luis@mail.com", "5550003", 800, 200)
u4 = Usuario("Maria Lopez", 4, "maria@mail.com", "5550004", 150, 20)
u5 = Usuario("Pedro Ramirez", 5, "pedro@mail.com", "5550005", 600, 80)
u6 = Usuario("Sofia Hernandez", 6, "sofia@mail.com", "5550006", 200, 40)
u7 = Usuario("Diego Castro", 7, "diego@mail.com", "5550007", 450, 110)
u8 = Usuario("Valeria Flores", 8, "valeria@mail.com", "5550008", 350, 90)
u9 = Usuario("Andres Morales", 9, "andres@mail.com", "5550009", 700, 175)
u10 = Usuario("Camila Reyes", 10, "camila@mail.com", "5550010", 250, 30)

usuarios = [u1, u2, u3, u4, u5, u6, u7, u8, u9, u10]

# 10 empleados
e1 = Administrador("Roberto Silva", 11, "rsilva@cine.com", "5551001", "admin", "control total")
e2 = Empleado("Patricia Vega", 12, "pvega@cine.com", "5551002", "taquillero")
e3 = Empleado("Miguel Angel", 13, "mangel@cine.com", "5551003", "limpieza")
e4 = Empleado("Laura Ortiz", 14, "lortiz@cine.com", "5551004", "taquillero")
e5 = Administrador("Fernando Ruiz", 15, "fruiz@cine.com", "5551005", "admin", "gestion funciones")
e6 = Empleado("Daniela Cruz", 16, "dcruz@cine.com", "5551006", "limpieza")
e7 = Empleado("Jorge Pena", 17, "jpena@cine.com", "5551007", "taquillero")
e8 = Administrador("Alejandra Rios", 18, "arios@cine.com", "5551008", "admin", "control total")
e9 = Empleado("Hector Vargas", 19, "hvargas@cine.com", "5551009", "limpieza")
e10 = Empleado("Natalia Guzman", 20, "nguzman@cine.com", "5551010", "taquillero")

empleados = [e1, e2, e3, e4, e5, e6, e7, e8, e9, e10]

# 10 salas
s1 = Sala("Sala 1", "2D", 80, False)
s2 = Sala("Sala 2", "3D", 60, False)
s3 = Sala("Sala 3", "IMAX", 40, False)
s4 = Sala("Sala 4", "2D", 100, False)
s5 = Sala("Sala 5", "3D", 50, True)
s6 = Sala("Sala 6", "IMAX", 35, True)
s7 = Sala("Sala 7", "2D", 90, False)
s8 = Sala("Sala 8", "3D", 55, False)
s9 = Sala("Sala 9", "2D", 70, True)
s10 = Sala("Sala 10", "3D", 45, False)

salas = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10]

c1 = Comida("Lobby Norte", 50, ["Palomitas", "Refresco"])
c2 = Comida("Lobby Sur", 40, ["Palomitas", "Nachos"])
c3 = Comida("Snack Bar 1", 30, ["Hot Dog", "Refresco"])
c4 = Comida("Snack Bar 2", 60, ["Palomitas", "Agua"])
c5 = Comida("Cafeteria", 25, ["Cafe", "Pastel"])
c6 = Comida("Kiosco 1", 45, ["Dulces", "Papas"])
c7 = Comida("Kiosco 2", 35, ["Palomitas", "Refresco"])
c8 = Comida("Bar VIP", 20, ["Vino", "Botanas"])
c9 = Comida("Mini Market", 55, ["Agua", "Jugo"])
c10 = Comida("Dulceria", 70, ["Gomitas", "Chocolate"])

zonas = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]

#    10 peliculas
p1 = Pelicula("Dune: Part Two", 155, "Ciencia Ficcion", "B")
p2 = Pelicula("Avengers: Secret Wars", 150, "Accion", "B")
p3 = Pelicula("Inside Out 3", 95, "Animacion", "A")
p4 = Pelicula("Oppenheimer 2", 180, "Drama", "C")
p5 = Pelicula("Fast and Furious 11", 130, "Accion", "B")
p6 = Pelicula("Moana 3", 90, "Animacion", "A")
p7 = Pelicula("Mission Impossible 8", 145, "Thriller", "B")
p8 = Pelicula("Joker 2", 138, "Drama", "C")
p9 = Pelicula("The Batman 2", 155, "Accion", "B")
p10 = Pelicula("Encanto 2", 88, "Animacion", "A")

peliculas = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]

# 10 funciones
f1 = Funcion(p1, s3, "10:00", 150.0)
f2 = Funcion(p2, s2, "12:30", 120.0)
f3 = Funcion(p3, s1, "14:00", 90.0)
f4 = Funcion(p4, s6, "16:00", 160.0)
f5 = Funcion(p5, s4, "18:30", 110.0)
f6 = Funcion(p6, s5, "20:00", 130.0)
f7 = Funcion(p7, s8, "21:30", 140.0)
f8 = Funcion(p8, s7, "22:00", 125.0)
f9 = Funcion(p9, s10, "17:00", 135.0)
f10 = Funcion(p10, s9, "11:00", 95.0)

funciones = [f1, f2, f3, f4, f5, f6, f7, f8, f9, f10]

# 10 promociones
pr1 = Promocion("PROMO10", "10 descuento general", 10, date(2026, 12, 31))
pr2 = Promocion("PROMO20", "20 descuento estudiante", 20, date(2026, 12, 31))
pr3 = Promocion("PROMO15", "15% miercoles de cine", 15, date(2026, 12, 31))
pr4 = Promocion("PROMO30", "30 black friday", 30, date(2026, 11, 30))
pr5 = Promocion("PROMO25", "25 cumpleanos", 25, date(2026, 12, 31))
pr6 = Promocion("PROMO5", "5% tarjeta de credito", 5, date(2026, 12, 31))
pr7 = Promocion("PROMO50", "50 dia del nino", 50, date(2026, 4, 30))
pr8 = Promocion("PROMO VIP", "35 cliente vip", 35, date(2026, 12, 31))
pr9 = Promocion("PROMO12", "12combo pareja", 12, date(2026, 12, 31))
pr10 = Promocion("PROMOLD", "40% promo vencida", 40, date(2025, 1, 1))

promociones = [pr1, pr2, pr3, pr4, pr5, pr6, pr7, pr8, pr9, pr10]


#Menu

# defino todas las funciones d mi programa

def mostrar_usuarios():
    print("REGISTRO DE 10 USUARIOS")
    for i in usuarios:
        i.login()
        i.promociones()
        print()

def mostrar_empleados():
    print("REGISTRO DE 10 EMPLEADOS")
    for e in empleados:
        e.login()
        e.marcar_entrada()
        e.gestionar_funciones()
        print()

def mostrar_salas():
    print("REGISTRO DE 10 SALAS")
    for s in salas:
        s.que_sala_es()
        s.disponibilidad()
        s.limpiar()
        print()

def mostrar_zonas():
    print("REGISTRO DE 10 ZONASDE COMIDA")
    for c in zonas:
        c.disponibilidad()
        c.vender_producto(c.productos[0])
        c.actualizar_sttock(c.stock + 10)
        print()

def mostrar_peliculas():
    print("REGISTRO DE 10 PELICULAS")
    for p in peliculas:
        p.reseña()
        p.clasificacion_edad()
        print()

def mostrar_funciones():
    print("REGISTRO DE 10 FUNCIONES")
    for f in funciones:
        f.detalles_funcion()
        f.lugares_disponibles()
        print()

def mostrar_promociones():
    print('REGISTRO DE 10 PROMOCIONES')
    for q in promociones:
        q.es_valida()
        q.aplicar_descuento(500)
        print()

def hacer_reserva():


    print("INICIANDO ROCESO DE RESERVA")

    print("Usuarios disponibles:")#
    for i, u in enumerate(usuarios):
        print(f"  {i+1}. {u.name}  Saldo: ${u.dinero}  Puntos: {u.puntos}")
    a = int(input("Selecciona un usuario (numero): ")) - 1
    u = usuarios[a]

    print("Funciones dispnibles:")# numero de funcion, pelicula, sala, horario y precio
    for i, f in enumerate(funciones):
        print(f"  {i+1}. {f.pelicula.titulo}  {f.sala.lugar} ({f.sala.tipo})  {f.horario}  ${f.precio}")
    a = int(input("Seleciona una funcion (numero): ")) - 1
    f = funciones[a]

    asientos_str = input("Ingresa los asientos separados por coma (ej: A1,A2,B3): ")
    asientos = [a.strip().upper() for a in asientos_str.split(",") if a.strip()]

    print(f"Usuario: {u.name} (Puntos: {u.puntos})")
    print(f"Pelicula: '{f.pelicula.titulo}' | Sala: {f.sala.lugar} ({f.sala.tipo})")
    print(f"Seleccione sus aentos: {asientos}")

    r = Reserva(u, f, asientos)

    print("Promociones dispnibles:")
    print("  0. Sin promocion")
    for i, pr in enumerate(promociones):#numero de promocion, codigo, descuento y descripcion
        print(f"  {i+1}. {pr.codigo} - {pr.descuento}% | {pr.descripcion}")
    a = int(input("Selecciona una promocion (0 para ninguna): "))

    if a != 0:
        promo = promociones[a - 1]
        print(f"APLICANDO GESTION COMERCIAL...")
        print(f"Codigo: {promo.codigo}")
        r.aplicar_descuento(promo)


    print(f"Monto base: ${r.total:.2f}")
    r.confirmar_pago()
    print()
    r.generar_ticket()

def panel_empleado():
    print("PANEL DE EMPLEADO")
    print("Administradores disponibles:")
    admins = [e for e in empleados if isinstance(e, Administrador)]#filtro para mostrar solo los administradores
    for i, a in enumerate(admins):
        print(f"  {i+1}. {a.name}  Privilegios: {a.privilegios}")
    a = int(input("Selecciona un administrador: ")) - 1
    admin = admins[a]
    admin.login()
    admin.gestionar_funciones()

    print("¿Que deses hacer?")
    print("  1. Agregar pelicula")
    print("  2. Ver funciones")
    op = input("Opcion: ")

    if op == "1":
        titulo = input("Titulo de la pelicula: ")
        duracion = int(input("Duracion en minutos: "))
        genero = input("Genero: ")
        clasificacion = input("Clasificacion (A/B/C): ").upper()
        nueva = Pelicula(titulo, duracion, genero, clasificacion)
        admin.agregar_pelicula(peliculas, nueva)
        nueva.reseña()


    elif op == "2":
        mostrar_funciones()


# corro el menu principal
menu()

