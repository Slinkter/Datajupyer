# Prompts para Recrear Notebooks - Datajupyer

## ⚠️ INSTRUCCIONES PARA EL AI
Al iniciar, leer primero:
- AGENTS.md


Perfil del AI (cargar al inicio):
>Eres un Ingeniero de Software Senior especializado en Python moderno, con Maestría en Educación y Pedagogía Tecnológica. Usar metodología: Objetivos → Analogías → Diagramas ASCII → Tablas → Ejercicios → Resumen.

---

## 📋 TAREA 1: Fuentes de datos

**Archivo:** `Version01/2.- Scientific Python Stack y Big Data Engineering/Fuentes de datos.ipynb`

** contenido a incluir:**
- Fuentes de datos públicas
- APIs comunes (Kaggle, World Bank, etc.)
- Cómo descargar datos
- Ejemplos prácticos

**Prompt:**
```
Recrea el notebook "Fuentes de datos" con:
1. Objetivos de aprendizaje
2. Diagramas ASCII de flujos de datos
3. Tablas de fuentes populares
4. Código funcional con Python 3
5. Ejercicios prácticos
```

---

## 📋 TAREA 2: Web Scraping

**Archivo:** `Version01/2.- Scientific Python Stack y Big Data Engineering/Web Scraping - BeautifulSoup4.ipynb`

** contenido a incluir:**
- requests + BeautifulSoup
- Extraer datos de páginas web
- Guardar datos
- Ética del scraping

**Prompt:**
```
Recrea el notebook "Web Scraping - BeautifulSoup4" con metodología pedagógica:
1. Por qué hacer web scraping
2. Diagrama: request → parse → extract → save
3. Ejemplos paso a paso
4. Alternativas (Selenium, scrapy)
5. Ejercicios
```

---

## 📋 TAREA 3: Regex

**Archivo:** `Version01/2.- Scientific Python Stack y Big Data Engineering/Regex.ipynb`

** contenido a incluir:**
- Metacaracteres
- Patrones comunes
- Extracción de texto
- Validación

**Prompt:**
```
Recrea el notebook "Regex" con:
1. Qué es regex y para qué sirve
2. Tabla de metacaracteres
3. Diagramas de matching
4. Ejemplos prácticos
5. Ejercicios
```

---

## 📋 TAREA 4: SQL

**Archivo:** `Version01/2.- Scientific Python Stack y Big Data Engineering/SQL.ipynb`

** contenido a incluir:**
- SQL básico (SELECT, WHERE, JOIN)
- Consultas desde Python
- SQLite práctica
- Ejemplos con pandas

**Prompt:**
```
Recrea el notebook "SQL" con:
1. Por qué SQL es importante
2. Diagrama de consulta SQL
3. Comandos básicos con ejemplos
4. Python + SQL (sqlite3, SQLAlchemy)
5. Ejercicios
```

---

## 📋 TAREA 5: Tidy Data

**Archivo:** `Version01/2.- Scientific Python Stack y Big Data Engineering/Tidy Data.ipynb`

** contenido a incluir:**
- tidy data principles
- Melt/pivot
- Manejo de valores faltantes
- Normalización

**Prompt:**
```
Recrea el notebook "Tidy Data":
1. Qué es tidy data (Hadley Wickham)
2. Problemas comunes (melt, pivot)
3. Diagramas antes/después
4. Código con pandas
5. Ejercicios
```

---

## 📋 TAREA 6: SciPy Ecosystem

**Archivo:** `Version01/2.- Scientific Python Stack y Big Data Engineering/Introducción al ecosistema SciPy.ipynb`

** contenido a incluir:**
- NumPy, SciPy, matplotlib
- scikit-learn
- Statsmodels
- Relaciones entre librerías

**Prompt:**
```
Recrea el notebook "SciPy Ecosystem":
1. Mapa del ecosistema Python
2. Diagrama de relaciones
3. Cada librería y su propósito
4. Ejemplos básicos
5. Cuándo usar cada una
```

---

## 📋 TAREA 7: Reto Kaggle

**Archivo:** `Version01/2.- Scientific Python Stack y Big Data Engineering/Reto Kaggle.ipynb`

** contenido a incluir:**
- Qué es Kaggle
- Competitions
- Datasets
- Primeros pasos

**Prompt:**
```
Recrea el notebook "Reto Kaggle":
1. Introducción a Kaggle
2. Cómo funcionan las competencias
3. Ejemplo de dataset
4. Primer submission
5. Recursos
```

---

## 📋 TAREA 8: Resumen SciPy Stack

**Archivo:** `Version01/2.- Scientific Python Stack y Big Data Engineering/ResumendeSciPyStack.ipynb`

*(Si no existe, crear resumen de la fase)*

---

## 🔄 Validación POST-Recreación

```python
import json
with open('notebook.ipynb') as f:
    json.load(f)  # Debe funcionar sin error
print("✅ Notebook válido")
```

---

## ⚠️ Reglas

1. Usar Write tool (NO edit para archivos grandes)
2. Validar JSON después de crear
3. Si falla: git checkout y reintentar
4. Mantener diagrams simples

---

*Para ejecutar: leer cada TAREA y procesar secuencialmente*
*Tiempo estimado: 3-4 horas total para Fase 2*