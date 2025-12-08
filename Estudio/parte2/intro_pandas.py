
import pandas as pd
import numpy as np

# ==========================================
# 1. Conceptos Principales (Estructuras de Datos)
# ==========================================

# A. Series: Array unidimensional etiquetado (como una columna de Excel o un array con nombres)
serie_ejemplo = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
print("--- Serie Ejemplo ---")
print(serie_ejemplo)

# B. DataFrame: Estructura tabular bidimensional (como una hoja de cálculo completa o tabla SQL)
datos = {
    'Nombre': ['Ana', 'Luis', 'Carlos', 'Sofia'],
    'Edad': [25, 30, 22, 28],
    'Ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Sevilla'],
    'Salario': [30000, 45000, 28000, 52000]
}
df = pd.DataFrame(datos)
print("\n--- DataFrame Ejemplo ---")
print(df)

# ==========================================
# 2. Funciones Más Usadas (CRUD y Exploración)
# ==========================================

# --- Exploración Inicial ---
print("\n--- Exploración ---")
print("df.head(2):") # Ver las primeras 2 filas
print(df.head(2))
print("\ndf.info():") # Resumen técnico (tipos de datos, nulos)
df.info()
print("\ndf.describe():") # Resumen estadístico (media, min, max, cuartiles)
print(df.describe())

# --- Selección y Filtrado ---
print("\n--- Selección ---")
# Selección de columna
print("Columna 'Edad':", df['Edad'].tolist())

# Filtrado (Boolean Indexing)
filtro_edad = df[df['Edad'] > 25]
print("\nMayores de 25 años:")
print(filtro_edad)

# Selección por etiquetas (loc) y posición (iloc)
print("\nFila de índice 1 (Luis) usando .loc:") # Nota: en este df el índice es numérico por defecto
print(df.loc[1]) 

# --- Manipulación ---
print("\n--- Manipulación ---")
# Crear nueva columna calculada
df['Salario_Mensual'] = df['Salario'] / 12

# Ordenar
df_ordenado = df.sort_values(by='Edad', ascending=False)
print("Ordenado por Edad descendente:")
print(df_ordenado)

# Agrupación (GroupBy) - Muy potente
print("\nPromedio de salario por Ciudad (Ejemplo simple):")
# Agregamos una fila extra para que el grupo tenga sentido
df.loc[4] = ['Pedro', 35, 'Madrid', 40000, 3333.33] 
print(df.groupby('Ciudad')['Salario'].mean())

# ==========================================
# 3. Conceptos Indispensables & Trucos
# ==========================================
# - Vectorización: Operar sobre columnas completas sin bucles for (ej: df['A'] + df['B']). Es C rápido.
# - El Índice (Index): Es la clave para búsquedas rápidas. df.set_index('ID') hace que buscar por ID sea O(1).
# - Missing Data (NaN): Pandas tiene métodos robustos para manejar datos faltantes: dropna(), fillna().

# Truco: "Chaining" (Encadenamiento de métodos)
# Permite leer código como una historia paso a paso
resultado = (
    df
    .assign(Edad_en_10_anos = lambda x: x['Edad'] + 10) # Crear columna al vuelo
    .query('Edad > 25')                                 # Filtrar estilo SQL
    .sort_values('Salario', ascending=False)            # Ordenar
)
print("\n--- Resultado con Method Chaining ---")
print(resultado)

