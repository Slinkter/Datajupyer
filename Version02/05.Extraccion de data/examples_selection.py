import pandas as pd

# 1. Crear un DataFrame de ejemplo
data = {
    'nombre': ['Ana', 'Luis', 'Marta'],
    'edad': [25, 30, 22],
    'ciudad': ['Madrid', 'Barcelona', 'Sevilla'],
    'salario': [30000, 45000, 28000]
}
df = pd.DataFrame(data)

print("--- DataFrame Original ---")
print(df)
print("\n")

# ---------------------------------------------------------
# Ejemplo 1: Diferencia entre Serie (1 corchete) y DataFrame (2 corchetes)
# ---------------------------------------------------------
serie = df['edad']
dataframe_una_columna = df[['edad']]

print("1. df['edad'] es tipo:", type(serie))
print("   Se ve así (sin encabezado de tabla):")
print(serie)
print("\n")

print("2. df[['edad']] es tipo:", type(dataframe_una_columna))
print("   Se ve así (con formato de tabla):")
print(dataframe_una_columna)
print("\n")

# ---------------------------------------------------------
# Ejemplo 2: Reordenar columnas
# ---------------------------------------------------------
# El orden en la lista determina el orden en el resultado
# Aquí ponemos 'ciudad' primero, aunque en el original estaba al final
df_reordenado = df[['ciudad', 'nombre', 'edad']]
print("--- Ejemplo 2: Columnas reordenadas (ciudad primero) ---")
print(df_reordenado)
print("\n")

# ---------------------------------------------------------
# Ejemplo 3: Usar una variable para la lista
# ---------------------------------------------------------
# Esto es muy útil en scripts profesionales para mantener el código limpio
columnas_deseadas = ['nombre', 'salario']
df_seleccion = df[columnas_deseadas]

print("--- Ejemplo 3: Usando una variable lista ---")
print(df_seleccion)
print("\n")

# ---------------------------------------------------------
# Ejemplo 4: Duplicar columnas (Curiosidad)
# ---------------------------------------------------------
# Pandas permite seleccionar la misma columna varias veces si lo necesitas
df_duplicado = df[['nombre', 'salario', 'salario']]
print("--- Ejemplo 4: Seleccionar la misma columna dos veces ---")
print(df_duplicado)