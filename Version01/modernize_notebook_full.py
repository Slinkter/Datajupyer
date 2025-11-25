
import json

notebook_path = "1.- Introducción a Python. Python Avanzado/1. Sesión-1.ipynb"

with open(notebook_path, 'r', encoding='utf-8') as f:
    notebook_content = json.load(f)

# --- General Helper ---
def find_cell_by_source(source_text, cell_type='markdown'):
    for i, cell in enumerate(notebook_content['cells']):
        if cell['cell_type'] == cell_type and source_text in ''.join(cell['source']):
            return i
    return -1

# --- 1. Enhance Jupyter Explanation ---
jupyter_intro_index = find_cell_by_source("## IPython 3 (jupyter)")
if jupyter_intro_index != -1:
    notebook_content['cells'][jupyter_intro_index]['source'] = [
        "## El Ecosistema Jupyter: Tu Laboratorio Interactivo\n",
        "Durante el programa usaremos **Jupyter Notebooks**, una potente aplicación web que se ha convertido en el estándar de facto para la computación científica interactiva. Un notebook es un documento que puede contener tanto código ejecutable (Python, R, etc.) como elementos de texto enriquecido (ecuaciones, visualizaciones, texto con formato), creando un único artefacto reproducible y compartible.\n\n",
        "**¿Por qué es fundamental para la Ciencia de Datos?**\n\n",
        "- **Computación Interactiva:** Permite ejecutar pequeños fragmentos de código, ver los resultados inmediatamente y refinar el análisis de forma iterativa. Esto es ideal para la exploración de datos.\n",
        "- **Investigación Reproducible:** Un notebook encapsula todo el análisis, desde la carga de datos hasta la visualización final, en un solo lugar. Esto facilita que otros (o tu 'yo' del futuro) puedan entender y reproducir tu trabajo.\n",
        "- **Documentación y Comunicación:** Permite tejer una narrativa alrededor del código, explicando la metodología, interpretando los resultados y presentando conclusiones de forma clara y profesional."
    ]

# --- 2. Update Python History/Philosophy ---
python_why_index = find_cell_by_source("### ¿Por qué Python para la ciencia de datos?")
if python_why_index != -1:
    notebook_content['cells'][python_why_index+1]['source'] = [
        "El ecosistema de Python para la ciencia de datos ha madurado inmensamente desde sus inicios. Si bien las bases como **NumPy** (para computación numérica eficiente) y **Matplotlib** (para visualización) siguen siendo fundamentales, el ecosistema moderno se ha expandido para incluir herramientas de alto nivel que lo convierten en la opción preferida por la industria y la academia:\n\n",
        "- **Pandas:** Proporciona estructuras de datos de alto rendimiento (como el `DataFrame`) y herramientas de análisis de datos que son indispensables para la limpieza, manipulación y análisis de datos tabulares.\n\n",
        "- **Scikit-learn:** Ofrece un conjunto de herramientas unificado y fácil de usar para el aprendizaje automático (machine learning), cubriendo tareas desde la clasificación y regresión hasta el clustering y la reducción de dimensionalidad.\n\n",
        "- **Visualización Avanzada:** Librerías como **Seaborn** (construida sobre Matplotlib) y **Plotly** (para gráficos interactivos) permiten crear visualizaciones complejas y estéticamente agradables con muy poco código.\n\n",
        "- **Deep Learning:** Frameworks como **TensorFlow** y **PyTorch** han consolidado a Python como el lenguaje líder para la investigación y desarrollo en inteligencia artificial y redes neuronales profundas.\n\n",
        "La combinación de una sintaxis limpia, una comunidad masiva y un ecosistema de librerías de vanguardia hace de Python una solución integral que puede llevar un proyecto de datos desde la concepción inicial hasta su puesta en producción."
    ]

# --- 3. Data Types & Operators ---
# Expand on Tuples
tuple_index = find_cell_by_source("A diferencia de las listas, las tuplas no se pueden cambiar")
if tuple_index != -1:
    notebook_content['cells'][tuple_index]['source'] = [
        " - **Tuplas:** Son secuencias ordenadas e **inmutables** de elementos. A diferencia de las listas, una vez que se crea una tupla, no se puede modificar (ni añadir, ni eliminar, ni cambiar elementos). Esta propiedad de inmutabilidad las hace ideales para representar datos que no deben cambiar, como coordenadas, constantes o claves de diccionario. Se definen con paréntesis `()`."
    ]

# Explain the TypeError on tuple modification
tuple_error_index = find_cell_by_source("mi_tupla[0] = 2")
if tuple_error_index != -1 and tuple_error_index > 0:
    # Insert explanation cell before the error cell
    explanation_cell = {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "Intentar modificar un elemento de una tupla resultará en un `TypeError`, reforzando el concepto de inmutabilidad. Esta es una característica de diseño clave de Python que previene cambios accidentales en datos que se supone que son fijos."
        ]
    }
    notebook_content['cells'].insert(tuple_error_index, explanation_cell)

# Expand on Dictionaries
dict_index = find_cell_by_source("#### Tipo Mapping")
if dict_index != -1:
    notebook_content['cells'][dict_index+1]['source'] = [
        "- **Diccionario (`dict`):** Es una colección no ordenada de pares clave-valor. Cada `valor` está asociado a una `clave` única, que se utiliza para acceder a él. Las claves deben ser de un tipo de dato inmutable (como strings, números o tuplas), mientras que los valores pueden ser de cualquier tipo. Los diccionarios son extremadamente eficientes para buscar datos por su clave."
    ]
    # Add comments to the dictionary code cell
    dict_code_index = dict_index + 2
    if notebook_content['cells'][dict_code_index]['cell_type'] == 'code':
        notebook_content['cells'][dict_code_index]['source'] = [
            "# Los diccionarios se crean con llaves {}\n",
            "mi_diccionario = {\n",
            "    \"Nombre\" : \"Carl W.\", # La clave 'Nombre' es un string\n",
            "    \"Edad\" : 26, # La clave 'Edad' es un string\n",
            "    \"Apellido\" : \"Handlin\"\n",
            "}\n",
            "\n",
            "# Se accede a los valores usando la notación de corchetes con la clave\n",
            "mi_diccionario[\"Nombre\"]"
        ]

# --- 4. Control Flow ---
# Expand on 'for' loops
for_index = find_cell_by_source("#### For")
if for_index != -1:
    notebook_content['cells'][for_index]['source'] = [
        "#### El Bucle `for`: Iteración sobre Secuencias\n",
        "`for` se utiliza para iterar sobre los elementos de una secuencia (como una lista, tupla, string, o diccionario) o cualquier otro objeto iterable. En cada iteración, la variable del bucle toma el valor del siguiente elemento de la secuencia."
    ]
    # Add a more comprehensive for loop example
    for_code_index = for_index + 1
    if notebook_content['cells'][for_code_index]['cell_type'] == 'code':
        notebook_content['cells'][for_code_index]['source'] = [
            "# Iterar sobre una lista completa\n",
            "nombres = [\"Carl\", \"Edo\", \"Rick\"]\n",
            "for nombre in nombres:\n",
            "    print(f\"Hola, {nombre}!\")\n\n",
            "# La función `enumerate` nos da el índice y el valor en cada iteración\n",
            "print(\"\nCon enumerate:\")\n",
            "for indice, nombre in enumerate(nombres):\n",
            "    print(f\"Índice {indice}: {nombre}\")"
        ]

# --- 5. Clean up old/unnecessary cells ---
# Remove outdated github repo link comment
github_index = find_cell_by_source("## Github")
if github_index != -1:
    notebook_content['cells'][github_index+1]['source'] = [
        "Encuentra el repo en: https://github.com/ricalanis/Programa-Data-Science"
    ]


with open(notebook_path, 'w', encoding='utf-8') as f:
    json.dump(notebook_content, f, indent=4, ensure_ascii=False)

print(f"Notebook '{notebook_path}' has been modernized.")
