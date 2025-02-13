from datetime import datetime, timedelta

# MATERIALES
class Material:
    def __init__(self, id_material, titulo, anio_publicacion):
        self.id = id_material
        self.titulo = titulo
        self.anio_publicacion = anio_publicacion
        self.estado = "disponible"  

class Libro(Material):
    def __init__(self, id_material, titulo, anio, autor, genero):
        super().__init__(id_material, titulo, anio)
        self.autor = autor
        self.genero = genero

class Revista(Material):
    def __init__(self, id_material, titulo, anio, edicion, periodicidad):
        super().__init__(id_material, titulo, anio)
        self.edicion = edicion
        self.periodicidad = periodicidad

class MaterialDigital(Material):
    def __init__(self, id_material, titulo, anio, tipo_archivo, enlace):
        super().__init__(id_material, titulo, anio)
        self.tipo_archivo = tipo_archivo
        self.enlace = enlace

# PERSONAS
class Persona:
    def __init__(self, nombre, id_persona):
        self.nombre = nombre
        self.id = id_persona

class Usuario(Persona):
    def __init__(self, nombre, id_persona):
        super().__init__(nombre, id_persona)
        self.materiales_prestados = []  

    def prestar_material(self, material):
        if material.estado == "disponible":
            material.estado = "prestado"
            self.materiales_prestados.append(material)
            print(f"{self.nombre} ha tomado prestado '{material.titulo}'.")
        else:
            print(f"'{material.titulo}' no está disponible.")

    def devolver_material(self, material):
        if material in self.materiales_prestados:
            material.estado = "disponible"
            self.materiales_prestados.remove(material)
            print(f"{self.nombre} ha devuelto '{material.titulo}'.")
        else:
            print(f"{self.nombre} no tiene '{material.titulo}' prestado.")

class Bibliotecario(Persona):
    def agregar_material(self, material, sucursal):
        sucursal.catalogo.append(material)
        print(f"{self.nombre} ha agregado '{material.titulo}' a {sucursal.nombre}.")

    def transferir_material(self, material, origen, destino):
        if material in origen.catalogo:
            origen.catalogo.remove(material)
            destino.catalogo.append(material)
            print(f"{self.nombre} ha transferido '{material.titulo}' de {origen.nombre} a {destino.nombre}.")
        else:
            print(f"'{material.titulo}' no se encontró en {origen.nombre}.")

# SUCURSAL
class Sucursal:
    def __init__(self, nombre):
        self.nombre = nombre
        self.catalogo = []  

#Sucursales
sucursal_puebla = Sucursal("Sucursal Puebla")
sucursal_atlixco = Sucursal("Sucursal Atlixco")

#Materiales
libro1 = Libro(10, "El llano en llamas", 1953, "Juan Rulfo", "Cuento")
revista1 = Revista(20, "Revista Clio", 2024, "Edición Especial", "Mensual")
digital1 = MaterialDigital(30, "Open English", 2022, "HTML", "https://www.openenglish.com/")

#Agregar a lista materiales a sucursales
sucursal_puebla.catalogo.append(libro1)
sucursal_puebla.catalogo.append(revista1)
sucursal_atlixco.catalogo.append(digital1)

#Crear personas
usuario1 = Usuario("Pedro Pérez", 1)
biblio1 = Bibliotecario("Carlos Fuentes", 2)

#Materiales disponibles en sucursales
print("Materiales disponibles:")
for sucursal in [sucursal_puebla, sucursal_atlixco]:
    print(f"\n{sucursal.nombre}:")
    for material in sucursal.catalogo:
        print(f"- {material.titulo} ({material.estado})")

#Préstamo de un libro
print("\n--- Préstamo ---")
usuario1.prestar_material(libro1)

#Estado después del préstamo
print("\nDespués del préstamo:")
for sucursal in [sucursal_puebla, sucursal_atlixco]:
    print(f"\n{sucursal.nombre}:")
    for material in sucursal.catalogo:
        print(f"- {material.titulo} ({material.estado})")

#Devolución del libro
print("\n--- Simulación de devolución ---")
usuario1.devolver_material(libro1)

#Estado después de la devolución
print("\nEstado después de la devolución:")
for sucursal in [sucursal_puebla, sucursal_atlixco]:
    print(f"\n{sucursal.nombre}:")
    for material in sucursal.catalogo:
        print(f"- {material.titulo} ({material.estado})")

#Acciones del bibliotecario
print("\n--- Acciones del bibliotecario ---")
nuevo_libro = Libro(102, "El Princito", 1943, "Antoine de Saint Exupéry", "Libro")
biblio1.agregar_material(nuevo_libro, sucursal_atlixco)
biblio1.transferir_material(revista1, sucursal_puebla, sucursal_atlixco)

#Catálogo final en cada sucursal
print("\nCatálogo final:")
for sucursal in [sucursal_puebla, sucursal_atlixco]:
    print(f"\n{sucursal.nombre}:")
    for material in sucursal.catalogo:
        print(f"- {material.titulo} ({material.estado})")