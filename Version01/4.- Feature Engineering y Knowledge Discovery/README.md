# Módulo 4: Feature Engineering y Knowledge Discovery

---

## 1. Introducción del Módulo

Este módulo se adentra en lo que muchos consideran el corazón creativo y el diferenciador clave en proyectos de ciencia de datos exitosos: el **arte de la ingeniería de características y el descubrimiento de conocimiento**. Si los módulos anteriores nos dieron las herramientas para manejar y analizar datos, este módulo nos enseña a esculpirlos, a transformar los datos brutos en *features* (variables) que revelen la señal oculta y potencien el rendimiento de los modelos de aprendizaje automático.

Se cubrirán las tres disciplinas principales: **Feature Engineering** (crear nuevas variables), **Feature Selection** (elegir las variables más importantes) y **Feature Extraction** (extraer información de datos no estructurados como texto e imágenes). Finalmente, el módulo culmina con una introducción al **Knowledge Discovery**, explorando cómo analizar datos estructurados en forma de grafos y cómo enriquecer nuestros conjuntos de datos a través de APIs externas.

---

## 2. Objetivos Pedagógicos

Al finalizar este módulo, el estudiante será capaz de:

-   **Crear y Transformar Features:** Diseñar y construir variables informativas a partir de datos existentes para mejorar la performance de los modelos.
-   **Implementar Técnicas de Preprocesamiento:** Aplicar correctamente el escalado de características y la codificación de variables categóricas.
-   **Seleccionar las Features más Relevantes:** Utilizar métodos de selección de características para reducir la dimensionalidad, mejorar la eficiencia del modelo y evitar el sobreajuste.
-   **Extraer Features de Texto e Imágenes:** Convertir datos no estructurados (texto e imágenes) en representaciones numéricas (vectores) que puedan ser utilizadas por algoritmos de machine learning.
-   **Analizar Datos de Redes/Grafos:** Modelar y analizar relaciones entre entidades utilizando librerías como NetworkX para descubrir nodos y comunidades influyentes.
-   **Integrar Datos a través de APIs:** Conectarse a APIs web para obtener y procesar datos en formato JSON.

---

## 3. Temas Tratados

### Sesión 1: Feature Engineering y Feature Selection
-   **Feature Engineering:**
    -   **Imputación de Valores Faltantes:** Estrategias simples (media, mediana) y avanzadas (k-NN, MICE).
    -   **Transformaciones Matemáticas:** Logarítmica, Box-Cox para manejar distribuciones sesgadas.
    -   **Creación de Features Polinómicas y de Interacción.**
    -   **Discretización (Binning):** Convertir variables numéricas en categóricas.
    -   **Features basadas en Fechas y Horas.**
-   **Codificación de Variables Categóricas:**
    -   `OneHotEncoder` vs. `LabelEncoder`: Cuándo y por qué usar cada uno.
-   **Escalado de Features:**
    -   `StandardScaler`, `MinMaxScaler`, `RobustScaler`. La importancia del escalado para algoritmos sensibles a la distancia (e.g., SVM, k-NN).
-   **Feature Selection:**
    -   **Filter Methods:** Selección por varianza, correlación, pruebas estadísticas (chi-cuadrado).
    -   **Wrapper Methods:** Recursive Feature Elimination (RFE).
    -   **Embedded Methods:** Selección a través de modelos que tienen coeficientes de importancia (e.g., `Lasso (L1)`).

### Sesión 2: Feature Extraction de Datos No Estructurados
-   **Feature Extraction de Texto:**
    -   **Bag-of-Words (BoW):** `CountVectorizer`.
    -   **TF-IDF (Term Frequency-Inverse Document Frequency):** `TfidfVectorizer`. La intuición de pesar las palabras por su importancia.
    -   **N-gramas:** Capturando contexto más allá de palabras individuales.
-   **Feature Extraction de Imágenes con OpenCV:**
    -   **Lectura y Representación de Imágenes:** Las imágenes como arrays de NumPy.
    -   **Espacios de Color:** RGB, HSV, Escala de grises.
    -   **Preprocesamiento de Imágenes:** Redimensionamiento, umbralización (thresholding), filtros y transformaciones morfológicas.
    -   **Extracción de Features Clásicas:** Histogramas de color, Histogramas de Gradientes Orientados (HOG).

### Sesión 3: Knowledge Discovery - Grafos y APIs
-   **Análisis de Redes con NetworkX:**
    -   **Creación de Grafos:** A partir de listas de adyacencia o DataFrames (e.g., los datos en `friend_relationships`).
    -   **Visualización de Grafos.**
    -   **Análisis de Centralidad:**
        -   **Degree Centrality:** Número de conexiones.
        -   **Betweenness Centrality:** Importancia como "puente" en la red.
        -   **Eigenvector Centrality:** Influencia (conectado a nodos influyentes).
-   **Trabajando con APIs Web:**
    -   Uso de la librería `requests` para realizar peticiones HTTP (`GET`).
    -   Manejo de respuestas en formato **JSON**.
    -   Transformación de datos JSON anidados en un DataFrame de Pandas.

---

## 4. Ejemplos y Notas del Profesor

### Nota sobre el "Data Leakage" en el Preprocesamiento
Un error crítico y común en la ingeniería de características es el **data leakage** (fuga de datos). Esto ocurre cuando se usa información del conjunto de prueba (o de todo el conjunto de datos) para entrenar el preprocesador.

**Incorrecto (Fuga de Datos):**
```python
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X) # Se ajusta el scaler con TODOS los datos
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y)
```
En el código anterior, la media y desviación estándar de `X_test` se usaron para escalar `X_train`, "contaminando" el entrenamiento con información del futuro.

**Correcto:**
```python
from sklearn.preprocessing import StandardScaler
X_train, X_test, y_train, y_test = train_test_split(X, y)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train) # 1. AJUSTAR y transformar en el train set
X_test_scaled = scaler.transform(X_test)       # 2. SOLO transformar en el test set
```
**Insight:** Siempre se debe dividir los datos en `train` y `test` **antes** de cualquier preprocesamiento. Los `scalers`, `encoders`, etc., se ajustan (`fit`) **únicamente** con el conjunto de entrenamiento y luego se usan para transformar (`transform`) tanto el conjunto de entrenamiento como el de prueba.

### TF-IDF: La Intuición
-   **Term Frequency (TF):** ¿Qué tan frecuente es una palabra en un documento? Si aparece mucho, es importante *para ese documento*.
-   **Inverse Document Frequency (IDF):** ¿Qué tan frecuente es una palabra en *toda la colección de documentos*? Si aparece en todos los documentos (e.g., "el", "la"), no es distintiva y recibe un peso bajo.

**TF-IDF = TF * IDF**. Este puntaje es alto para palabras que son frecuentes en un documento pero raras en general, capturando así las palabras que mejor caracterizan a ese documento en particular. Es la base de muchos sistemas de recomendación y motores de búsqueda.

---

## 5. Fuentes y Referencias

-   **Documentación de Scikit-learn sobre Preprocesamiento:** [https://scikit-learn.org/stable/modules/preprocessing.html](https://scikit-learn.org/stable/modules/preprocessing.html)
-   **Documentación de OpenCV-Python:** [https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html)
-   **Tutorial de NetworkX:** [https://networkx.org/documentation/stable/tutorial.html](https://networkx.org/documentation/stable/tutorial.html)
-   **Libro "Feature Engineering for Machine Learning" de Alice Zheng & Amanda Casari:** Una guía completa y práctica.

---
