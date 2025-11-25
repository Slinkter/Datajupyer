# Módulo 3: Análisis Exploratorio de Datos y Estadística

---

## 1. Introducción del Módulo

Con las herramientas para la manipulación de datos ya dominadas, este módulo se adentra en el primer paso fundamental de cualquier proyecto de ciencia de datos: el **Análisis Exploratorio de Datos (EDA)**. El EDA es tanto una ciencia como un arte; es el proceso de "dialogar" con los datos para entender sus principales características, descubrir patrones, identificar anomalías y formular hipótesis.

Este módulo establece los cimientos estadísticos y probabilísticos necesarios para realizar un EDA robusto. Se abordarán desde las medidas de estadística descriptiva más básicas hasta los conceptos de distribuciones de probabilidad. Luego, se presentará un marco de trabajo sistemático para explorar conjuntos de datos, combinando el rigor estadístico con el poder de la visualización. El objetivo final es aprender a extraer *insights* y a contar la historia que se esconde dentro de los datos.

---

## 2. Objetivos Pedagógicos

Al finalizar este módulo, el estudiante será capaz de:

-   **Calcular e Interpretar Estadísticas Descriptivas:** Utilizar medidas de tendencia central (media, mediana) y de dispersión (desviación estándar, varianza, cuantiles) para resumir conjuntos de datos.
-   **Aplicar Conceptos Fundamentales de Probabilidad:** Entender los principios de la probabilidad, las distribuciones más comunes (Normal, Binomial) y su relevancia en la inferencia estadística.
-   **Realizar un Análisis Exploratorio de Datos (EDA) Sistemático:** Ejecutar un flujo de trabajo de EDA, incluyendo análisis univariado, bivariado y multivariado.
-   **Crear Visualizaciones para el Descubrimiento:** Emplear librerías como Matplotlib y Seaborn para crear visualizaciones (histogramas, box plots, scatter plots, heatmaps) que revelen la estructura y las relaciones en los datos.
-   **Formular y Validar Hipótesis Iniciales:** Utilizar los hallazgos del EDA para generar preguntas de investigación y guiar los siguientes pasos en un proyecto de modelado.

---

## 3. Temas Tratados

### Sesión 1: Fundamentos de Probabilidad y Estadística Descriptiva
-   **Estadística Descriptiva:**
    -   **Medidas de Tendencia Central:**
        -   **Media:** El promedio. Sensible a outliers.
        -   **Mediana:** El valor central. Robusta frente a outliers.
        -   **Moda:** El valor más frecuente.
    -   **Medidas de Dispersión:**
        -   **Rango:** Diferencia entre el máximo y el mínimo.
        -   **Varianza ($\sigma^2$):** El promedio de las diferencias al cuadrado con la media.
        -   **Desviación Estándar ($\sigma$):** La raíz cuadrada de la varianza. Interpretable en las unidades originales.
        -   **Cuantiles, Percentiles y Rango Intercuartílico (IQR):** Medidas robustas para describir la dispersión.
-   **Probabilidad Básica:**
    -   Espacio muestral, eventos, probabilidad condicional.
    -   Teorema de Bayes: La base de la inferencia bayesiana.
-   **Distribuciones de Probabilidad:**
    -   **Distribución Normal (Gaussiana):** La distribución más importante en estadística.
    -   **Distribuciones Discretas:** Binomial, Poisson.

### Sesión 2: Metodología del Análisis Exploratorio de Datos (EDA)
-   **El Proceso de EDA:** Un ciclo iterativo de preguntas, visualización, transformación y repetición.
-   **Análisis Univariado:**
    -   **Variables Numéricas:** Histogramas, KDE plots, y box plots para entender la distribución.
    -   **Variables Categóricas:** Gráficos de barras (`countplot`) para entender las frecuencias.
-   **Análisis Bivariado:**
    -   **Numérica vs. Numérica:** `scatter plots` para visualizar relaciones y `correlation matrices` (heatmaps) para cuantificarlas.
    -   **Numérica vs. Categórica:** Box plots o violin plots para comparar distribuciones entre categorías.
    -   **Categórica vs. Categórica:** Tablas de contingencia (`pd.crosstab`) y gráficos de barras agrupados.
-   **Visualización con Seaborn:** Aprovechar la sintaxis de alto nivel de Seaborn para crear gráficos estadísticos complejos y estéticamente agradables de forma rápida.

### Sesión 3: Práctica de Análisis Exploratorio
-   **Estudio de Caso (End-to-End):**
    -   Se utiliza un conjunto de datos completo (e.g., el `train.csv` del Titanic).
    -   **Paso 1: Carga y Limpieza Inicial:** Cargar los datos, revisar tipos de datos, manejar valores faltantes.
    -   **Paso 2: Análisis Descriptivo y Univariado:** Calcular estadísticas clave y visualizar la distribución de cada variable importante.
    -   **Paso 3: Análisis Bivariado y Multivariado:** Explorar relaciones entre pares de variables (e.g., ¿cómo se relaciona la clase del ticket con la supervivencia?) y usar facetas para incluir una tercera dimensión.
    -   **Paso 4: Formulación de Insights:** Resumir los hallazgos en conclusiones claras y accionables. Por ejemplo: "Los pasajeros de primera clase tuvieron una tasa de supervivencia significativamente mayor".

---

## 4. Ejemplos y Notas del Profesor

### Nota sobre Media vs. Mediana
La elección entre la media y la mediana como medida de tendencia central depende de la distribución de tus datos.
-   Para **distribuciones simétricas** (como la normal), la media y la mediana son aproximadamente iguales. La media es generalmente preferida porque utiliza toda la información del conjunto de datos.
-   Para **distribuciones asimétricas (sesgadas)** o con **outliers significativos**, la mediana es una mejor representante del "valor típico", ya que no se ve afectada por los valores extremos.

**Insight:** Siempre visualiza tus datos (e.g., con un histograma) antes de decidir qué estadística descriptiva es la más apropiada. En el análisis de salarios, por ejemplo, siempre se reporta la mediana, ya que unos pocos salarios extremadamente altos sesgarían la media hacia arriba.

### La Matriz de Correlación: Una Herramienta Poderosa y Peligrosa
Una matriz de correlación, visualizada como un heatmap, es una de las herramientas más comunes en EDA. Sin embargo, debe interpretarse con cuidado.

```python
import seaborn as sns
import numpy as np
import pandas as pd

# Crear datos de ejemplo
np.random.seed(42)
data = {
    'Temperatura': np.random.normal(25, 5, 100),
    'Venta_Helados': np.random.normal(100, 20, 100),
    'Venta_Bufandas': np.random.normal(10, 3, 100)
}
df = pd.DataFrame(data)
df['Venta_Helados'] += (df['Temperatura'] - 25) * 4 # Añadir correlación positiva
df['Venta_Bufandas'] -= (df['Temperatura'] - 25) * 2 # Añadir correlación negativa

# Calcular y visualizar la matriz de correlación
corr_matrix = df.corr()
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Matriz de Correlación")
plt.show()
```
**Insight:** La correlación (de Pearson, por defecto) solo mide la **relación lineal** entre variables.
-   Una correlación de `+0.9` indica una fuerte relación lineal positiva.
-   Una correlación de `-0.8` indica una fuerte relación lineal negativa.
-   Una correlación de `0.0` indica **ausencia de relación lineal**, pero **no ausencia de relación**. Una relación cuadrática (e.g., en forma de 'U') podría tener una correlación de cero y aun así ser una relación muy fuerte y predecible. **¡Correlación no implica causalidad!**

---

## 5. Fuentes y Referencias

-   **Libro "Think Stats: Exploratory Data Analysis in Python" de Allen B. Downey:** Un excelente recurso gratuito.
-   **Galería de ejemplos de Seaborn:** [https://seaborn.pydata.org/examples/index.html](https://seaborn.pydata.org/examples/index.html)
-   **Documentación de `scipy.stats`:** [https://docs.scipy.org/doc/scipy/reference/stats.html](https://docs.scipy.org/doc/scipy/reference/stats.html)

---
