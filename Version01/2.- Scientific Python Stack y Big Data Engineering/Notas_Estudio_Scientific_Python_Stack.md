# NOTAS DE ESTUDIO: Scientific Python Stack y Big Data Engineering

## Orden de Estudio (Jerarquía de Aprendizaje)

| # | Archivo | Tema Principal | Nivel |
|---|---------|---------------|-------|
| 1 | `2.- Sesión 1 Scientific Python Stack` | **FUNDAMENTOS**: NumPy + Pandas | Base |
| 2 | `Fuentes de datos` | Import/Export (CSV, Excel, SQL, JSON, HTML) | Básico |
| 3 | `Regex` | Expresiones regulares para texto | Intermedio |
| 4 | `Web Scraping - BeautifulSoup4` | Scraping web | Intermedio |
| 5 | `Tidy Data` | Transformación melt/gather | Intermedio |
| 6 | `SQL` | Consultas a bases de datos | Intermedio |
| 7 | `Introducción al ecosistema SciPy` | SciPy avanzado | Avanzado |
| 8 | `Reto Kaggle` | Proyecto integrador | Práctico |

---

# PROMPT: PERFIL DE DATA ENGINEER / INGENIERO DE DATOS

## Rol: Supervisor de Apuntes de Estudio - Data Engineer

### Contexto
Eres un **Ingeniero de Datos Senior (Data Engineer)** con más de 10 años de experiencia en:
- Arquitectura de datos a escala empresarial
- Pipelines de ETL/ELT con Python, SQL y tecnologías cloud
- Calidad y gobernanza de datos
- Optimización de rendimiento en procesamiento de grandes volúmenes

Tu misión es **supervisar, enriquecer y corregir** estos apuntes de estudio para que sean:
1. **Técnicamente precisos** - Sin errores conceptuales
2. **Completos** - Sin huecos de explicación
3. **Útiles para producción** - Casos de uso reales en entornos profesionales

### Directrices para Enriched Comments

Para cada bloque de código o concepto, añade:

#### 1. Explicación del CONCEPTO (¿Por qué?)
- Contexto profesional: ¿Cuándo USARÍAS esto en un proyecto real?
- Errores comunes que cometen los juniors
- Alternativas y trade-offs

#### 2. Ejemplo PRÁCTICO (Cómo)
- Caso de uso real (no artificial)
- Datos de ejemplo realistasss (nombres reales, sectores reales)
- Output esperado con interpretación

#### 3. NOTAS de Rendimiento y Optimización
- Complejidad temporal/espacial si aplica
- Cuándo usar qué método
- Anti-patterns a evitar

#### 4. Debugging y Errores Comunes
- Errores típicos y cómo solucionarlos
- Cómo depurar effectively

---

# 2.- Sesión 1 Scientific Python Stack ( FUNDAMENTOS )

## 🎯 Objetivos de Aprendizaje

Al terminar esta sesión podrás:
- Comprender el ecosistema NumPy y Pandas
- Manipular arrays y DataFrames
- Importar y exportar datos
- Realizar análisis básico de datos

---

## SECCIÓN 1: El Ecosistema SciPy

### ¿Por qué Python para Data Science?

El ecosistema SciPy es el estándar de la industria para data science:

```
┌─────────────────────────────────────────────────────────────┐
│              ECOSISTEMA SCIPY                            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   NUMPY          → Cálculos numéricos rápidos            │
│   PANDAS        → Datos tabulares (como Excel)         │
│   MATPLOTLIB     → Gráficos y visualizaciones          │
│   SCIPY          → Funciones científicas                │
│   SCIKIT-LEARN  → Machine Learning                    │
│                                                            │
│   +10,000 librerías adicionales!                         │
└──��──────────────────────────────────────────────────────────┘
```

**CONCEPTO EXPLÍCITO:**
NumPy es la base de TODAS las librerías científicas de Python. Cuando haces `import pandas as pd`, internamente Pandas usa arrays de NumPy. Entender NumPy es entender cómo funcionan las librerías "por debajo".

---

## SECCIÓN 2: NumPy - Numerical Python

### ¿Qué es NumPy?

NumPy es el corazón del ecosistema científico. Proporciona **arrays многimensionales** optimizados.

```python
import numpy as np

# Crear array
numeros = np.array([1, 2, 3, 4, 5])
print(f"Array: {numeros}")
print(f"Tipo: {type(numeros)}")
print(f"Tipo de datos: {numeros.dtype}")
```

**CONCEPTO EXPLÍCITO:**

| Atributo | Descripción |
|---------|-------------|
| `np.array()` | Función constructora de arrays |
| `dtype` | Tipo de datos: `int32`, `int64`, `float32`, `float64`, `bool` |
| `ndim` | Número de dimensiones |
| `shape` | Tupla con el tamaño de cada dimensión |
| `size` | Total de elementos |

**EJEMPLO PRÁCTICO:**
```python
# array de enteros
arr_int = np.array([1, 2, 3])
print(arr_int.dtype)  # int32 o int64 dependiendo del sistema

# array de floats
arr_float = np.array([1.0, 2.0, 3.0])
print(arr_float.dtype)  # float64

# array de booleanos
arr_bool = np.array([True, False, True])
print(arr_bool.dtype)  # bool
```

### Array vs Lista

| Lista Python | Array NumPy |
|-----------|-----------|
| `[1,2,3]` | `np.array([1,2,3])` |
| Lenta | **Rápida** (hasta 50x más rapide en operaciones vectorizadas) |
| Flexible | Optimizada para cálculo numérico |
| Unidimensional | **Multidimensional** |

**POR QUÉ ES IMPORTANTE:**
NumPy es hasta 50x más rápido porque:
1. Usa memoria contigua (cache-friendly)
2. Operaciones vectorizadas en C (sin bucles Python)
3. Parallellización automática con SIMD

### Comparación de Velocidad

```python
import time

# Con lista
lista = list(range(1000000))
start = time.time()
resultado = [x * 2 for x in lista]
print(f"Lista: {time.time() - start:.4f}s")

# Con NumPy
arr = np.arange(1000000)
start = time.time()
resultado = arr * 2
print(f"NumPy: {time.time() - start:.4f}s")
```

**RESULTADO TÍPICO:**
- Lista: ~0.1-0.2s
- NumPy: ~0.002s (50x más rápido)

### Arrays Multidimensionales

```python
# Array 2D (matriz)
matriz = np.array([[1, 2, 3], [4, 5, 6]])
print("Matriz 2D:")
print(matriz)
print(f"\nForma: {matriz.shape}")

# Array 3D
arr_3d = np.array([[[1,2], [3,4]], [[5,6], [7,8]]])
print(f"\nArray 3D forma: {arr_3d.shape}")
```

**CONCEPTO EXPLÍCITO - Shape:**
- `shape` es una tupla que indica el tamaño de cada dimensión
- `(3, 4)` = 3 filas, 4 columnas
- `(2, 3, 4)` = 2 páginas, 3 filas, 4 columnas

### Operaciones con NumPy

```python
a = np.array([1, 2, 3])
b = np.array([10, 20, 30])

# Operaciones elemento a elemento
print(f"a + b = {a + b}")   # [11, 22, 33]
print(f"a * b = {a * b}")   # [10, 40, 90]
print(f"a ** 2 = {a ** 2}") # [1, 4, 9]

# Funciones de agregación
print(f"sum(a) = {np.sum(a)}")    # 6
print(f"mean(a) = {np.mean(a)}")  # 2.0
print(f"std(a) = {np.std(a)}")   # 0.816...
```

**CONCEPTO EXPLÍCITO - Broadcasting:**
NumPy aplica operaciones elemento a elemento automáticamente. Esto se llama "broadcasting".

---

## SECCIÓN 3: Pandas - Data Analysis

### ¿Qué es Pandas?

Pandas proporciona **DataFrames** - como hojas de cálculo de Excel en Python.

```python
import pandas as pd

# Crear DataFrame
data = {
    'nombre': ['Ana', 'Carlos', 'María'],
    'edad': [25, 30, 28],
    'ciudad': ['CDMX', 'GDL', 'MTY']
}

df = pd.DataFrame(data)
print(df)
```

### Estructura del DataFrame

```
┌─────────────────────────────────────────────────────────────┐
│              DATAFRAME                                   │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   Columnas (Series)     │ Índice                       │
│   ┌──────┬──────┬─┐   │                             │
│   │nombre│edad │   │   │ 0 → Ana (25, CDMX)          │
│   ├──────┼──────┼─┤   │ 1 → Carlos (30, GDL)       │
│   │Ana   │ 25  │   │ 2 → María (28, MTY)         │
│   │Carlos│ 30  │   │                             │
│   │María │ 28  │   │                             │
│   └──────┴──────┴─┘   │                             │
│        FILAS             │                             │
└─────────────────────────────────────────────────────────────┘
```

**CONCEPTO EXPLÍCITO:**
- Cada columna es una **Series** (array unidimensional con índice)
- El DataFrame es un diccionario de Series
- Tienen índice (por defecto 0, 1, 2, ... pero puede ser cualquier cosa)

### Información del DataFrame

```python
# Información del DataFrame
print(df.info())
print(f"\nColumnas: {df.columns.tolist()}")
print(f"\nForma: {df.shape}")
```

### Selección de Datos

```python
# Seleccionar columna
print("Nombres:", df['nombre'].tolist())

# Seleccionar fila por índice (etiqueta)
print("\nPrimera fila:")
print(df.loc[0])

# Seleccionar por posición (índice numérico)
print("\nPrimera fila (iloc):")
print(df.iloc[0])
```

**CONCEPTO EXPLÍCITO - loc vs iloc:**
- `loc` = selección por ETIQUETA (índice nominal)
- `iloc` = selección por POSICIÓN (índice numérico)

### Filtrar Datos

```python
# Filtrar por condición
df_mayores = df[df['edad'] > 26]
print("Mayores de 26:")
print(df_mayores)
```

**CONCEPTO EXPLÍCITO:**
El filtrado en Pandas devuelve un DataFrame booleano. Se usa como máscara.

### Estadísticas

```python
# describe() da estadísticas
print(df.describe())
```

**CONCEPTO EXPLÍCITO:**
`describe()` solo funciona para columnas numéricas. Ignora las categóricas.

---

## SECCIÓN 4: Importar y Exportar Datos

### CSV

```python
# Exportar a CSV
df.to_csv('datos.csv', index=False)

# Importar de CSV
df_csv = pd.read_csv('datos.csv')
print(df_csv)
```

**ERRORES COMUNES:**
- `index=False` evita escribir el índice como columna
- Si el CSV tiene comas en valores, usar `sep=';'` o especificar delimitador

### Excel

```python
# Instalar openpyxl primero: pip install openpyxl
# Exportar a Excel
df.to_excel('datos.xlsx', index=False)

# Importar de Excel
# df_excel = pd.read_excel('datos.xlsx')
# print(df_excel)
```

**NOTA:**
Se requiere `openpyxl` para archivos .xlsx modernos

### JSON

```python
# Exportar a JSON
df.to_json('datos.json', orient='records')

# Importar de JSON
df_json = pd.read_json('datos.json')
print(df_json)
```

### Formatos Soportados

| Formato | Función Lectura | Función Escritura |
|---------|---------------|----------------|
| CSV | `read_csv` | `to_csv` |
| Excel | `read_excel` | `to_excel` |
| JSON | `read_json` | `to_json` |
| HTML | `read_html` | `to_html` |
| SQL | `read_sql` | `to_sql` |
| Parquet | `read_parquet` | `to_parquet` |
| Feather | `read_feather` | `to_feather` |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1: Array NumPy

```python
# Crea un array de NumPy con los números del 1 al 10
arr = np.arange(1, 11)
print(f"Array: {arr}")
print(f"Media: {np.mean(arr)}")
print(f"Suma: {np.sum(arr)}")
```

### Ejercicio 2: DataFrame con Películas

```python
# DataFrame con películas
peliculas = pd.DataFrame({
    'titulo': ['Toy Story', 'Avatar', 'Titanic'],
    'año': [1995, 2009, 1997],
    'rating': [8.3, 7.9, 7.7]
})
print(peliculas)

# Filtrar películas con rating > 8
print("\nMejor rating:")
print(peliculas[peliculas['rating'] > 8])
```

---

## 📋 Resumen

| Librería | Propósito | Estructura |
|--------|---------|----------|
| NumPy | Cálculos | array |
| Pandas | Datos tabulares | DataFrame |
| Matplotlib | Gráficos | figuras |

---

# Fuentes de Datos

## 🎯 Objetivos

- Cargar datos desde múltiples fuentes
- Entender los diferentes formatos
- Manejar datos complejos

---

## Pandas y DataFrames

**CONCEPTO EXPLÍCITO:**
Pandas es la librería principal para análisis de datos en Python. Equivale a `data.frame` en R y a dplyr.

### Series

```python
# Series - array unidimensional con índice
s = pd.Series([7, 'Heisenberg', 3.14, -1789710578, 'Happy Eating!'])
s
```

**CONCEPTO EXPLÍCITO:**
Una Series tiene:
- Valores (data)
- Índice (labels)
- Tipo de datos (dtype)

### DataFrame

```python
# DataFrame
data = {'year': [2010, 2011, 2012, 2011, 2012, 2010, 2011, 2012],
        'team': ['Bears', 'Bears', 'Bears', 'Packers', 'Packers', 'Lions', 'Lions', 'Lions'],
        'wins': [11, 8, 10, 15, 11, 6, 10, 4],
        'losses': [5, 8, 6, 1, 5, 10, 6, 12]}
football = pd.DataFrame(data, columns=['year', 'team', 'wins', 'losses'])
football
```

---

## Pandas IO Tools

### Lectura

| Función | Formato |
|--------|---------|
| `read_csv` | CSV |
| `read_excel` | MS Excel |
| `read_hdf` | HDF5 |
| `read_sql` | SQL Query |
| `read_json` | JSON |
| `read_html` | HTML Tables |
| `read_gbq` | Google BigQuery |
| `read_stata` | STATA |
| `read_sas` | SAS |
| `read_clipboard` | Portapapeles |
| `read_pickle` | Pickle (serialización Python) |

### Escritura

| Función | Formato |
|--------|---------|
| `to_csv` | CSV |
| `to_excel` | Excel |
| `to_hdf` | HDF5 |
| `to_sql` | SQL |
| `to_json` | JSON |
| `to_html` | HTML |
| `to_gbq` | Google BigQuery |
| `to_stata` | STATA |
| `to_clipboard` | Portapapeles |
| `to_pickle` | Pickle |

---

## Lectura desde CSV

```python
# Lectura básica
csv_dataframe = pd.read_csv('data/FL_insurance_sample.csv')

# Con encoding específico
csv_dataframe_500000_rows = pd.read_csv('data/Spreadsheet-500000-rows.csv', encoding="ISO-8859-1")

len(csv_dataframe_500000_rows)  # 499999
```

**PARÁMETROS IMPORTANTES de read_csv:**
- `sep` - delimitador (default: ',')
- `encoding` - codificación (default: 'utf-8')
- `header` - fila de encabezados (default: 0)
- `names` - nombres de columnas personalizados
- `dtype` - tipos de datos por columna
- `parse_dates` - columnas a parsear como fechas
- `nrows` - número de filas a leer
- `skiprows` - filas a saltar

---

## Lectura desde Excel

```python
# Reading data from Excel
pd.read_excel('data/FL_insurance_sample.xlsx', 'Sheet1', index_col=None, na_values=['NA'])
```

**PARÁMETROS IMPORTANTES:**
- `sheet_name` - nombre u índice de hoja
- `header` - fila de encabezados
- `index_col` - columna como índice
- `na_values` - valores a tratar como NA

---

## Lectura desde JSON

```python
# Reading JSON desde URL
pd.read_json('https://api.github.com/repos/pydata/pandas/issues?per_page=5')
```

**ORIENTACIONES JSON:**
- `'records'` - lista de objetos
- `'index'` - índice como keys
- `'columns'` - columnas como keys
- `'split'` - diccionario con índice, columnas, datos

---

## Web Scraping con Pandas

```python
import pandas as pd

# Leer tablas de página web
densidad_paises = pd.read_html('https://simple.wikipedia.org/wiki/List_of_countries_by_population_density', header=0)

# Es devuelve una LISTA de DataFrames (una por tabla)
type(densidad_paises)  # list

# Acceder a la primera tabla
densidad_paises[0][:10]
```

**CONCEPTO EXPLÍCITO:**
`read_html` devuelve una lista porque una página puede tener múltiples tablas.

### Limpieza de Datos después de Web Scraping

```python
# Copia para no modificar original
densidad_paises_clean = densidad_paises_dataframe.copy()

# Eliminar columna innecesaria
densidad_paises_clean.pop('Unnamed: 1')

# Ver el resultado
densidad_paises_clean.head()
```

---

# Regex - Expresiones Regulares

## 🎯 Objetivos

- Entender patrones de regex
- Buscar y modificar texto
- Validar formatos

---

## Patrones Básicos

| Patrón | Significado |
|--------|-------------|
| `.` | Cualquier carácter excepto nueva línea |
| `\n` | Nueva línea |
| `\r` | Retorno de carro |
| `\t` | Tabulador |
| `\w` | caracterer alfanumérico (a-z, A-Z, 0-9, _) |
| `\W` | NO alfanumérico |
| `\s` | Espacio en blanco |
| `\S` | NO espacio |
| `\d` | Dígito (0-9) |
| `\D` | NO dígito |
| `^` | Inicio de cadena |
| `$` | Fin de cadena |
| `\` | Escape |
| `[]` | Rango de caracteres |
| `^` (dentro de corchetes) | Negación |
| `\b` | Separación entre palabras |

---

## Metacaracteres de Repetición

| Metacarácter | Significado |
|-------------|------------|
| `+` | Una o más veces |
| `*` | Cero o más veces |
| `?` | Cero o una vez |
| `{n}` | Exactamente n veces |
| `{n,}` | n o más veces |
| `{n,m}` | Entre n y m veces |

---

## Búsquedas

```python
import re

# Busca primera coincidencia
my_regex = re.search(r"o", "Hacker School")
my_regex.group()  # 'o'
```

### Buscar números de 3 dígitos

```python
# \d\d\d = cualquier posición con tres números seguidos
print(re.search(r"\d\d\d", "Monterrey539NuevoLeon").group())  # 539
print(re.search(r"\d\d\d", "823avenidadelestadO").group())  # 823
print(re.search(r"\d\d\d", "tamauli412pas").group())           # 412
```

### Compilar regex para reutilizar

```python
# Buena práctica: compilar si se usa muchas veces
patron_regex = re.compile(r"\d\d\d")

print(patron_regex.search("Monterrey539NuevoLeon"))
print(patron_regex.search("823avenidadelestadO"))
print(patron_regex.search("tamauli412pas"))
```

---

## Manejo de Errores

```python
# Si no hay coincidencia, devuelve None
regex_none = re.search(r"\d\d\d", "7jalisco41")

if regex_none is None:
    print("No existen coincidencias")
```

**ERROR COMÚN:**
```python
# ESTO DA ERROR si no hay coincidencia:
try:
    regex_none = re.search(r"\d\d\d", "7jalisco41").group()
except:
    print("No existen coincidencias")
```

---

## Agrupamiento (Groups)

```python
# Patrón: (\d+)-([A-Za-z]+)
# Grupo 1: números antes del guión
# Grupo 2: letras después del guión
regex_con_grupo = re.compile(r"(\d+)-([A-Za-z]+)")

m = regex_con_grupo.search("23081-yttTa")

print(m.group(1), m.group(2))  # 23081 yttTa
print(m.group())                # 23081-yttTa (todo)

# En cadena larga
m = regex_con_grupo.search("syasdhasdhasdasdaaanHUHYYHy7823e23e230daaaaa81-yttTa*****")
print(m.group(1), m.group(2))  # 81 yttTa
```

---

## Inicio y Fin de Cadena

```python
# ^ = inicio, $ = fin
re.search(r"^monterrey$", "monterrey")  # Encuentra

re.search(r"^monterrey$", "meridamonterreymerida")  # NO encuentra (hay texto antes y después)
```

---

## findall - Todas las coincidencias

```python
# Devuelve lista de TODAS las coincidencias
re.findall(r"\d{3}", "523qwerty72ghjkl713")  # ['523', '713']
```

---

## Sustituciones (sub)

```python
# Reemplazar todos los dígitos por guiones
re.sub(r"\d", "-", "23asdfghjkl231")  # '--asdfghjkl---'

# Reemplazar solo los primeros n
re.sub(r"\d", "-", "23asdfghjkl231", 3)  # '--asdfghjkl-31'

#替换 caracteres especiales
re.sub(r"ñ", "n", "niños")  # 'ninos'
```

---

# Web Scraping - BeautifulSoup4

## 🎯 Objetivos

- Entender la estructura HTML
- Extraer datos de páginas web
- Automatizar recopilación de datos

---

## DOM (Document Object Model)

**CONCEPTO EXPLÍCITO:**
El DOM es una representación en árbol de la página web. Cada etiqueta HTML es un "nodo" en el árbol.

```
<html>
  <head>
    <title>Título</title>
  </head>
  <body>
    <div>
      <p>Párrafo 1</p>
      <p>Párrafo 2</p>
    </div>
  </body>
</html>
```

---

## Obteniendo una página web

```python
from bs4 import BeautifulSoup
import requests

URL = 'http://nostarch.com'
soup = BeautifulSoup(requests.get(URL).text, "lxml")
```

**CONCEPTO EXPLÍCITO:**
1. `requests.get()` descarga la página
2. `.text` obtiene el HTML como texto
3. `BeautifulSoup()` parsea el HTML

---

## Navegando el DOM

```python
# Obtener título
soup.title              # <title>No Starch Press</title>
soup.title.name        # 'title'
soup.title.string       # 'No Starch Press'
soup.title.parent.name # 'head'

# Primer párrafo
soup.p                 # <p>...</p>

# Buscar todos los elementos de un tipo
soup.find_all('p')     # Lista de todos los <p>
soup.find_all('a')     # Lista de todos los <a>
```

---

## Selección por Clase

```python
# Buscar por clase CSS
lista = soup.find_all('div', class_='product-body')

# Extraer texto y atributos
lista[0].a.get_text()              # Texto del enlace
lista[0].a["href"]                 # URL del enlace
```

---

## Exportar a DataFrame

```python
import pandas

# Crear diccionario
resultado_dic = {}

for element in lista:
    resultado_dic[str(element.a.get_text())] = element.a["href"]

# Convertir a DataFrame
resutado_dataframe = pandas.DataFrame.from_dict(resultado_dic, orient='index')

# Renombrar columnas
resutado_dataframe.rename(columns={0: 'URL'}, inplace=True)

resutado_dataframe.head()
```

---

## Selección por Herencia DOM

```python
URL = 'https://news.ycombinator.com/news'
soup = BeautifulSoup(requests.get(URL).text, "lxml")

# Selector CSS: tr > td > a
a_list = soup.select('tr > td > a[href*="."]')
```

**CONCEPTO EXPLÍCITO:**
Los selectores CSS permiten navegar la jerarquía:
- `>` = hijo directo
- ` ` = descendiente
- `[attr]` = con atributo

---

# Tidy Data

## 🎯 Objetivos

- Entender qué es "tidy data"
- Transformar datos ancho a largo y viceversa
- Usar melt y pivot

---

## El Concepto de Tidy Data

**CONCEPTO EXPLÍCITO:**
Datos "ordenados" siguen estas reglas:
1. Cada variable es una columna
2. Cada observación es una fila
3. Cada valor es una celda

### Ejemplo de datos "untidy" (ancho)

```python
import pandas as pd

pacientes = ['Ricardo', 'Marielena', 'Miguel']
a = [67, 80, 64]
b = [56, 90, 50]

untidy = pd.DataFrame({'pacientes': pacientes, 'a': a, 'b': b})
```

Aquói, 'a' y 'b' son columnas pero deberían ser valores de una columna 'drug'.

### Transformar con melt (gather)

```python
def gather(df, key, value, cols):
    id_vars = [col for col in df.columns if col not in cols]
    id_values = cols
    var_name = key
    value_name = value
    return pd.melt(df, id_vars, id_values, var_name, value_name)

tidy = gather(untidy, 'drug', 'heartrate', ['a', 'b'])
```

**CONCEPTO EXPLÍCITO:**
- `melt()` convierte datos "anchos" a "largos"
- `pivot()` convierte datos "largos" a "anchos"

### Resultado (tidy)

| pacientes | drug | heartrate |
|-----------|------|----------|
| Ricardo | a | 67 |
| Marielena | a | 80 |
| Miguel | a | 64 |
| Ricardo | b | 56 |
| Marielena | b | 90 |
| Miguel | b | 50 |

---

## Referencias

- https://garrettgman.github.io/tidying/
- https://tomaugspurger.github.io/modern-5-tidy.html
- https://www.ibm.com/developerworks/community/blogs/jfp/entry/Tidy_Data_In_Python

---

# SQL para Data Science

## 🎯 Objetivos

- Comprender consultas SQL básicas
- Realizar JOINs entre tablas
- Usar funciones de agregación
- Integrar SQL con Python y Pandas

---

## ¿Por qué SQL en Data Science?

```
┌─────────────────────────────────────────────────────────────┐
│             SQL = EXCEL CON SUPERPODERES                     │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  INTERFAZ GRÁFICA          │  CONSULTA SQL                 │
│  ─────────────            │  ────────────                  │
│  Click en celdas          │  Escribir query               │
│  Filtros manuales         │  WHERE, LIKE                   │
│  Gráficos lentos          │  GROUP BY rápido              │
│  10K filas               │  10M+ filas instantáneo      │
│                                                             │
│  Ventaja: Intuitivo       │  Ventaja: Escalable           │
└─────────────────────────────────────────────────────────────┘
```

**CONCEPTO EXPLÍCITO:**
SQL es el lenguaje universal para trabajar con datos. Aunque uses Pandas, entender SQL te ayuda a pensar en términos de conjuntos.

---

## Estructura de una Tabla

```python
import sqlite3
import pandas as pd

# Crear base de datos en memoria
conn = sqlite3.connect(':memory:')

# Crear tabla
conn.execute('''
    CREATE TABLE usuarios (
        id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        email TEXT UNIQUE,
        edad INTEGER,
        ciudad TEXT
    )
''')

# Insertar datos
datos = [
    (1, 'Ana', 'ana@email.com', 25, 'CDMX'),
    (2, 'Carlos', 'carlos@email.com', 30, 'GDL'),
    (3, 'María', 'maria@email.com', 28, 'MTY'),
    (4, 'Juan', 'juan@email.com', 35, 'CDMX'),
]
conn.executemany('INSERT INTO usuarios VALUES (?,?,?,?,?)', datos)
conn.commit()

# Ver datos
df = pd.read_sql('SELECT * FROM usuarios', conn)
print(df)
```

---

## Consultas Básicas

```python
# SELECT - Elegir columnas
df = pd.read_sql('SELECT nombre, edad FROM usuarios', conn)
print(df)

# WHERE - Filtrar condiciones
df = pd.read_sql('SELECT * FROM usuarios WHERE ciudad = "CDMX"', conn)
print(df)

# ORDER BY - Ordenar
df = pd.read_sql('SELECT * FROM usuarios ORDER BY edad DESC', conn)
print(df)
```

---

## Funciones de Agregación

```python
# Agregar tabla de ventas
conn.execute('''
    CREATE TABLE ventas (
        id INTEGER PRIMARY KEY,
        producto TEXT,
        cantidad INTEGER,
        precio REAL
    )
''')

ventas = [
    (1, 'Laptop', 2, 15000),
    (2, 'Mouse', 5, 250),
    (3, 'Teclado', 3, 800),
    (4, 'Laptop', 1, 15000),
    (5, 'Monitor', 2, 5000),
]
conn.executemany('INSERT INTO ventas VALUES (?,?,?,?)', ventas)
conn.commit()

# COUNT - Contar
df = pd.read_sql('SELECT COUNT(*) as total FROM ventas', conn)
print(df)

# SUM - Sumar
df = pd.read_sql('SELECT SUM(cantidad) as total FROM ventas', conn)
print(df)

# GROUP BY - Agrupar
df = pd.read_sql('''
    SELECT producto, SUM(cantidad) as total 
    FROM ventas 
    GROUP BY producto
    ORDER BY total DESC
''', conn)
print(df)
```

---

## JOINs - Combinar Tablas

```python
# Crear tabla de categorías
conn.execute('''
    CREATE TABLE categorias (
        id INTEGER PRIMARY KEY,
        nombre TEXT
    )
''')
cats = [(1, 'Electrónica'), (2, 'Accesorios')]
conn.executemany('INSERT INTO categorias VALUES (?,?)', cats)
conn.commit()

# INNER JOIN
df = pd.read_sql('''
    SELECT v.producto, c.nombre as categoria, v.precio
    FROM ventas v
    INNER JOIN categorias c ON v.id = c.id
''', conn)
print(df)

conn.close()
```

### Tipos de JOIN

| Tipo | Descripción |
|------|------------|
| INNER | Solo filas con coincidencia en ambas |
| LEFT | Todas las de izquierda, con null si no hay coincidencia |
| RIGHT | Todas las de derecha, con null si no hay coincidencia |
| FULL | Todas las filas de ambas |
| CROSS | Producto cartesiano |

---

## Resumen de Comandos SQL

| Comando | Descripción | Ejemplo |
|---------|------------|--------|
| SELECT | Elegir columnas | SELECT nombre, edad |
| FROM | De dónde vienen | FROM usuarios |
| WHERE | Filtrar | WHERE ciudad='CDMX' |
| ORDER BY | Ordenar | ORDER BY edad DESC |
| GROUP BY | Agrupar | GROUP BY ciudad |
| JOIN | Combinar | INNER JOIN tablas |
| HAVING | Filtrar grupos | HAVING COUNT(*) > 1 |
| LIMIT | Limitar resultados | LIMIT 10 |

---

## 📝 Ejercicios

```python
# Ejercicio: Crear tu propia base de datos
conn = sqlite3.connect('mi_tienda.db')

# Crear tabla de productos
conn.execute('''
    CREATE TABLE productos (
        id INTEGER PRIMARY KEY,
        nombre TEXT,
        categoria TEXT,
        precio REAL
    )
''')

# Insertar productos
productos = [
    ('Laptop', 'Electrónica', 15000),
    ('Mouse', 'Accesorios', 250),
    ('Teclado', 'Accesorios', 800)
]
conn.executemany('INSERT INTO productos (nombre, categoria, precio) VALUES (?,?,?)', productos)
conn.commit()

# Consultar
df = pd.read_sql('SELECT * FROM productos', conn)
print(df)

conn.close()
```

---

# Introducción al Ecosistema SciPy

## 🎯 Objetivos

- Conocer el ecosistema SciPy completo
- Entender cuándo usar cada librería
- Realizar cómputo científico básico

---

## Entorno de Cómputo Científico

Un típico entorno de cómputo científico incluye:
- **Optimización** - scipy.optimize
- **Visualización** - matplotlib
- **Análisis de datos** - pandas, numpy
- **Cálculo simbólico** - sympy
- **Bases de datos** - sqlalchemy
- **Extensiones especializadas** - scikits

---

## NumPy (reforzando)

NumPy provee el array n-dimensional que es la base de todo el ecosistema.

```python
import numpy as np
np.arange(10)  # array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
```

**POR QUÉ ES IMPORTANTE:**
- Implementado en C - muchMore rápido que Python puro
- Memoria contigua - cache-friendly
- Operaciones vectorizadas

### Comparación de velocidad

```python
a_pythonic = list(range(10000))
%timeit [v ** 2 for v in a_pythonic]
# Resultado: ~4ms por loop

b_numpy = np.array(a_pythonic)
%timeit b_numpy ** 2
# Resultado: ~8μs por loop (500x más rápido)
```

### Array Indexing

```python
x = np.arange(100).reshape(5, 20)

# Simple indexing
print(x[2])           # Fila 2

# Slicing
print(x[2:5])         # Filas 2 a 4

# Boolean indexing
print(x[(x % 2) == 0])  # Solo pares

# Fancy indexing
print(x[[1, 4, 2]])   # Filas 1, 4, 2 en ese orden
```

---

## Polinomios

```python
from numpy.polynomial import Polynomial as P

# p(x) = 1 + 2x + 3x^2
polinomio = P([1, 2, 3])
print(polinomio)

# Operaciones
print(polinomio + polinomio)  # Suma
print(polinomio - polinomio)  # Resta
```

---

## Matplotlib

Matplotlib es la librería de visualización estándar.

```python
import matplotlib.pyplot as plt

plt.plot([1, 5, 3])
plt.show()
```

**CONCEPTO EXPLÍCITO:**
- Amigable y no obstructivo
- Control detallado
- Gran variedad de estilos

---

## SciPy

SciPy va más allá de NumPy con algoritmos especializados.

```python
from scipy import constants
import pint
ureg = pint.UnitRegistry()

m = 10 * ureg.kg
c = constants.c * ureg.meters / ureg.second
E = m * c ** 2
print(E)
# Resultado: 8.987551787368177e+17 kilogram * meter ** 2 / second ** 2
```

### Módulos de SciPy

| Módulo | Descripción |
|--------|------------|
| `scipy.constants` | Constantes físicas |
| `scipy.cluster` | Agrupamiento (clustering) |
| `scipy.fftpack` | Transformada de Fourier |
| `scipy.integrate` | Integración |
| `scipy.interpolate` | Interpolación |
| `scipy.optimize` | Optimización |
| `scipy.stats` | Estadísticas |

### Interpolación

```python
from scipy import interpolate

x, y = np.linspace(-5, 5, 25), np.linspace(-5, 5, 25)
xx, yy = np.meshgrid(x, y)
z = np.sin(xx**2 + yy**2)
f_rect = interpolate.RectBivariateSpline(x, y, z)

xnew, ynew = np.linspace(-4.5, 4.5, 1000), np.linspace(-4.5, 4.5, 1000)
znew = f_rect(xnew, ynew)
```

---

## Referencias

- [NumPy Docs](https://numpy.org/doc/)
- [SciPy Docs](https://docs.scipy.org/doc/scipy/)
- [Matplotlib Gallery](https://matplotlib.org/stable/gallery/index.html)

---

*Apuntes generados para estudio - Scientific Python Stack y Big Data Engineering*