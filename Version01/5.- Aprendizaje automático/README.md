# Módulo 5: Aprendizaje Automático

---

## 1. Introducción del Módulo

Este módulo constituye el núcleo predictivo de la ciencia de datos. Habiendo aprendido a adquirir, limpiar y transformar datos, ahora nos enfocamos en el **Aprendizaje Automático (Machine Learning)**, la disciplina que nos permite construir sistemas que aprenden patrones a partir de los datos para hacer predicciones sobre nueva información.

Se introducirá el marco conceptual del aprendizaje automático, distinguiendo entre tareas de regresión y clasificación. Los estudiantes aprenderán el flujo de trabajo estándar utilizando la librería `scikit-learn`, desde el entrenamiento de un modelo hasta su evaluación y ajuste. Se explorarán diversos algoritmos, desde los modelos lineales más simples hasta los métodos de ensamble más complejos y potentes. El módulo culmina con la aplicación de estas técnicas en un estudio de caso práctico: la construcción de un modelo de scoring de crédito.

---

## 2. Objetivos Pedagógicos

Al finalizar este módulo, el estudiante será capaz de:

-   **Comprender el Flujo de Trabajo del Machine Learning:** Implementar el ciclo completo de modelado: división de datos (train/test), entrenamiento (`fit`), predicción (`predict`) y evaluación.
-   **Aplicar y Evaluar Modelos de Regresión y Clasificación:** Entrenar diferentes algoritmos (Regresión Lineal, Regresión Logística, Naive Bayes, Árboles de Decisión, etc.) y entender sus fortalezas y debilidades.
-   **Diagnosticar y Mitigar el Sobreajuste (Overfitting):** Comprender el tradeoff entre sesgo y varianza (Bias-Variance) y utilizar técnicas como la validación cruzada para construir modelos más generalizables.
-   **Optimizar el Rendimiento del Modelo:** Realizar búsquedas de hiperparámetros (`GridSearchCV`) para encontrar la mejor configuración para un modelo.
-   **Utilizar Métodos de Ensamble:** Implementar técnicas de Bagging (Random Forests) y Boosting para mejorar la robustez y precisión de las predicciones.
-   **Interpretar los Resultados del Modelo:** Analizar las métricas de evaluación (Accuracy, Precision, Recall, F1-Score, ROC-AUC) y los coeficientes o importancias de las features para entender el comportamiento del modelo.

---

## 3. Temas Tratados

### Sesión 1: Fundamentos del Aprendizaje Automático
-   **Introducción Conceptual:**
    -   Tipos de Aprendizaje: Supervisado (Regresión, Clasificación), No Supervisado (Clustering).
    -   El ecosistema `scikit-learn`: consistencia de la API (`estimator`).
-   **El Primer Modelo: Regresión Lineal:**
    -   Intuición y formulación matemática.
    -   Implementación con `sklearn.linear_model.LinearRegression`.
    -   **Métricas de Evaluación:** Mean Squared Error (MSE), Root Mean Squared Error (RMSE), R-cuadrado ($R^2$).
-   **El Primer Modelo de Clasificación: Regresión Logística:**
    -   La función sigmoide para mapear a probabilidades.
    -   **Métricas de Evaluación para Clasificación:**
        -   Accuracy (Exactitud): Cuándo puede ser engañosa.
        -   Matriz de Confusión: Verdaderos Positivos, Falsos Positivos, etc.
        -   Precision, Recall y F1-Score.
-   **Validación de Modelos:**
    -   La necesidad de separar los datos: `train_test_split`.

### Sesión 2: Modelos Avanzados y Validación Robusta
-   **Otros Algoritmos de Clasificación:**
    -   **Naive Bayes:** Basado en el teorema de Bayes, muy eficiente para texto.
    -   **k-Nearest Neighbors (k-NN):** Un modelo no paramétrico basado en instancia.
    -   **Support Vector Machines (SVM):** Modelos basados en la maximización de márgenes.
    -   **Árboles de Decisión:** Modelos interpretables basados en reglas.
-   **El Tradeoff entre Sesgo y Varianza:**
    -   **Underfitting (Alto Sesgo):** El modelo es demasiado simple.
    -   **Overfitting (Alta Varianza):** El modelo memoriza el ruido del entrenamiento.
-   **Validación Cruzada (Cross-Validation):**
    -   Técnica para una evaluación más robusta del rendimiento del modelo.
-   **Búsqueda de Hiperparámetros:**
    -   `GridSearchCV` para encontrar la combinación óptima de parámetros.

### Sesión Sábado: Métodos de Ensamble y Caso Práctico
-   **Métodos de Ensamble: La Sabiduría de la Multitud:**
    -   **Bootstrap Aggregating (Bagging):**
        -   El método de remuestreo **Bootstrap**.
        -   **Random Forests:** Un ensamble de árboles de decisión que reduce la varianza.
    -   **Boosting:**
        -   Modelos que aprenden secuencialmente de los errores de los predecesores.
        -   AdaBoost, Gradient Boosting Machines (GBM).
-   **Estudio de Caso: Scorecard de Crédito (German Credit Dataset):**
    -   Aplicación completa del pipeline de Machine Learning.
    -   Preprocesamiento de datos y Feature Engineering.
    -   Entrenamiento de múltiples modelos (e.g., Regresión Logística, Random Forest).
    -   Evaluación y selección del mejor modelo usando métricas de negocio relevantes (e.g., impacto de los falsos negativos).
    -   Interpretación del modelo final para derivar una "tarjeta de puntuación".

---

## 4. Ejemplos y Notas del Profesor

### Nota sobre la Trampa de la Exactitud (Accuracy Trap)
En problemas con **clases desbalanceadas** (e.g., detección de fraude, diagnóstico de enfermedades raras), la exactitud (accuracy) es una métrica terrible. Un modelo que siempre predice "no hay fraude" en un dataset con 99% de transacciones legítimas tendrá un 99% de accuracy, pero será completamente inútil.

**Insight:** En estos casos, enfócate en **Precision**, **Recall** y la **Curva ROC-AUC**.
-   **Precision:** De todas las veces que el modelo predijo "Positivo", ¿cuántas acertó? (Minimiza Falsos Positivos).
-   **Recall (Sensibilidad):** De todos los casos que eran realmente "Positivo", ¿cuántos encontró el modelo? (Minimiza Falsos Negativos).
-   **Curva ROC y AUC:** Mide el rendimiento del clasificador a través de todos los umbrales de clasificación. Un AUC de 0.5 es un modelo aleatorio, mientras que 1.0 es un modelo perfecto.

### El Pipeline de Scikit-learn
Para evitar el *data leakage* y simplificar el flujo de trabajo, `scikit-learn` ofrece el objeto `Pipeline`. Un `Pipeline` encadena múltiples pasos de preprocesamiento y un estimador final.

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import SelectKBest
from sklearn.svm import SVC

# Se crea un pipeline que:
# 1. Escala los datos.
# 2. Selecciona las 5 mejores features.
# 3. Entrena un clasificador SVM.
pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('selector', SelectKBest(k=5)),
    ('classifier', SVC(kernel='rbf'))
])

# Ahora podemos usar el pipeline como si fuera un único estimador
pipe.fit(X_train, y_train)
predictions = pipe.predict(X_test)

# ¡GridSearchCV puede incluso buscar en los parámetros del pipeline!
param_grid = {
    'selector__k': [3, 5, 10],
    'classifier__C': [0.1, 1, 10]
}
grid = GridSearchCV(pipe, param_grid, cv=5)
grid.fit(X_train, y_train)
print(grid.best_params_)
```
**Insight:** El uso de `Pipeline` es una mejor práctica profesional. Hace que tu código sea más limpio, menos propenso a errores y más fácil de desplegar.

---

## 5. Fuentes y Referencias

-   **Documentación de Scikit-learn:** [https://scikit-learn.org/stable/](https://scikit-learn.org/stable/)
-   **Libro "Introduction to Machine Learning with Python" de Andreas Müller & Sarah Guido:** Una guía práctica y accesible.
-   **Libro "Python Machine Learning" de Sebastian Raschka & Vahid Mirjalili:** Una referencia muy completa.

---
