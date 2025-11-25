
import json

notebook_path = "1.- Introducción a Python. Python Avanzado/1. Sesión-3.ipynb"

# It's safer to read the notebook to find the exact cell content to replace
with open(notebook_path, 'r', encoding='utf-8') as f:
    notebook_content = json.load(f)

# --- Start with a fresh list of cells ---
new_cells = []

# --- 1. Title and Agenda ---
new_cells.append({
    "cell_type": "markdown",
    "metadata": {},
    "source": [
        "# Módulo 1.3: Python Avanzado y Estructura de Proyectos\n\n",
        "Esta sesión final del módulo de introducción cubre temas avanzados que son cruciales para escribir código en Python robusto, eficiente y bien estructurado."
    ]
})
new_cells.append({
    "cell_type": "markdown",
    "metadata": {},
    "source": [
        "## Agenda\n\n",
        "1.  **Manejo de Excepciones:** Estrategias para escribir código resiliente.\n",
        "2.  **Comprehensions:** Sintaxis concisa para crear colecciones.\n",
        "3.  **Generadores:** Creación de secuencias 'perezosas' para optimizar el uso de memoria.\n",
        "4.  **Funciones Lambda:** Funciones anónimas para tareas simples.\n",
        "5.  **Estructura de Proyectos:** Cómo organizar el código en módulos y paquetes.\n",
        "6.  **Distribución de Paquetes:** El estándar moderno para empaquetar y distribuir tu código."
    ]
})

# --- 2. Exception Handling ---
new_cells.append({
    "cell_type": "markdown",
    "metadata": {},
    "source": [
        "## 1. Manejo de Excepciones\n\n",
        "Python utiliza excepciones para gestionar errores que ocurren durante la ejecución del programa. Un manejo de errores adecuado es fundamental para la robustez del software.\n\n",
        "### Estrategias: LBYL vs. EAFP\n\n",
        "- **LBYL (Look Before You Leap - Mira antes de saltar):** Consiste en verificar explícitamente las precondiciones antes de realizar una operación. Es como comprobar si una llave existe en un diccionario antes de intentar acceder a ella.\n",
        "- **EAFP (Easier to Ask for Forgiveness than Permission - Es más fácil pedir perdón que permiso):** Consiste en ejecutar el código directamente y capturar las excepciones que puedan surgir. Este es el estilo preferido en la comunidad Python, ya que se considera más limpio y rápido si las excepciones no son la norma.\n\n",
        "**Ejemplo EAFP (preferido en Python):**"
    ]
})
new_cells.append({
    "cell_type": "code",
    "execution_count": None,
    "metadata": {}, "outputs": [],
    "source": [
        "mi_dict = {'a': 1, 'b': 2}\n\n",
        "try:\n",
        "    valor = mi_dict['c']\n",
        "    print(f\"El valor es {valor}\")\n",
        "except KeyError:\n",
        "    print(\"La clave 'c' no fue encontrada. Se usará un valor por defecto.\")\n",
        "    valor = 0"
    ]
})
new_cells.append({
    "cell_type": "markdown",
    "metadata": {},
    "source": [
        "### Bloque `try...except...else...finally`\n\n",
        "La estructura completa para el manejo de excepciones es:\n\n",
        "- `try`: Contiene el código que podría lanzar una excepción.\n",
        "- `except`: Se ejecuta si ocurre una excepción del tipo especificado en el bloque `try`.\n",
        "- `else`: Se ejecuta si **no** ocurre ninguna excepción en el bloque `try`.\n",
        "- `finally`: Se ejecuta **siempre**, haya o no haya ocurrido una excepción. Es ideal para tareas de limpieza, como cerrar un archivo o una conexión de red."
    ]
})
new_cells.append({
    "cell_type": "code",
    "execution_count": None,
    "metadata": {}, "outputs": [],
    "source": [
        "try:\n",
        "    resultado = 10 / 2\n",
        "except ZeroDivisionError:\n",
        "    print(\"Error: No se puede dividir por cero.\")\n",
        "else:\n",
        "    print(f\"La división fue exitosa. Resultado: {resultado}\")\n",
        "finally:\n",
        "    print(\"Fin del bloque de manejo de excepciones.\")"
    ]
})

# --- 3. Comprehensions ---
new_cells.append({
    "cell_type": "markdown",
    "metadata": {},
    "source": [
        "## 2. Comprehensions\n\n",
        "Las *comprehensions* son una de las características más apreciadas de Python. Ofrecen una sintaxis concisa y legible para crear listas, diccionarios o sets a partir de otros iterables. Generalmente, son más rápidas que usar bucles `for` explícitos."
    ]
})
new_cells.append({
    "cell_type": "code",
    "execution_count": None,
    "metadata": {}, "outputs": [],
    "source": [
        "# List comprehension: crear una lista con los cuadrados de los números pares del 0 al 9\n",
        "cuadrados_pares = [n**2 for n in range(10) if n % 2 == 0]\n",
        "print(f'List comprehension: {cuadrados_pares}')\n\n",
        "# Set comprehension: crear un conjunto con los mismos valores (elimina duplicados)\n",
        "set_cuadrados = {n**2 for n in range(10)}\n",
        "print(f'Set comprehension: {set_cuadrados}')\n\n",
        "# Dict comprehension: crear un diccionario que mapea un número a su cuadrado\n",
        "dict_cuadrados = {n: n**2 for n in range(5)}\n",
        "print(f'Dict comprehension: {dict_cuadrados}')"
    ]
})
new_cells.append({
    "cell_type": "markdown",
    "metadata": {},
    "source": [
        "> **Nota del profesor:** Las *comprehensions* son poderosas, pero deben usarse con moderación. Si la lógica se vuelve demasiado compleja (múltiples `for` anidados y `if`), es mejor usar un bucle `for` tradicional para mantener la legibilidad del código. **La legibilidad cuenta**."
    ]
})


# --- 4. Generators ---
new_cells.append({
    "cell_type": "markdown",
    "metadata": {},
    "source": [
        "## 3. Generadores: Iteración Perezosa (Lazy Iteration)\n\n",
        "Un generador es un tipo especial de iterador que no almacena todos sus valores en memoria. En su lugar, 'genera' los valores uno por uno sobre la marcha, a medida que se le solicitan. Esto los hace extremadamente eficientes para trabajar con secuencias de datos muy grandes o infinitas.\n\n",
        "Se pueden crear de dos formas:\n\n",
        "1.  **Expresión generadora:** Usa una sintaxis similar a una *list comprehension*, pero con paréntesis `()`.
",
        "2.  **Función generadora:** Una función que usa la palabra clave `yield`."
    ]
})
new_cells.append({
    "cell_type": "code",
    "execution_count": None,
    "metadata": {}, "outputs": [],
    "source": [
        "# 1. Expresión generadora: no calcula todos los cuadrados, solo crea el objeto generador\n",
        "gen_cuadrados = (n**2 for n in range(1000000000))\n",
        "print(f'Objeto generador: {gen_cuadrados}')\n\n",
        "# Consumimos los primeros 5 valores del generador\n",
        "print('Primeros 5 valores:')\n",
        "for i in range(5):\n",
        "    print(next(gen_cuadrados))\n\n",
        "# 2. Función generadora para leer un archivo grande línea por línea\n",
        "def lector_log_grande(ruta_archivo):\n",
        "    with open(ruta_archivo, 'r') as f:\n",
        "        for linea in f:\n",
        "            yield linea # Pausa la función y entrega la línea\n"
    ]
})

# --- 5. Lambdas ---
new_cells.append({
    "cell_type": "markdown",
    "metadata": {},
    "source": [
        "## 4. Funciones Lambda (Funciones Anónimas)\n\n",
        "Una función `lambda` es una pequeña función anónima definida con la palabra clave `lambda`. Puede tener cualquier número de argumentos, pero solo puede tener **una expresión**. Son útiles para tareas cortas donde definir una función completa con `def` sería excesivo.\n\n",
        "Su uso más común es como argumento para funciones de orden superior, como `sorted()`, `map()` o `filter()`."
    ]
})
new_cells.append({
    "cell_type": "code",
    "execution_count": None,
    "metadata": {}, "outputs": [],
    "source": [
        "puntos = [('A', 3), ('C', 1), ('B', 2)]\n\n",
        "# Usamos una lambda como clave para ordenar la lista de tuplas por su segundo elemento\n",
        "puntos_ordenados = sorted(puntos, key=lambda punto: punto[1])\n\n",
        "print(f'Lista original: {puntos}')\n",
        "print(f'Lista ordenada por el número: {puntos_ordenados}')"
    ]
})

# --- 6. Modules and Packages ---
new_cells.append({
    "cell_type": "markdown",
    "metadata": {},
    "source": [
        "## 5. Estructura de Proyectos: Módulos y Paquetes\n\n",
        "A medida que un proyecto crece, es fundamental organizar el código en archivos y directorios.\n\n",
        "- **Módulo:** Un archivo `.py` que contiene definiciones y declaraciones de Python. Permite agrupar lógicamente el código relacionado y reutilizarlo mediante la sentencia `import`.\n",
        "- **Paquete:** Un directorio que contiene módulos y un archivo especial `__init__.py`. Este archivo (que puede estar vacío) le indica a Python que el directorio debe ser tratado como un paquete, permitiendo importaciones anidadas (e.g., `from mi_paquete.mi_modulo import mi_funcion`)."
    ]
})

# --- 7. Packaging ---
new_cells.append({
    "cell_type": "markdown",
    "metadata": {},
    "source": [
        "## 6. Distribución de Paquetes: El Estándar Moderno\n\n",
        "Para que nuestro código sea reutilizable por otros o en otros proyectos, debemos empaquetarlo. El estándar moderno en Python se basa en el archivo `pyproject.toml`.\n\n",
        "**¡Nunca modifiques `sys.path` manualmente!** Manipular `sys.path` (e.g., `sys.path.append(...)`) es una práctica frágil y propensa a errores que dificulta la reproducibilidad. En su lugar, debemos instalar nuestro paquete en nuestro entorno virtual.\n\n",
        "### Pasos para Empaquetar un Proyecto\n\n",
        "1.  **Estructura del proyecto:**\n",
        "    ```\n",
        "    mi_proyecto/\n",
        "    ├── mipaquete/          # El código fuente de nuestro paquete\n",
        "    │   ├── __init__.py\n",
        "    │   └── saludos.py\n",
        "    └── pyproject.toml      # El archivo de configuración\n",
        "    ```\n\n",
        "2.  **Crear `pyproject.toml`:**\n",
        "    Este archivo le dice a las herramientas de construcción (como `pip`) cómo construir e instalar tu paquete.\n",
        "    ```toml\n",
        "    [project]\n",
        "    name = \"mipaquete\"\n",
        "    version = \"0.1.0\"\n",
        "    authors = [{name = \"Tu Nombre\", email = \"tu@email.com\"}]\n",
        "    description = \"Un paquete de ejemplo para el curso.\"\n",
        "    ```\n\n",
        "3.  **Instalar el paquete en modo editable:**\n",
        "    Desde el directorio raíz (`mi_proyecto/`), ejecutamos:\n",
        "    ```bash\n",
        "    pip install -e .\n",
        "    ```\n",
        "    El flag `-e` (o `--editable`) instala el paquete creando un enlace al código fuente. Esto significa que cualquier cambio que hagas en `saludos.py` estará disponible inmediatamente en tu entorno sin necesidad de reinstalar.\n\n",
        "4.  **Usar el paquete instalado:**\n",
        "    Ahora puedes importar y usar tu paquete desde cualquier lugar en tu entorno virtual, de la manera correcta."
    ]
})
new_cells.append({
    "cell_type": "code",
    "execution_count": None,
    "metadata": {}, "outputs": [],
    "source": [
        "# Asumiendo que has seguido los pasos anteriores y has instalado 'mipaquete'\n",
        "from mipaquete import saludos\n\n",
        "saludos.hola()"
    ]
})

# --- Replace old content with new cells ---
notebook_content['cells'] = new_cells

# --- Write the modernized notebook back to the file ---
with open(notebook_path, 'w', encoding='utf-8') as f:
    json.dump(notebook_content, f, indent=4, ensure_ascii=False)

print(f"Notebook '{notebook_path}' has been completely restructured and modernized.")
