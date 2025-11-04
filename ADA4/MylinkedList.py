class Nodo:
    """
    Representa un único nodo en una lista enlazada.
    Almacena un 'valor' y un puntero 'siguiente' al próximo nodo.
    """
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    """
    Representa una lista simplemente enlazada.
    Maneja la 'cabeza' (head) de la lista y el 'tamaño' (size).
    """
    
    def __init__(self):
        """Inicializa una lista vacía."""
        self.cabeza = None  
        self.tamaño = 0

    def esta_vacia(self):
        """Devuelve True si la lista no tiene nodos, False de lo contrario."""
        return self.tamaño == 0

    def __len__(self):
        """Permite usar la función len(mi_lista) para obtener el tamaño."""
        return self.tamaño

    def __str__(self):
        """
        Permite usar print(mi_lista) para mostrar la lista.
        Formato: [ Valor1 -> Valor2 -> ... -> NIL ]
        """
        if self.esta_vacia():
            return "Lista: [ VACIA ]"
        
        elementos = []
        actual = self.cabeza
        while actual:
            elementos.append(str(actual.valor))
            actual = actual.siguiente
        
        return "Lista: [ " + " -> ".join(elementos) + " -> NIL ]"

    def insertar_al_inicio(self, valor):
        """Inserta un nuevo nodo con el 'valor' dado al comienzo de la lista."""
        nuevo_nodo = Nodo(valor)
        
        nuevo_nodo.siguiente = self.cabeza  
        self.cabeza = nuevo_nodo           
        self.tamaño += 1
        print(f"-> Insertado al inicio: {valor}")

    def insertar_al_final(self, valor):
        """Inserta un nuevo nodo con el 'valor' dado al final de la lista."""
        nuevo_nodo = Nodo(valor)
        
        if self.esta_vacia():
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            
            actual.siguiente = nuevo_nodo
            
        self.tamaño += 1
        print(f"-> Insertado al final: {valor}")

    def eliminar_por_valor(self, valor):
        """
        Busca y elimina la primera ocurrencia del 'valor' en la lista.
        Devuelve True si se eliminó, False si no se encontró.
        """
        if self.esta_vacia():
            print(f"-> Error: No se puede eliminar '{valor}'. Lista vacía.")
            return False

        actual = self.cabeza
        previo = None

        while actual and actual.valor != valor:
            previo = actual
            actual = actual.siguiente

        if not actual:
            print(f"-> Error: Valor '{valor}' no encontrado.")
            return False

        if previo is None:
            self.cabeza = actual.siguiente
      
        else:
            previo.siguiente = actual.siguiente
            
        self.tamaño -= 1
        print(f"-> Eliminado por valor: {valor}")
        return True

    def eliminar_al_inicio(self):
        """
        Elimina el primer nodo de la lista.
        Devuelve el valor del nodo eliminado, o None si estaba vacía.
        """
        if self.esta_vacia():
            print("-> Error: No se puede eliminar al inicio. Lista vacía.")
            return None
            
        valor_eliminado = self.cabeza.valor
        self.cabeza = self.cabeza.siguiente 
        self.tamaño -= 1
        print(f"-> Eliminado al inicio (valor: {valor_eliminado})")
        return valor_eliminado

    def buscar(self, valor):
        """
        Busca un 'valor' en la lista.
        Devuelve True si se encuentra, False de lo contrario.
        """
        actual = self.cabeza
        while actual:
            if actual.valor == valor:
                return True
            actual = actual.siguiente
        return False

    def obtener(self, posicion):
        """
        Obtiene el valor en una 'posicion' (índice) dada.
        Devuelve el valor o None si la posición está fuera de rango.
        """
        if posicion < 0 or posicion >= self.tamaño:
            print(f"-> Error: Posición {posicion} fuera de rango (Tamaño: {self.tamaño}).")
            return None
            
        actual = self.cabeza
        for i in range(posicion):
            actual = actual.siguiente
            
        return actual.valor
