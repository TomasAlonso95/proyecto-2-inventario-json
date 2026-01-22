import json
import os

class Inventario:
    def __init__(self, archivo="inventario.json"):
        self.archivo = archivo
        self.productos = self.cargar_inventario()

    def cargar_inventario(self):
        """Si el archivo existe, carga los datos. Si no, devuelve diccionario vacío."""
        if not os.path.exists(self.archivo):
            return {}
            
        try:
            with open(self.archivo, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {} # Si el archivo está corrupto, inicia vacío

    def guardar_inventario(self):
        """Guarda el diccionario actual en el archivo JSON."""
        with open(self.archivo, "w") as f:
            json.dump(self.productos, f, indent=4)

    def agregar_producto(self, id, nombre, stock):
        if id in self.productos:
            print(f"\n❌ Error: El ID '{id}' ya existe.")
        else:
            self.productos[id] = {"nombre": nombre, "stock": stock}
            self.guardar_inventario() # <--- Guardado Automático
            print(f"\n✅ Producto '{nombre}' agregado y guardado.")

    def mostrar_productos(self):
        if not self.productos:
            print("\n📂 El inventario está vacío.")
        else:
            print("\n--- 📦 INVENTARIO (Leyendo la Base de Datos) ---")
            for id, info in self.productos.items():
                print(f"ID: {id} | Producto: {info['nombre']} | Stock: {info['stock']}")

    def actualizar_stock(self, id, nuevo_stock):
        if id in self.productos:
            self.productos[id]["stock"] = nuevo_stock
            self.guardar_inventario() # <--- Guardado Automático
            print(f"\n✅ Stock de '{id}' actualizado a {nuevo_stock}.")
        else:
            print("\n❌ Error: ID no encontrado.")
            
    def borrar_producto(self, id):
        if id in self.productos:
            del self.productos[id]
            self.guardar_inventario() # <--- Guardado Automático
            print(f"\n🗑️ Producto '{id}' eliminado correctamente.")
        else:
            print("\n❌ Error: ID no encontrado.")
    
    def buscar_producto(self, texto):
        resultados = [] # 1. Tu lista vacía
        for id, info in self.productos.items():
            if texto.lower() in info["nombre"].lower():
                # 3. Lo encontramos -> Lo guardamos junto con su ID
                # (Guardamos una tupla o lista pequeña con los datos)
                resultados.append(f"ID: {id} | {info["nombre"]} | Stock: {info["stock"]}")
        return resultados 



# --- MENÚ DE EJECUCIÓN ---
if __name__ == "__main__":
    sistema = Inventario()
    
    while True:
        print("\n" + "="*30)
        print("   SISTEMA DE INVENTARIO 2.0")
        print("="*30)
        print("1. Agregar Producto")
        print("2. Mostrar Inventario")
        print("3. Actualizar Stock")
        print("4. Borrar Producto")
        print("5. 🔍 Buscar Producto")
        print("6. Salir")
        
        opcion = input("\n👉 Seleccione una opción: ")

        if opcion == "1":
            id = input("ID: ")
            nombre = input("Nombre: ")
            try:
                stock = int(input("Stock: "))
                sistema.agregar_producto(id, nombre, stock)
            except ValueError:
                print("\n❌ Error: El stock debe ser un número.")

        elif opcion == "2":
            sistema.mostrar_productos()

        elif opcion == "3":
            id = input("ID a actualizar: ")
            try:
                stock = int(input("Nuevo Stock: "))
                sistema.actualizar_stock(id, stock)
            except ValueError:
                print("\n❌ Error: El stock debe ser un número.")

        elif opcion == "4":
            id = input("ID a borrar: ")
            sistema.borrar_producto(id)

        elif opcion == "5":
            texto = input("¿Qué estas buscando?: ")
            hallazgos = sistema.buscar_producto(texto)
            if len(hallazgos) > 0:
                print(f"\n✅ Se encontraron {len(hallazgos)} coincidencias:")
                for item in hallazgos:
                    print(item)
            else:
                print(f"\n❌ No se encontraron productos con '{texto}'.")

        elif opcion == "6": # <--- Cambiamos a 6
            print("\n👋 ¡Cerrando sistema! Tus datos quedan seguros.")
            break
            
        else:
            print("\n❌ Opción no válida.")