# 🌳 Taller Integrador – Árboles Binarios (MVC en Python)

## 👨‍💻 Autor
**Nombre:** Alejandro Carmona  

**Programa:** Ingeniería de Sistemas 

**Rol:** Desarrollador principal  

**Responsabilidades:**  
- Diseño y desarrollo del modelo del Árbol Binario de Búsqueda (BST).  
- Implementación del patrón MVC (modelo, vista, controlador).  
- Programación de métodos CRUD, recorridos y métricas.  
- Elaboración del README y documento de evidencias.  
- Pruebas de funcionamiento y validación de los requisitos de la guía.

---
## 🎯 Objetivo General
Diseñar e implementar un **Árbol Binario de Búsqueda (BST)** que modele el árbol de documentos de una empresa (carpetas y archivos), aplicando el patrón de arquitectura **MVC**.

El sistema debe permitir operaciones CRUD, búsquedas, actualizaciones y eliminaciones selectivas, además de mostrar recorridos, métricas y un diagrama ASCII del árbol en consola.
---

## 🧱 Arquitectura del Proyecto (MVC)

ProyectoBST/
 ├── models/
 │    ├── nodo.py
 │    └── arbol_binario.py
 ├── views/
 │    └── consola_view.py
 ├── controllers/
 │    └── arbol_controller.py
 ├── main.py
 └── README.md


### 🧩 Descripción de capas

| Capa | Archivo | Descripción |
|------|----------|-------------|
| **Model** | `nodo.py`, `arbol_binario.py` | Lógica del árbol binario, CRUD, recorridos y altura. |
| **View** | `consola_view.py` | Muestra el árbol en consola (ASCII), métricas y resultados. |
| **Controller** | `arbol_controller.py` | Ejecuta todas las pruebas del taller de forma automática. |
| **Main** | `main.py` | Punto de entrada del programa. Ejecuta el controlador. |

---

## ⚙️ Funcionalidades Implementadas

### CRUD del Árbol
- `insertar(nombre, es_carpeta)`  
- `buscar(nombre)`  
- `actualizar(antiguo, nuevo)` → (Eliminar + Insertar)  
- `eliminar(nombre)` → Maneja casos:  
  - Nodo hoja  
  - Nodo con un hijo  
  - Nodo con dos hijos (reemplazo por sucesor)

### Recorridos
- Preorden  
- Inorden  
- Postorden  
- Por niveles (BFS)

### Métricas
- Altura total del árbol  
- Comparaciones acumuladas en búsquedas  
- Resultados visuales del CRUD  

### Visualización ASCII
Ejemplo de impresión del árbol:

```
└── M (📁)
    ├── C (📁)
    │   ├── A (📄)
    │   └── E (📄)
    └── R (📁)
        ├── P (📄)
        └── Z (📁)
```

---

## 🧪 Pruebas Realizadas (según guía)

| Tipo de Prueba | Descripción | Estado |
|----------------|--------------|---------|
| **Construcción inicial** | 14 nodos (mezcla de carpetas y archivos). | ✅ |
| **Búsquedas rápidas** | 6 pruebas (2 izq, 2 der, 2 inexistentes). | ✅ |
| **Actualizaciones selectivas** | Hoja, un hijo, raíz. | ✅ |
| **Eliminaciones selectivas** | Hoja, un hijo, raíz. | ✅ |
| **Recorridos** | Preorden, Inorden, Postorden, Niveles. | ✅ |
| **Métricas** | Comparaciones y altura final. | ✅ |

---

## 🧠 Justificación del Recorrido Inorden

El recorrido **Inorden** (izquierdo → raíz → derecho) es el que **ordena los elementos de un Árbol Binario de Búsqueda (BST)**.

Esto sucede porque:
- Todos los elementos del subárbol izquierdo son **menores** que la raíz.  
- Todos los elementos del subárbol derecho son **mayores** que la raíz.  

Por tanto, al recorrer en ese orden, los nodos se visitan **en secuencia ascendente** (orden alfabético en este caso).  
El resultado del recorrido Inorden valida que el árbol **mantiene su propiedad de orden**.

---

## 📊 Resultados Finales

| Métrica | Valor aproximado |
|----------|------------------|
| **Altura del árbol final:** | 4 niveles |
| **Comparaciones totales:** | ~25 |
| **Nodos insertados:** | 14 |
| **Nodos eliminados:** | 3 |

---

## ▶️ Ejecución del Proyecto

### Requisitos
- Python 3.11 o superior  
- PyCharm o cualquier IDE con soporte de consola

### Cómo ejecutar
1. Clonar o abrir la carpeta del proyecto `ProyectoBST`.  
2. Ejecutar el archivo `main.py`.  
3. Observar en la consola las salidas automáticas de:
   - Árbol inicial  
   - Búsquedas  
   - Actualizaciones  
   - Eliminaciones  
   - Recorridos  
   - Métricas finales  

---

## 📚 Conclusiones

- Se aplicó correctamente la **arquitectura MVC**.  
- El árbol cumple con las condiciones estructurales exigidas por la guía (14 nodos, dos subárboles, hojas, y nodo con un solo hijo).  
- El sistema permite observar el comportamiento del BST mediante un **diagrama ASCII y métricas numéricas**.  
- La estructura modular facilita la **lectura, mantenimiento y ampliación del código**.  
- El recorrido Inorden confirma el **ordenamiento correcto** del árbol.  

---

## 📷 Evidencias
Las salidas del programa y las pruebas fueron capturadas en el documento:
**“Evidencias Taller Árbol Binario.docx”**, con pantallazos de cada prueba.

---

## 🔗 Repositorio Público
https://github.com/alejandrocarmona1127-design/proyectoBST_alejandro_carmona?tab=readme-ov-file
**Versión final etiquetada:** `release-unidad1`

---

© 2025 — release- unidad 1 -- Programación 3, 
            Ingeniería de Sistemas.



