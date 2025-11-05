# views/consola_view.py

class ConsolaView:
    """Vista encargada de mostrar el árbol y los resultados en consola."""

    # ---------------------------------------------
    # IMPRIMIR ÁRBOL EN FORMATO ASCII
    # ---------------------------------------------
    def imprimir_arbol(self, nodo, prefijo="", es_ultimo=True):
        """Imprime el árbol en consola con estructura tipo carpetas."""
        if nodo is not None:
            conector = "└── " if es_ultimo else "├── "
            tipo = "📁" if nodo.es_carpeta else "📄"
            print(prefijo + conector + f"{nodo.nombre} ({tipo})")

            # Ajustar prefijo para las ramas
            nuevo_prefijo = prefijo + ("    " if es_ultimo else "│   ")
            hijos = [h for h in [nodo.izquierdo, nodo.derecho] if h is not None]

            for i, hijo in enumerate(hijos):
                es_ultimo_hijo = i == len(hijos) - 1
                self.imprimir_arbol(hijo, nuevo_prefijo, es_ultimo_hijo)

    # ---------------------------------------------
    # IMPRIMIR MENSAJES Y RESULTADOS
    # ---------------------------------------------
    def mostrar_mensaje(self, mensaje: str):
        print(f"\n{mensaje}")

    def mostrar_lista(self, titulo: str, lista):
        print(f"\n{titulo}:")
        print([n.nombre for n in lista])

    def mostrar_metricas(self, comparaciones, altura):
        print("\n📊 MÉTRICAS DEL ÁRBOL:")
        print(f"Comparaciones totales: {comparaciones}")
        print(f"Altura final del árbol: {altura}")
