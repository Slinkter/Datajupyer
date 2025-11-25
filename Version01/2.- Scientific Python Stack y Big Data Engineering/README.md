# Módulo 2: Scientific Python Stack y Big Data Engineering

---

## 1. Introducción del Módulo

Este módulo sumerge a los estudiantes en el corazón del ecosistema de Python para la ciencia de datos: el **Scientific Python Stack**. Una vez dominados los fundamentos avanzados de Python, el siguiente paso es aprender a manejar, procesar y analizar datos a gran escala. Este módulo cubre el ciclo de vida completo de la ingeniería de datos, desde la adquisición de datos de fuentes dispares hasta su transformación en formatos estructurados y "tidy" (ordenados), listos para el análisis.

Se introducirán las librerías que forman la columna vertebral de casi cualquier proyecto de ciencia de datos: **NumPy** para la computación numérica de alto rendimiento, **Pandas** para la manipulación y el análisis de datos tabulares, y **SciPy** para algoritmos científicos avanzados. Además, se abordarán técnicas cruciales para la obtención de datos del mundo real, como el web scraping, las consultas a bases de datos SQL y el procesamiento de texto con expresiones regulares.

---

## 2. Objetivos Pedagógicos

Al finalizar este módulo, el estudiante será capaz de:

-   **Dominar la Computación con Arrays:** Utilizar **NumPy** para realizar operaciones matemáticas y lógicas sobre arreglos N-dimensionales de manera eficiente.
-   **Manipular Datos Estructurados:** Emplear **Pandas** para la ingesta, limpieza, transformación, unión y agregación de datos utilizando DataFrames.
-   **Aplicar los Principios de "Tidy Data":** Reestructurar conjuntos de datos desordenados a un formato `tidy` utilizando técnicas de `melt` (gathering) y `pivot` (spreading) para facilitar el análisis.
-   **Adquirir Datos de Múltiples Fuentes:** Escribir scripts para extraer datos de archivos (CSV, SQLite), bases de datos relacionales (usando SQL) y páginas web (usando BeautifulSoup).
-   **Procesar Datos de Texto:** Utilizar expresiones regulares (regex) para la búsqueda, extracción y validación de patrones en datos de texto no estructurado.
-   **Comprender el Ecosistema Científico:** Reconocer las funciones de las principales librerías del stack (NumPy, SciPy, Pandas, Matplotlib) y cómo interactúan entre sí.

---

## 3. Temas Tratados

### Sesión 1: El Stack Científico - NumPy y Pandas
-   **NumPy (`ndarray`):**
    -   **Creación de Arrays:** `np.array`, `np.arange`, `np.linspace`, `np.zeros`, `np.random`.
    -   **Operaciones Vectorizadas:** El poder de las Universal Functions (Ufuncs) para evitar bucles lentos en Python.
    -   **Indexing y Slicing:** Técnicas avanzadas de selección de datos, incluyendo *boolean indexing* y *fancy indexing*.
    -   **Broadcasting:** Las reglas que permiten a NumPy operar con arrays de diferentes tamaños.
-   **Pandas (Series y DataFrame):**
    -   **Estructuras de Datos:** La `Serie` (1D) y el `DataFrame` (2D).
    -   **Ingesta y Escritura de Datos:** `pd.read_csv`, `pd.read_sql`, `df.to_csv`, etc.
    -   **Selección de Datos:** `loc` (basada en etiquetas), `iloc` (basada en posición) y `[]`.
    -   **Limpieza de Datos:** Manejo de valores nulos (`.dropna()`, `.fillna()`), cambio de tipos de datos (`.astype()`).
    -   **Operaciones Esenciales:** `groupby`, `merge`, `join`, `concat`.

### Sesión 2: Fuentes de Datos y Principios de Tidy Data
-   **Fuentes de Datos:**
    -   **Bases de Datos Relacionales:** Conexión a bases de datos con librerías como `sqlite3` o `SQLAlchemy` y ejecución de consultas SQL con Pandas.
    -   **Web Scraping:** Introducción a HTML y uso de `BeautifulSoup4` para parsear el DOM y extraer información.
    -   **Expresiones Regulares (Regex):** Uso del módulo `re` para la manipulación de texto.
-   **Principios de "Tidy Data":**
    -   **Definición:** 1) Cada variable es una columna, 2) Cada observación es una fila, 3) Cada tipo de unidad observacional es una tabla.
    -   **Transformación de Formatos:**
        -   **Gathering (Wide to Long):** Uso de `pd.melt()` para convertir columnas que son valores en filas.
        -   **Spreading (Long to Wide):** Uso de `pd.pivot_table()` para la operación inversa, útil para crear resúmenes o features.

### Sesión 3: Ecosistema SciPy y Aplicación Práctica
-   **Introducción al Ecosistema SciPy:**
    -   Un vistazo a los submódulos más importantes de `scipy`:
        -   `scipy.stats`: Funciones estadísticas y pruebas de hipótesis.
        -   `scipy.optimize`: Algoritmos de optimización y ajuste de curvas.
        -   `scipy.integrate`: Integración numérica.
        -   `scipy.linalg`: Álgebra lineal avanzada.
-   **Reto Práctico (Kaggle):**
    -   Aplicación de todos los conceptos del módulo en un conjunto de datos del mundo real.
    -   El flujo de trabajo completo: adquisición, limpieza, tidying, análisis exploratorio básico y preparación de los datos para el modelado.

---

## 4. Ejemplos y Notas del Profesor

### Nota sobre Vectorización en NumPy
La eficiencia de NumPy no proviene de la magia, sino de la **vectorización**. Las operaciones se implementan en C y se aplican simultáneamente a todo el arreglo, en lugar de iterar elemento por elemento en Python, que es mucho más lento.

```python
import numpy as np
import time

# Enfoque NO Pythonic (lento)
lista = list(range(10_000_000))
start = time.time()
resultado_lista = [x * 2 for x in lista]
end = time.time()
print(f"Tiempo con lista y bucle: {end - start:.4f}s")

# Enfoque NumPy (rápido)
array_np = np.arange(10_000_000)
start = time.time()
resultado_np = array_np * 2
end = time.time()
print(f"Tiempo con NumPy vectorizado: {end - start:.4f}s")
```
**Insight:** La diferencia de rendimiento es de órdenes de magnitud. En ciencia de datos, si te encuentras escribiendo un `for` sobre un array de NumPy o una columna de Pandas, detente y busca una operación vectorizada. Probablemente exista.

### El Poder del "Method Chaining" en Pandas
Para mejorar la legibilidad y la reproducibilidad de tus transformaciones de datos, es una excelente práctica encadenar las operaciones de Pandas. Esto crea un "pipeline" de transformaciones fácil de seguir.

```python
import pandas as pd

# Supongamos que tenemos un DataFrame 'df_ventas'

# Enfoque con variables intermedias (difícil de leer)
df_filtrado = df_ventas[df_ventas['region'] == 'Norte']
df_agrupado = df_filtrado.groupby('producto')
df_sumado = df_agrupado['ventas'].sum()
df_final = df_sumado.reset_index()

# Enfoque con Method Chaining (limpio y legible)
df_ventas_norte = (
    df_ventas
    .copy() # Evita SettingWithCopyWarning
    [df_ventas['region'] == 'Norte']
    .groupby('producto')['ventas']
    .sum()
    .reset_index()
    .rename(columns={'ventas': 'ventas_totales_norte'})
    .sort_values(by='ventas_totales_norte', ascending=False)
)
```
**Insight:** Encadenar métodos crea una receta clara de cómo se transformaron los datos. Usa paréntesis para dividir la cadena en múltiples líneas (como se muestra arriba) para una legibilidad máxima, cumpliendo con el estándar PEP 8.

---

## 5. Fuentes y Referencias

-   **Documentación oficial de NumPy:** [https://numpy.org/doc/stable/](https://numpy.org/doc/stable/)
-   **Documentación oficial de Pandas:** [https://pandas.pydata.org/docs/](https://pandas.pydata.org/docs/)
-   **Documentación oficial de SciPy:** [https://docs.scipy.org/doc/scipy/](https://docs.scipy.org/doc/scipy/)
-   **Libro "Python for Data Analysis" de Wes McKinney:** Escrito por el creador de Pandas, es la referencia definitiva.
-   **Artículo "Tidy Data" de Hadley Wickham:** [https://www.jstatsoft.org/article/view/v059i10](https://www.jstatsoft.org/article/view/v059i10)

---