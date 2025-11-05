# controllers/arbol_controller.py

from models.arbol_binario import ArbolBinario
from views.consola_view import ConsolaView


class ArbolController:
    """Controlador principal que conecta el modelo con la vista y ejecuta las pruebas del taller."""

    def __init__(self):
        self.arbol = ArbolBinario()
        self.vista = ConsolaView()
        self.comparaciones_totales = 0

    # --------------------------------------------
    # CONSTRUCCIÓN INICIAL DEL ÁRBOL
    # --------------------------------------------
    def construir_arbol_inicial(self):
        nodos_iniciales = [
            ("M", True), ("C", True), ("R", True), ("A", False),
            ("E", False), ("P", False), ("S", True), ("Q", False),
            ("B", True), ("D", False), ("F", True), ("T", False),
            ("Z", True), ("N", False)
        ]

        for nombre, es_carpeta in nodos_iniciales:
            self.arbol.insertar(nombre, es_carpeta)
        self.vista.mostrar_mensaje("✅ Árbol inicial construido correctamente.")
        self.vista.imprimir_arbol(self.arbol.raiz)

    # --------------------------------------------
    # PRUEBAS DE BÚSQUEDA
    # --------------------------------------------
    def pruebas_busqueda(self):
        self.vista.mostrar_mensaje("🔍 Pruebas de búsqueda:")
        busquedas = ["A", "Z", "C", "R", "X", "Y"]  # 2 izq, 2 der, 2 inexistentes

        for nombre in busquedas:
            nodo, comparaciones = self.arbol.buscar(nombre)
            self.comparaciones_totales += comparaciones
            if nodo:
                self.vista.mostrar_mensaje(f"✅ Encontrado '{nombre}' ({'📁' if nodo.es_carpeta else '📄'}) con {comparaciones} comparaciones.")
            else:
                self.vista.mostrar_mensaje(f"❌ '{nombre}' no encontrado ({comparaciones} comparaciones).")

    # --------------------------------------------
    # PRUEBAS DE ACTUALIZACIÓN
    # --------------------------------------------
    def pruebas_actualizacion(self):
        self.vista.mostrar_mensaje("♻️ Pruebas de actualización:")
        casos = [
            ("A", "A_1"),      # hoja
            ("P", "P_1"),      # un hijo
            ("M", "M_1"),      # raíz
        ]
        for antiguo, nuevo in casos:
            msg = self.arbol.actualizar(antiguo, nuevo)
            self.vista.mostrar_mensaje(msg)
            self.vista.imprimir_arbol(self.arbol.raiz)

    # --------------------------------------------
    # PRUEBAS DE ELIMINACIÓN
    # --------------------------------------------
    def pruebas_eliminacion(self):
        self.vista.mostrar_mensaje("🗑️ Pruebas de eliminación:")
        casos = ["A_1", "P_1", "M_1"]  # hoja, un hijo, raíz
        for nombre in casos:
            caso = self.arbol.eliminar(nombre)
            self.vista.mostrar_mensaje(f"Eliminado '{nombre}' (caso: {caso})")
            self.vista.imprimir_arbol(self.arbol.raiz)

    # --------------------------------------------
    # RECORRIDOS Y MÉTRICAS
    # --------------------------------------------
    def recorridos_y_metricas(self):
        self.vista.mostrar_lista("📜 Preorden", self.arbol.preorden())
        self.vista.mostrar_lista("📜 Inorden", self.arbol.inorden())
        self.vista.mostrar_lista("📜 Postorden", self.arbol.postorden())
        self.vista.mostrar_lista("📜 Por niveles", self.arbol.por_niveles())

        altura = self.arbol.altura()
        self.vista.mostrar_metricas(self.comparaciones_totales, altura)

    # --------------------------------------------
    # FLUJO PRINCIPAL
    # --------------------------------------------
    def ejecutar_todas_las_pruebas(self):
        self.construir_arbol_inicial()
        self.pruebas_busqueda()
        self.pruebas_actualizacion()
        self.pruebas_eliminacion()
        self.recorridos_y_metricas()
