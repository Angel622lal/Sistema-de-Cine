# PERSONAS
class Persona:
    pers = []
    def __init__(self, nombre, id_persona):
        self.nombre = nombre
        self.id = id_persona

    def registrar(self):
            Persona.pers.append(self)
            print(f"Se ha registrado")

class Cliente(Persona):
    def __init__(self, nombre, id_persona):
        super().__init__(nombre, id_persona)  

    def realizar_pedido(self, pedido):
        pedido.ejecutar_pedido()
    
    def consultar_historial(self):
        historial = [p for p in Pedido.list_pedidos if p.cliente == self]
        if not historial:
            print("No hay pedidos en tu historial.")
            return
        for pedido in historial:
            producto_nombre = pedido.producto.nombre if pedido.producto else "Personalizado"
            print(f"{self.nombre} - {producto_nombre} - ${pedido.precio} - {pedido.estado}")

class Empleado(Persona):
    def __init__(self, nombre, id_persona, rol):
        super().__init__(nombre, id_persona)
        self.rol = rol 

    def anadir_producto(self, consumo):
        consumo.agregar_producto()

    def anadir_ingredientes(self, ingre):
        ingre.agregar_ingredientes()

    def agregar_promocion(self, promocion):
        promocion.registrar_promocion()

# Producto
class Producto_Base:
    def __init__(self, nombre_prod):
        self.nombre = nombre_prod

    def agregar_producto(self):
        Pedido.list_producto.append(self)
        print("El producto se ha agregado")
         
class Bebida(Producto_Base):
    def __init__(self, nombre_prod, tamano, tipo):
        super().__init__(nombre_prod)
        self.tamano = tamano
        self.tipo = tipo

class Postre(Producto_Base):
    def __init__(self, nombre_prod, tipo):
        super().__init__(nombre_prod)
        self.tipo = tipo

#Producto Pedido
class Pedido:
    list_producto = []
    list_pedidos = []
    def __init__(self, cliente, estado, precio, ingredientes, producto=None):
        self.cliente = cliente
        self.ingredientes = ingredientes
        self.producto = producto
        self.estado = estado
        self.precio = precio 

    def mostrar_menú(self):
        print("----BEBIDAS----"
              "Te - 50"
              "Americano - 100"
              "Capuchino - 150"
              "----POSTRES----"
              "Rebanada de pastel de chocolate - 50"
              "Crepa - 100"
            )

    def ejecutar_pedido(self):
        if self.producto is not None:
            if self.producto not in Pedido.list_producto:
                return print(f"No hay {self.producto} en el Menú")
        
        if Inventario.validar_stock(self.ingredientes) == False:
            print("No hay suficientes ingredientes")
            return False
        
        for nombre, cantidad in self.ingredientes:
            item = next((i for i in Inventario.list_ingredien if i.ingrediente == nombre), None)
            if item:
                item.existencias -= cantidad
        
        if Promocion.aplicar_promo(self.cliente) == False:
            print("No se aplico ningun descuento")

        Pedido.list_pedidos.append(self)
        print("Se ha agregado el pedido")

class Inventario:
    list_ingredien = []
    def __init__(self, ingrediente, existencias):
        self.ingrediente = ingrediente
        self.existencias = existencias

    def agregar_ingredientes(self):
        Inventario.list_ingredien.append(self)
        print("El ingrediente se ha agregado")

    @classmethod
    def disponibilidad_ingredientes(cls):
        for item in cls.list_ingredien:
            print(f"{item.ingrediente} - {item.existencias}")

    @classmethod
    def validar_stock(cls, ingredientes_requeridos):
        for nombre, cantidad in ingredientes_requeridos:
            item = next((i for i in cls.list_ingredien if i.ingrediente == nombre), None)
            if not item or item.existencias < cantidad:
                return False
        return True

class Promocion:
    list_descuentos = []
    def __init__(self, descuento):
        self.descuento = descuento

    def registrar_promocion(self):
        Promocion.list_descuentos.append(self)
        print(f"Promocion registrada")

    @classmethod
    def aplicar_promo(cls, cliente):
        n = sum(1 for p in Pedido.list_pedidos if p.cliente == cliente)
        if n >= 7 and len(cls.list_descuentos) >= 1:
            d = cls.list_descuentos[0].descuento
        elif n >= 5 and len(cls.list_descuentos) >= 2:
            d = cls.list_descuentos[1].descuento
        elif n >= 3 and len(cls.list_descuentos) >= 3:
            d = cls.list_descuentos[2].descuento
        else:
            return False
        print(f"Se aplicó el {d}% de descuento a tu compra")
        return True

#Ingredientes
Ingre1 = Inventario("Agua", 50)
Ingre2 = Inventario("Azucar", 30)
Ingre3 = Inventario("Cafe", 20)
Ingre4 = Inventario("Sobre de te", 10)
Ingre5 = Inventario("Rebanada de pastel de chocolate", 12)
Ingre6 = Inventario("Crepa", 12)

#Bebidas
Bebi1 = Bebida("Té", "Pequeño", "Caliente")
Bebi2 = Bebida("Americano", "Mediano", "Caliente")
Bebi3 = Bebida("Capuchino", "Grande", "Frio")

#Postres
Post1 = Postre("Rebanada de pastel de chocolate", "Sin gluten")
Post2 = Postre("Crepa", "Tradicional")

#Clientes
Client1 = Cliente("Angel Camacho", "574")
Client1.registrar()
Client2 = Cliente("Paris Gutierres", "946")
Client2.registrar()

#Empleados
Emp1 = Empleado("Marco Missael", "723", "Cajero")
Emp1.registrar()
Emp2 = Empleado("Luis Toscano", "456", "Administrador")
Emp2.registrar()

#Promociones
Prom1 = Promocion(20)
Prom2 = Promocion(30)
Prom3 = Promocion(40)

#Agregar alimentos
Emp2.anadir_producto(Bebi1)
Emp2.anadir_producto(Bebi2)
Emp2.anadir_producto(Bebi3)
Emp2.anadir_producto(Post1)
Emp2.anadir_producto(Post2)

#Agregar ingredientes
Emp2.anadir_ingredientes(Ingre1)
Emp2.anadir_ingredientes(Ingre2)
Emp2.anadir_ingredientes(Ingre3)
Emp2.anadir_ingredientes(Ingre4)
Emp2.anadir_ingredientes(Ingre5)
Emp2.anadir_ingredientes(Ingre6)

#Agregar promocion
Emp1.agregar_promocion(Prom1)
Emp1.agregar_promocion(Prom2)
Emp1.agregar_promocion(Prom3)

#Pedidos
Ped1 = Pedido(Client1, "Preparacion", "40", [("Sobre de te", 1), ("Azucar", 3) ], Bebi1)
Ped2 = Pedido(Client2, "Preparacion", "50", [("Cafe", 3)], Bebi2)

#Agregar pedido
Client1.realizar_pedido(Ped1)
Client2.realizar_pedido(Ped2)

#Consultar Historial
Client2.consultar_historial()
