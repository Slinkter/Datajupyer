# Módulo 6: Comunicación, Visualización y Productos de Datos

---

## 1. Introducción del Módulo

Un análisis o modelo, por más sofisticado que sea, carece de valor si sus resultados no pueden ser comunicados de manera clara, efectiva y accionable. Este módulo se centra en la "última milla" del proceso de ciencia de datos: la transformación de hallazgos en **insights** y la creación de **productos de datos** que entreguen valor a los usuarios finales.

Se abordarán los principios teóricos de la percepción visual y el "data storytelling" para construir narrativas convincentes. Los estudiantes explorarán un amplio abanico de herramientas de visualización, desde la fundamental **Matplotlib** hasta librerías interactivas modernas como **Bokeh** y **Plotly**. Finalmente, el módulo introduce el concepto de "producto de datos", culminando en la creación de una aplicación web simple que sirva como vehículo para presentar un análisis o modelo interactivo.

---

## 2. Objetivos Pedagógicos

Al finalizar este módulo, el estudiante será capaz de:

-   **Aplicar los Principios de la Visualización de Datos Efectiva:** Elegir el tipo de gráfico adecuado para cada propósito y utilizar atributos visuales (color, forma, tamaño) para transmitir información de forma clara y sin ambigüedades.
-   **Construir Narrativas con Datos (Data Storytelling):** Estructurar una presentación o informe que guíe a la audiencia a través de los hallazgos de un análisis de manera lógica y persuasiva.
-   **Dominar el Ecosistema de Visualización de Python:** Crear visualizaciones estáticas con Matplotlib y Seaborn, y desarrollar gráficos y dashboards interactivos con Bokeh y Plotly.
-   **Diseñar y Construir Productos de Datos Simples:** Entender qué constituye un producto de datos y ser capaz de encapsular un análisis o modelo en una aplicación web básica usando herramientas como Streamlit, Flask o Dash.
-   **Comunicar Resultados a Diferentes Audiencias:** Adaptar el lenguaje y el nivel de detalle técnico para presentar los resultados a audiencias tanto técnicas como de negocio.

---

## 3. Temas Tratados

### Sesión 1: Productos de Datos y Comunicación
-   **El Concepto de "Producto de Datos":**
    -   Definición: Un producto cuyo valor deriva de los datos (e.g., un dashboard de BI, un sistema de recomendación, un modelo de scoring expuesto vía API).
-   **Data Storytelling:**
    -   Estructura de una narrativa: Contexto, conflicto (el problema de negocio), clímax (el insight clave) y resolución.
    -   Identificar y entender a la audiencia.
-   **Introducción a Frameworks de Aplicaciones Web:**
    -   Un vistazo a herramientas como **Streamlit** o **Flask** para convertir un script de análisis en una aplicación web interactiva (`myapp.py`).

### Sesión 2: Principios de Visualización de Datos
-   **Gramática de los Gráficos (Grammar of Graphics):**
    -   La teoría subyacente de cómo construir gráficos a partir de componentes (datos, mapeos estéticos, geometrías).
-   **Percepción Visual y Atributos Pre-atentivos:**
    -   Cómo el cerebro humano procesa la información visual. Uso efectivo de color, tamaño, forma y posición.
-   **Catálogo de Gráficos y sus Usos:**
    -   **Comparación:** Gráficos de barras.
    -   **Distribución:** Histogramas, Box plots, Violin plots.
    -   **Relación:** Scatter plots, Bubble charts.
    -   **Composición:** Gráficos de pastel (y por qué evitarlos), Treemaps.
    -   **Evolución en el Tiempo:** Gráficos de líneas.
-   **Práctica Fundamental con Matplotlib:**
    -   La API orientada a objetos: `Figure`, `Axes`, `Subplots`.
    -   Personalización de gráficos: etiquetas, títulos, leyendas, colores.

### Sesión Sábado: Visualización Interactiva y Construcción de un Dashboard
-   **Visualización Interactiva:**
    -   **Bokeh:**
        -   Creación de gráficos con herramientas interactivas (pan, zoom, hover).
        -   Diseño de layouts y dashboards simples.
    -   **Plotly:**
        -   Creación de gráficos interactivos de alta calidad (Plotly Express).
        -   Entendiendo la arquitectura de Plotly (figuras como diccionarios JSON).
-   **Proyecto de Dashboard:**
    -   Taller práctico para construir un dashboard interactivo que visualice uno de los conjuntos de datos del curso (e.g., `life_expectancy.csv`).
    -   Integración de múltiples gráficos, widgets (sliders, dropdowns) y texto para contar una historia.
    -   (Avanzado) Despliegue de la aplicación (`myapp.py`) en un servidor local, posiblemente manejando concurrencia (`threads.py`).

---

## 4. Ejemplos y Notas del Profesor

### Nota sobre Matplotlib: API Orientada a Objetos vs. Pyplot
Matplotlib tiene dos interfaces. La `pyplot` (basada en estado) es rápida para gráficos sencillos, pero la **API orientada a objetos (OO)** es mucho más robusta y flexible para gráficos complejos o múltiples.

**Pyplot (rápido pero limitado):**
```python
import matplotlib.pyplot as plt
plt.plot(x, y)
plt.title("Mi Gráfico")
plt.show()
```

**API Orientada a Objetos (preferida):**
```python
import matplotlib.pyplot as plt
fig, ax = plt.subplots() # ax es el objeto que representa el gráfico
ax.plot(x, y)
ax.set_title("Mi Gráfico")
ax.set_xlabel("Eje X")
fig.suptitle("Título Principal de la Figura")
plt.show()
```
**Insight:** Acostúmbrate a usar siempre la API orientada a objetos (`fig, ax = plt.subplots()`). Te da un control total sobre cada elemento de la figura y es la base sobre la que se construyen librerías de más alto nivel como Seaborn.

### ¿Cuándo usar Interactividad?
La interactividad (hover-tools, zoom, filtros) no es un fin en sí mismo. Debe usarse con un propósito.

-   **Bueno para la Exploración:** La interactividad es fantástica en la fase de EDA, ya que permite al analista "jugar" con los datos, hacer zoom en áreas de interés y descubrir patrones que no son visibles en una vista estática.
-   **Potencialmente Malo para la Explicación:** En una presentación (data storytelling), demasiada interactividad puede distraer. A menudo, un conjunto de gráficos estáticos bien elegidos y anotados puede contar una historia de manera más efectiva y controlada. Un dashboard interactivo, sin embargo, es un producto excelente para que un usuario de negocio explore los datos por su cuenta dentro de unos límites definidos.

**Insight:** Usa la interactividad para **empoderar la exploración**, no para **complicar la explicación**.

---

## 5. Fuentes y Referencias

-   **Documentación de Matplotlib:** [https://matplotlib.org/stable/index.html](https://matplotlib.org/stable/index.html)
-   **Documentación de Bokeh:** [https://docs.bokeh.org/en/latest/](https://docs.bokeh.org/en/latest/)
-   **Documentación de Plotly Python:** [https://plotly.com/python/](https://plotly.com/python/)
-   **Libro "Storytelling with Data" de Cole Nussbaumer Knaflic:** Un clásico sobre cómo comunicar insights.
-   **Libro "Fundamentals of Data Visualization" de Claus O. Wilke:** Una referencia teórica excelente y gratuita en línea.

---
