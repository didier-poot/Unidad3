import sys
class Nodo:
    
    def __init__(self, nombre):
        self.nombre = nombre
        self.siguiente = None

class ListaEnlazada:

    def __init__(self):
        self.cabeza = None

    def imprimir(self):
        """Imprime todos los ingredientes en la lista."""
        if not self.cabeza:
            print("(Este postre no tiene ingredientes registrados)")
            return
        
        actual = self.cabeza
        while actual:
            print(f"  -> {actual.nombre}")
            actual = actual.siguiente

    def insertar(self, nombre_ingrediente):
        """
        Inserta un nuevo ingrediente al inicio de la lista.
        Verifica si el ingrediente ya existe.
        """
        if self.buscar(nombre_ingrediente):
            print(f"  AVISO: El ingrediente '{nombre_ingrediente}' ya existe en la lista.")
            return False

        nuevo_nodo = Nodo(nombre_ingrediente)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo
        print(f"  -> Ingrediente '{nombre_ingrediente}' añadido.")
        return True

    def eliminar(self, nombre_ingrediente):
        """
        Elimina un ingrediente de la lista.
        """
        actual = self.cabeza
        previo = None

        while actual and actual.nombre.lower() != nombre_ingrediente.lower():
            previo = actual
            actual = actual.siguiente

        if not actual:
            print(f"  ERROR: Ingrediente '{nombre_ingrediente}' no encontrado.")
            return False

        if not previo:
            self.cabeza = actual.siguiente
        else:
            previo.siguiente = actual.siguiente
        
        print(f"  -> Ingrediente '{nombre_ingrediente}' eliminado.")
        return True

    def buscar(self, nombre_ingrediente):
        """Busca un ingrediente y devuelve True si existe, False si no."""
        actual = self.cabeza
        while actual:
            if actual.nombre.lower() == nombre_ingrediente.lower():
                return True
            actual = actual.siguiente
        return False

class Postre:

    def __init__(self, nombre):
        self.nombre = nombre
        self.ingredientes = ListaEnlazada()

def buscar_postre(menu, nombre_postre):
    """
    Realiza una búsqueda binaria en el arreglo de postres (que está ordenado).
    """
    bajo, alto = 0, len(menu) - 1
    
    while bajo <= alto:
        medio = (bajo + alto) // 2
        nombre_actual = menu[medio].nombre
        
        if nombre_actual.lower() == nombre_postre.lower():
            return True, medio, menu[medio]  # Encontrado
        elif nombre_actual.lower() < nombre_postre.lower():
            bajo = medio + 1
        else:
            alto = medio - 1
            
    return False, bajo, None

def mostrar_ingredientes(menu, nombre_postre):

    print(f"\n--- a. Buscando ingredientes de: {nombre_postre} ---")
    encontrado, _, postre_obj = buscar_postre(menu, nombre_postre)
    
    if not encontrado:
        print(f"ERROR: Postre '{nombre_postre}' no encontrado en el menú.")
        return
        
    print(f"Ingredientes de '{nombre_postre}':")
    postre_obj.ingredientes.imprimir()

def insertar_ingrediente(menu, nombre_postre, nombre_ingrediente):

    print(f"\n--- b. Añadiendo ingrediente a: {nombre_postre} ---")
    encontrado, _, postre_obj = buscar_postre(menu, nombre_postre)
    
    if not encontrado:
        print(f"ERROR: Postre '{nombre_postre}' no encontrado. No se puede añadir ingrediente.")
        return
    
    postre_obj.ingredientes.insertar(nombre_ingrediente)

def eliminar_ingrediente(menu, nombre_postre, nombre_ingrediente):
    
    print(f"\n--- c. Eliminando ingrediente de: {nombre_postre} ---")
    encontrado, _, postre_obj = buscar_postre(menu, nombre_postre)
    
    if not encontrado:
        print(f"ERROR: Postre '{nombre_postre}' no encontrado. No se puede eliminar ingrediente.")
        return
        
    postre_obj.ingredientes.eliminar(nombre_ingrediente)

def dar_alta_postre(menu, nombre_postre, lista_ingredientes_iniciales):

    print(f"\n--- d. Dando de alta el postre: {nombre_postre} ---")
    encontrado, indice_insercion, _ = buscar_postre(menu, nombre_postre)
    
    if encontrado:
        print(f"ERROR: El postre '{nombre_postre}' ya existe en el menú.")
        return

    nuevo_postre = Postre(nombre_postre)
    
    print(f"Añadiendo ingredientes iniciales para {nombre_postre}:")
    if not lista_ingredientes_iniciales:
        print("  -> (Se añade sin ingredientes iniciales)")
    else:
        for ing in lista_ingredientes_iniciales:
            nuevo_postre.ingredientes.insertar(ing)
            
    menu.insert(indice_insercion, nuevo_postre)
    print(f"¡Postre '{nombre_postre}' añadido al menú en la posición {indice_insercion}!")

def dar_baja_postre(menu, nombre_postre):
    """
    e. Dé de baja un postre con todos sus ingredientes.
    """
    print(f"\n--- e. Dando de baja el postre: {nombre_postre} ---")
    encontrado, indice, _ = buscar_postre(menu, nombre_postre)
    
    if not encontrado:
        print(f"ERROR: El postre '{nombre_postre}' no se puede eliminar porque no existe.")
        return
        
    menu.pop(indice)
    print(f"¡Postre '{nombre_postre}' y todos sus ingredientes han sido eliminados del menú!")
  
  def eliminar_postres_duplicados(menu):
    print("\n--- f. Eliminando Postres Duplicados ---")
    
    if len(menu) < 2:
        print("-> El menú tiene menos de 2 elementos, no pueden existir duplicados.")
        return

    nombres_vistos = set()
    eliminados_count = 0

    i = 0
    while i < len(menu):
        postre_actual = menu[i]
        nombre_actual = postre_actual.nombre.lower() # Comparamos en minúsculas

        if nombre_actual in nombres_vistos:
            print(f"  -> Duplicado encontrado: '{postre_actual.nombre}'. Eliminando...")
            menu.pop(i)
            eliminados_count += 1
            
        else:
            nombres_vistos.add(nombre_actual)
            i += 1

    if eliminados_count == 0:
        print("-> No se encontraron postres duplicados.")
    else:
        print(f"-> Se eliminaron {eliminados_count} postres duplicados.")

def mostrar_menu_completo(menu):
    print("\n" + "="*30)
    print("      MENÚ DE POSTRES (Ordenado)")
    print("="*30)
    if not menu:
        print("(El menú está vacío)")
        return
            
    for i, postre in enumerate(menu):
        print(f"\n[{i}] {postre.nombre.upper()}")
        postre.ingredientes.imprimir()
    print("="*30)

menu_postres = []

dar_alta_postre(menu_postres, "Pastel de Chocolate", ["Harina", "Azúcar", "Chocolate", "Huevos"])
dar_alta_postre(menu_postres, "Flan", ["Leche", "Huevos", "Azúcar", "Vainilla"])
dar_alta_postre(menu_postres, "Arroz con Leche", ["Arroz", "Leche", "Canela"])
dar_alta_postre(menu_postres, "Gelatina", ["Agua", "Grenetina"])

dar_alta_postre(menu_postres, "Flan", ["Leche", "Huevos"])
mostrar_menu_completo(menu_postres)

mostrar_ingredientes(menu_postres, "Arroz con Leche")

mostrar_ingredientes(menu_postres, "Tiramisú")
insertar_ingrediente(menu_postres, "Pastel de Chocolate", "Mantequilla")
insertar_ingrediente(menu_postres, "Pastel de Chocolate", "Harina")
insertar_ingrediente(menu_postres, "Tiramisú", "Café")

mostrar_ingredientes(menu_postres, "Pastel de Chocolate")
eliminar_ingrediente(menu_postres, "Flan", "Vainilla")
eliminar_ingrediente(menu_postres, "Flan", "Chocolate")
eliminar_ingrediente(menu_postres, "Tiramisú", "Café")
mostrar_ingredientes(menu_postres, "Flan")
dar_baja_postre(menu_postres, "Gelatina")
dar_baja_postre(menu_postres, "Gelatina")
print("\n--- ESTADO FINAL DEL MENÚ ---")
mostrar_menu_completo(menu_postres)

postre_flan_duplicado = Postre("Flan")
postre_flan_duplicado.ingredientes.insertar("Ingrediente falso 1")
menu_postres.insert(2, postre_flan_duplicado)

postre_pastel_duplicado = Postre("Pastel de Chocolate")
postre_pastel_duplicado.ingredientes.insertar("Ingrediente falso 2")
menu_postres.append(postre_pastel_duplicado) 

print("[Menú ANTES de eliminar duplicados]")
mostrar_menu_completo(menu_postres)

eliminar_postres_duplicados(menu_postres)

print("[Menú DESPUÉS de eliminar duplicados]")
mostrar_menu_completo(menu_postres)
