class Nodo:
    """
    Clase que representa un nodo dentro del Árbol Binario de Búsqueda.
    Cada nodo puede ser una carpeta o un archivo.
    """

    def __init__(self, nombre: str, es_carpeta: bool):
        self.nombre = nombre
        self.es_carpeta = es_carpeta
        self.izquierdo = None
        self.derecho = None

    def __str__(self):
        tipo = "📁 Carpeta" if self.es_carpeta else "📄 Archivo"
        return f"{self.nombre} ({tipo})"
