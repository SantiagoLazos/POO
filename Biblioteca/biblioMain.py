from biblioBack import *


# Crear materiales
libro1 = Libro("García Márquez", "Ficción", 1, "Cien años de soledad", 1967, True)
revista1 = Revista(1, "Mensual", 2, "National Geographic", 2023, True)
digital1 = MaterialDigital(3, "Introducción a Python", 2022, True, "PDF", "bit.lyClaseJimmy1")

# Crear sucursal y agregar materiales
sucursal1 = Sucursal("Sucursal Centro")
sucursal1.catalogLocal.append(libro1)
sucursal1.catalogLocal.append(revista1)
sucursal1.catalogLocal.append(digital1)


# Crear personas
usuario1 = Usuario(3, "Ana López", 101, "Usuario")
biblio1 = Bibliotecario("María González", 201, "Bibliotecario")


# Registrar un préstamo
prestamo1 = Prestamo(1, "2026-03-19", "2026-04-02", usuario1, libro1)
usuario1.LibrosPresta2.append(prestamo1)

# Mostrar info
print("Sucursal:", sucursal1.sucursal)
print("Materiales en sucursal:", len(sucursal1.catalogLocal))
print("Usuario:", usuario1.name)
print("Préstamos activos:", len(usuario1.LibrosPresta2))
print("Bibliotecario:", biblio1.name)