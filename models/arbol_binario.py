from models.nodo import Nodo

class ArbolBinario:
    """
    Clase que implementa un Árbol Binario de Búsqueda (BST)
    para organizar archivos y carpetas.
    """

    def __init__(self):
        self.raiz = None

    # -----------------------------
    # INSERTAR
    # -----------------------------
    def insertar(self, nombre: str, es_carpeta: bool):
        """Inserta un nuevo nodo manteniendo la propiedad del BST."""
        nuevo = Nodo(nombre, es_carpeta)

        if self.raiz is None:
            self.raiz = nuevo
            return

        actual = self.raiz
        while True:
            # Comparación alfabética
            if nombre.lower() < actual.nombre.lower():
                if actual.izquierdo is None:
                    actual.izquierdo = nuevo
                    break
                actual = actual.izquierdo
            else:
                if actual.derecho is None:
                    actual.derecho = nuevo
                    break
                actual = actual.derecho

    # -----------------------------
    # BUSCAR
    # -----------------------------
    def buscar(self, nombre: str):
        """Busca un nodo por nombre y retorna (nodo, comparaciones)."""
        actual = self.raiz
        comparaciones = 0

        while actual is not None:
            comparaciones += 1
            if nombre.lower() == actual.nombre.lower():
                return actual, comparaciones
            elif nombre.lower() < actual.nombre.lower():
                actual = actual.izquierdo
            else:
                actual = actual.derecho

        return None, comparaciones

    # -----------------------------
    # IMPRIMIR PREORDEN (para prueba visual)
    # -----------------------------
    def imprimir_preorden(self, nodo=None, nivel=0):
        """Imprime el árbol con indentación para visualizar jerarquía."""
        if nodo is None:
            nodo = self.raiz
        if nodo is not None:
            print("   " * nivel + str(nodo))
            if nodo.izquierdo:
                self.imprimir_preorden(nodo.izquierdo, nivel + 1)
            if nodo.derecho:
                self.imprimir_preorden(nodo.derecho, nivel + 1)
    # -----------------------------
    # ELIMINAR
    # -----------------------------
    def eliminar(self, nombre: str):
        """
        Elimina un nodo del árbol manejando los tres casos:
        - Hoja
        - Nodo con un hijo
        - Nodo con dos hijos (reemplazo por sucesor)
        """
        self.raiz, caso = self._eliminar_recursivo(self.raiz, nombre)
        return caso

    def _eliminar_recursivo(self, nodo, nombre):
        if nodo is None:
            return nodo, "No encontrado"

        # Buscar el nodo a eliminar
        if nombre.lower() < nodo.nombre.lower():
            nodo.izquierdo, caso = self._eliminar_recursivo(nodo.izquierdo, nombre)
        elif nombre.lower() > nodo.nombre.lower():
            nodo.derecho, caso = self._eliminar_recursivo(nodo.derecho, nombre)
        else:
            # Nodo encontrado
            # Caso 1: Nodo hoja
            if nodo.izquierdo is None and nodo.derecho is None:
                return None, "Hoja"

            # Caso 2: Nodo con un hijo
            if nodo.izquierdo is None:
                return nodo.derecho, "Un hijo"
            elif nodo.derecho is None:
                return nodo.izquierdo, "Un hijo"

            # Caso 3: Nodo con dos hijos
            sucesor = self._minimo(nodo.derecho)
            nodo.nombre = sucesor.nombre
            nodo.es_carpeta = sucesor.es_carpeta
            nodo.derecho, _ = self._eliminar_recursivo(nodo.derecho, sucesor.nombre)
            return nodo, "Dos hijos"

        return nodo, caso

    def _minimo(self, nodo):
        """Devuelve el nodo con el valor mínimo del subárbol derecho."""
        while nodo.izquierdo is not None:
            nodo = nodo.izquierdo
        return nodo

    # -----------------------------
    # ACTUALIZAR
    # -----------------------------
    def actualizar(self, antiguo: str, nuevo: str, es_carpeta_nuevo: bool = None):
        """
        Actualiza un nodo: elimina el antiguo y crea uno nuevo con el nuevo nombre.
        - Si 'es_carpeta_nuevo' no se indica, conserva el tipo original.
        """
        # Buscar el nodo antiguo
        nodo_encontrado, _ = self.buscar(antiguo)
        if nodo_encontrado is None:
            return f"❌ No se encontró '{antiguo}' para actualizar."

        # Verificar que el nuevo nombre no exista ya
        nodo_existente, _ = self.buscar(nuevo)
        if nodo_existente:
            return f"⚠️ No se puede renombrar: '{nuevo}' ya existe."

        # Determinar tipo (si no se da, conserva el anterior)
        tipo = es_carpeta_nuevo if es_carpeta_nuevo is not None else nodo_encontrado.es_carpeta

        # Eliminar el nodo antiguo
        _, caso = self._eliminar_recursivo(self.raiz, antiguo)

        # Insertar el nuevo nodo
        self.insertar(nuevo, tipo)

        return f"✅ Actualizado '{antiguo}' → '{nuevo}' (caso de eliminación: {caso})"

    # -----------------------------
    # RECORRIDOS DEL ÁRBOL (versión corregida)
    # -----------------------------
    def preorden(self, nodo=None, lista=None):
        """Recorrido preorden (Raíz - Izquierdo - Derecho)."""
        if lista is None:
            lista = []
        if nodo is None:
            nodo = self.raiz
        if nodo:
            lista.append(nodo)
            if nodo.izquierdo:
                self.preorden(nodo.izquierdo, lista)
            if nodo.derecho:
                self.preorden(nodo.derecho, lista)
        return lista

    def inorden(self, nodo=None, lista=None):
        """Recorrido inorden (Izquierdo - Raíz - Derecho)."""
        if lista is None:
            lista = []
        if nodo is None:
            nodo = self.raiz
        if nodo:
            if nodo.izquierdo:
                self.inorden(nodo.izquierdo, lista)
            lista.append(nodo)
            if nodo.derecho:
                self.inorden(nodo.derecho, lista)
        return lista

    def postorden(self, nodo=None, lista=None):
        """Recorrido postorden (Izquierdo - Derecho - Raíz)."""
        if lista is None:
            lista = []
        if nodo is None:
            nodo = self.raiz
        if nodo:
            if nodo.izquierdo:
                self.postorden(nodo.izquierdo, lista)
            if nodo.derecho:
                self.postorden(nodo.derecho, lista)
            lista.append(nodo)
        return lista

    # -----------------------------
    # RECORRIDO POR NIVELES (BFS)
    # -----------------------------
    def por_niveles(self):
        """Recorrido por niveles (BFS usando una cola)."""
        if self.raiz is None:
            return []
        cola = [self.raiz]
        resultado = []
        while cola:
            actual = cola.pop(0)
            resultado.append(actual)
            if actual.izquierdo:
                cola.append(actual.izquierdo)
            if actual.derecho:
                cola.append(actual.derecho)
        return resultado

        # -----------------------------
        # ALTURA DEL ÁRBOL
        # -----------------------------

    def altura(self, nodo=None):
        """Calcula la altura del árbol (número máximo de niveles)."""
        # Si es la llamada inicial, arrancamos desde la raíz
        if nodo is None:
            nodo = self.raiz
        # Caso base: árbol vacío
        if nodo is None:
            return 0
        # Caso recursivo: si hay hijos, sumamos la altura
        altura_izq = self.altura(nodo.izquierdo) if nodo.izquierdo else 0
        altura_der = self.altura(nodo.derecho) if nodo.derecho else 0
        return 1 + max(altura_izq, altura_der)
