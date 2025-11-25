# Módulo 2: Scientific Python Stack y Big Data Engineering - Fundamentos

## Introducción del Módulo

Este módulo es una inmersión profunda en el ecosistema de herramientas esenciales de Python para la ciencia de datos y la ingeniería de datos. Desde la base de la computación numérica con NumPy, pasando por la manipulación y análisis de datos con Pandas, hasta la interacción con diversas fuentes de datos y la extracción de información de la web, este módulo equipa a los estudiantes con las habilidades técnicas fundamentales. Se enfatiza la comprensión de los principios detrás de estas herramientas y su aplicación en escenarios de datos del mundo real, preparando el terreno para análisis más avanzados y la construcción de modelos predictivos.

## Objetivos Pedagógicos

Al finalizar este módulo, el estudiante será capaz de:

1.  **Dominar los fundamentos de NumPy:** Comprender la estructura y eficiencia de los `ndarray`, y aplicar operaciones vectorizadas, indexación avanzada y álgebra lineal.
2.  **Manejar y manipular datos con Pandas:** Utilizar `Series` y `DataFrame` para la carga, exploración, limpieza, transformación y análisis de datos tabulares.
3.  **Interactuar con diversas fuentes de datos:** Cargar y guardar datos en formatos como CSV, Excel, HDF5, JSON, HTML, y bases de datos SQL (SQLite, PostgreSQL).
4.  **Aplicar herramientas de computación científica (SciPy):** Utilizar submódulos de SciPy para tareas como interpolación, álgebra lineal avanzada, optimización, procesamiento de señales, estadística y procesamiento de imágenes.
5.  **Realizar Web Scraping básico:** Extraer información estructurada de páginas web utilizando `requests` y `BeautifulSoup4`, entendiendo la estructura HTML y el DOM.
6.  **Comprender y aplicar Expresiones Regulares (Regex):** Utilizar Regex para buscar, extraer y manipular patrones en texto de manera eficiente.
7.  **Iniciarse en competiciones de Data Science:** Entender la dinámica de plataformas como Kaggle y realizar una exploración inicial de datos en un contexto de competición real.
8.  **Aplicar principios de Tidy Data:** Transformar datos desordenados a un formato 'tidy' utilizando `pandas.melt()` y `df.pivot_table()` para facilitar el análisis.

## Temas Tratados

### Sesión 1: NumPy, Pandas Básico y Matplotlib

*   **Python Scientific Stack Moderno:** Visión general del ecosistema actual.
*   **Configuración del Entorno:** Uso de Conda y Anaconda para la gestión de entornos y paquetes.
*   **NumPy (Numerical Python):**
    *   Arreglos N-dimensionales (`ndarray`).
    *   Operaciones vectorizadas, indexación avanzada, slicing.
    *   Álgebra lineal básica.
*   **Pandas (Python Data Analysis Library):**
    *   Estructuras de datos `Series` y `DataFrame`.
    *   Carga inicial de datos (ejemplo: Titanic `train.csv` desde URL).
    *   Exploración básica: `head()`, `info()`, `describe()`, `isnull().sum()`.
*   **Matplotlib:**
    *   Fundamentos de visualización estática.
    *   Creación de histogramas, boxplots, scatterplots y gráficos de barras.

### Sesión 2: Fuentes de Datos y Herramientas de E/S con Pandas

*   **Pandas IO Tools:** Funciones `read_` y `to_` para diferentes formatos.
*   **Archivos CSV:** Lectura (`read_csv`) y escritura (`to_csv`).
*   **Archivos Excel:** Lectura (`read_excel`) y escritura (`to_excel`), con conversión de CSV a XLSX.
*   **Archivos HDF5:** Formato eficiente para grandes volúmenes de datos (`read_hdf`, `to_hdf`).
*   **Bases de Datos SQL:**
    *   Conexión a SQLite (`sqlite3`) para bases de datos locales.
    *   Instrucciones para configurar PostgreSQL con Docker (opcional).
    *   Operaciones CRUD (`SELECT`, `INSERT`, `UPDATE`, `DELETE`) usando Pandas y SQL.
*   **Archivos JSON:** Lectura de datos JSON desde URLs.
*   **Tablas HTML:** Extracción de tablas de páginas web (`read_html`).

### Sesión 3: Introducción al Ecosistema SciPy

*   **SciPy: La Caja de Herramientas Científica:** Extensión de NumPy con algoritmos avanzados.
*   **`scipy.constants`:** Constantes físicas y matemáticas.
*   **`scipy.interpolate`:** Técnicas de interpolación de datos.
*   **`scipy.linalg`:** Álgebra lineal avanzada (inversas, resolución de sistemas).
*   **`scipy.integrate`:** Integración numérica.
*   **`scipy.optimize`:** Optimización y ajuste de curvas.
*   **`scipy.signal`:** Procesamiento de señales.
*   **`scipy.sparse`:** Manejo eficiente de matrices dispersas.
*   **`scipy.stats`:** Distribuciones de probabilidad y pruebas estadísticas.
*   **`scipy.ndimage`:** Procesamiento de imágenes N-dimensionales.
*   **`scipy.io`:** Entrada/salida de datos en formatos científicos (ej. MATLAB).

### Sesión 4: Expresiones Regulares (Regex) para el Procesamiento de Texto

*   **Fundamentos de Regex:** Sintaxis básica y el módulo `re` en Python.
*   **Patrones Básicos y Metacaracteres:** `.` `\d`, `\w`, `\s`, `[]`, `^`, `$` etc.
*   **Cuantificadores:** `*`, `+`, `?`, `{n}`, `{n,m}`.
*   **Operaciones Comunes:** `re.search()`, `re.compile()`, `re.findall()`, `re.sub()`.
*   **Agrupamiento:** Uso de paréntesis para capturar subpatrones.
*   **Consideraciones Avanzadas:** Cuantificadores greedy vs. non-greedy, flags (`re.IGNORECASE`, `re.MULTILINE`).
*   **Aplicaciones:** Uso de Regex en la limpieza de datos y NLP.

### Sesión 5: Datos Tidy (Ordenados) - Principios y Práctica

*   **Concepto de Datos Tidy:** Principios de Hadley Wickham (cada variable una columna, cada observación una fila).
*   **Problemas de Datos Desordenados:** Ejemplos de formatos comunes 'untidy'.
*   **`pandas.melt()`:** Transformar datos de formato 'ancho' a 'largo' (gathering/unpivoting).
*   **`df.pivot_table()` / `df.pivot()`:** Transformar datos de formato 'largo' a 'ancho' (spreading/pivoting).
*   **Beneficios:** Facilidad para el análisis, visualización y modelado.

### Sesión 6: Web Scraping con BeautifulSoup y Requests

*   **Fundamentos de Web Scraping:** Importancia y ética.
*   **`requests`:** Realizar solicitudes HTTP para obtener contenido web.
*   **`BeautifulSoup4` (bs4):** Parsear HTML/XML y navegar por el DOM.
*   **Búsqueda de Elementos:** Métodos `find()`, `find_all()`, y selectores CSS (`.select()`).
*   **Extracción Estructurada:** Convertir datos scrapeados en DataFrames de Pandas.
*   **Consideraciones Éticas y Legales:** `robots.txt`, términos de servicio, frecuencia de requests.

### Sesión 7: Introducción a Competiciones de Data Science con Kaggle

*   **Kaggle como Plataforma:** Competencias, datasets y comunidad.
*   **Competiciones para Principiantes:** Enfoque en el desafío **Titanic - Machine Learning from Disaster**.
*   **Acceso a Datos:** Descarga e introducción a los archivos de Kaggle.
*   **Exploración Inicial de Datos:** `head()`, `info()`, `describe()`, `isnull().sum()`, visualizaciones básicas.
*   **Flujo de Trabajo:** Pasos típicos en una competición de Kaggle (preprocesamiento, feature engineering, modelado, evaluación, envío).

## Notas del Profesor / Insights Avanzados

*   **Eficiencia Computacional:** Se destaca la importancia de las operaciones vectorizadas de NumPy y Pandas para el rendimiento en ciencia de datos.
*   **Gestión de Entornos:** Refuerzo constante sobre la importancia de Conda para la reproducibilidad del entorno.
*   **Documentación de Código:** Énfasis en comentarios claros, docstrings y seguir PEP 8.
*   **Buenas Prácticas de Datos:** La filosofía de Tidy Data como base para un análisis robusto.
*   **Web Scraping Responsable:** Aspectos éticos y legales que todo profesional debe considerar.

## Fuentes Verificadas

*   **Documentación Oficial de Python:** [https://docs.python.org/3/](https://docs.python.org/3/)
*   **Documentación de NumPy:** [https://numpy.org/doc/stable/](https://numpy.org/doc/stable/)
*   **Documentación de Pandas:** [https://pandas.pydata.org/docs/](https://pandas.pydata.org/docs/)
*   **Documentación de SciPy:** [https://docs.scipy.org/doc/scipy/reference/](https://docs.scipy.org/doc/scipy/reference/)
*   **Documentación de Matplotlib:** [https://matplotlib.org/stable/contents.html](https://matplotlib.org/stable/contents.html)
*   **Documentación de Requests:** [https://requests.readthedocs.io/en/latest/](https://requests.readthedocs.io/en/latest/)
*   **Documentación de BeautifulSoup:** [https://www.crummy.com/software/BeautifulSoup/bs4/doc/](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
*   **Documentación de Conda:** [https://conda.io/projects/conda/en/latest/user-guide/](https://conda.io/projects/conda/en/latest/user-guide/)
*   **Sitio Web de Kaggle:** [https://www.kaggle.com/](https://www.kaggle.com/)
*   **"Tidy Data" Paper de Hadley Wickham:** [https://www.jstatsoft.org/article/view/v059i10](https://www.jstatsoft.org/article/view/v059i10)

---
**Nota:** Este `README.md` es un documento vivo que complementa el contenido de los Jupyter Notebooks. Se recomienda consultarlo periódicamente para obtener una visión general y profundizar en los conceptos clave.
