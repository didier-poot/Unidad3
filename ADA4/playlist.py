# Importamos tu biblioteca
from MylinkedList import ListaEnlazada

class Playlist:

    def __init__(self, nombre):
        self.nombre = nombre
        self._lista_canciones = ListaEnlazada()
        self._cancion_actual = None
        print(f"Playlist '{self.nombre}' creada.")

    def agregar_cancion(self, nombre_cancion):

        print(f"Añadiendo a la cola: '{nombre_cancion}'")
        self._lista_canciones.insertar_al_final(nombre_cancion)

    def reproducir_siguiente(self):

        if self._lista_canciones.esta_vacia():
            print("-> Playlist terminada. No hay más canciones.")
            self._cancion_actual = None
            return
            
        self._cancion_actual = self._lista_canciones.eliminar_al_inicio()
        print(f"Reproduciendo Ahora: {self._cancion_actual}")
    
    def ver_siguiente(self):
       
        siguiente = self._lista_canciones.obtener(0)
        if siguiente:
            print(f"Siguiente en la fila: '{siguiente}'")
        else:
            print("No hay más canciones en la cola.")
            
    def mostrar_playlist_actual(self):
        print("-" * 30)
        print(f"Estado de la Playlist: '{self.nombre}'")
        if self._cancion_actual:
            print(f"Sonando: {self._cancion_actual}")
        else:
            print("Sonando: (Silencio)")
        
        print(f"En cola: {self._lista_canciones}")
        print("-" * 30)


mi_playlist = Playlist("playlist1")

mi_playlist.agregar_cancion("Musica 1")
mi_playlist.agregar_cancion("Musica 2")
mi_playlist.agregar_cancion("Musica 3")

mi_playlist.mostrar_playlist_actual()

mi_playlist.reproducir_siguiente()

mi_playlist.mostrar_playlist_actual()

mi_playlist.ver_siguiente()

mi_playlist.agregar_cancion("Musica 4")

mi_playlist.reproducir_siguiente()
mi_playlist.mostrar_playlist_actual()

mi_playlist.reproducir_siguiente()
mi_playlist.reproducir_siguiente()

mi_playlist.mostrar_playlist_actual()
mi_playlist.reproducir_siguiente()