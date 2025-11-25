
import json

notebook_path = "1.- Introducción a Python. Python Avanzado/1. Sesión-2.ipynb"

with open(notebook_path, 'r', encoding='utf-8') as f:
    notebook_content = json.load(f)

# --- Start with a fresh list of cells ---
new_cells = []

# --- 1. Title and Intro ---
new_cells.append({
    "cell_type": "markdown",
    "metadata": {},
    "source": [
        "# Módulo 1.2: Funciones y Programación Orientada a Objetos en Python\n\n",
        "Esta sesión profundiza en dos de los pilares más importantes de Python: las **funciones** como bloques de código reutilizables y el **modelo de programación orientada a objetos (POO)**, que nos permite estructurar el código de manera modular y escalable."
    ]
})

# --- 2. Functions Section ---
new_cells.append({
    "cell_type": "markdown",
    "metadata": {},
    "source": [
        "## 1. Funciones: Bloques de Lógica Reutilizables\n\n",
        "Las funciones son la principal herramienta para dividir el código en bloques de lógica manejables y reutilizables. Permiten organizar el código, hacerlo más legible y evitar la repetición. Una función bien diseñada toma unas entradas (argumentos), realiza una tarea específica y, opcionalmente, devuelve un resultado."
    ]
})

# --- 2.1 Basic Function Definition ---
new_cells.append({
    "cell_type": "markdown",
    "metadata": {},
    "source": [
        "### 1.1. Definición Básica\n\n",
        "La sintaxis básica para definir una función utiliza la palabra clave `def`, seguida del nombre de la función, paréntesis para los argumentos y dos puntos. El cuerpo de la función debe estar indentado. Para la interpolación de strings, se recomienda usar **f-strings** (disponibles desde Python 3.6), ya que son más legibles y eficientes que el antiguo formato con `%`."
    ]
})
new_cells.append({
    "cell_type": "code",
    "execution_count": None,
    "metadata": {}, "outputs": [],
    "source": [
        "def saludar(nombre_usuario, saludo=\"Buenos días\"):\n",
        "    \"\"\"Saluda a un usuario con un saludo personalizable.\"\"\"\n",
        "    mensaje = f\"Hola, {nombre_usuario}. ¡Te deseo {saludo}!\"\n",
        "    print(mensaje)\n\n",
        "# Llamamos a la función con ambos argumentos\n",
        "saludar(\"Ricardo\", \"una excelente semana\")\n\n",
        "# Llamamos a la función usando el valor por defecto para 'saludo'\n",
        "saludar(\"Ana\")"
    ]
})

# --- 2.2 Advanced Arguments ---
new_cells.append({
    "cell_type": "markdown",
    "metadata": {},
    "source": [
        "### 1.2. Argumentos Avanzados: `*args` y `**kwargs`\n\n",
        "Python ofrece una sintaxis muy flexible para manejar un número variable de argumentos:\n\n",
        "- **`*args`**: Permite pasar un número variable de **argumentos posicionales**, que se empaquetan en una **tupla** dentro de la función.\n",
        "- **`**kwargs`**: Permite pasar un número variable de **argumentos de palabra clave (keyword)**, que se empaquetan en un **diccionario** dentro de la función."
    ]
})
new_cells.append({
    "cell_type": "code",
    "execution_count": None,
    "metadata": {}, "outputs": [],
    "source": [
        "def procesar_datos(*args, **kwargs):\n",
        "    \"\"\"Una función genérica que recibe cualquier tipo de argumento.\"\"\"\n",
        "    print(f\"Argumentos posicionales (tupla): {args}\")\n",
        "    print(f\"Argumentos de palabra clave (diccionario): {kwargs}\")\n\n",
        "print(\"Llamada 1:\")\n",
        "procesar_datos(101, 'cliente_A', 200.50, status='activo', region='Norte')\n\n",
        "print(\"\\nLlamada 2 (desempaquetando una lista y un diccionario):\")\n",
        "items = [102, 'cliente_B', 350.0]\n",
        "detalles = {'status': 'pendiente', 'prioridad': 'alta'}\n",
        "procesar_datos(*items, **detalles)"
    ]
})

# --- 2.3 Decorators ---
new_cells.append({
    "cell_type": "markdown",
    "metadata": {},
    "source": [
        "### 1.3. Decoradores: Modificando Funciones\n\n",
        "Un decorador es una función que toma otra función como argumento, le añade alguna funcionalidad y devuelve otra función, sin alterar el código de la función original. Es una forma poderosa de aplicar la metaprogramación. Se usan con la sintaxis `@decorador`."
    ]
})
new_cells.append({
    "cell_type": "code",
    "execution_count": None,
    "metadata": {}, "outputs": [],
    "source": [
        "import time\n\n",
        "def temporizador(func):\n",
        "    \"\"\"Un decorador que mide y muestra el tiempo de ejecución de una función.\"\"\"\n",
        "    def wrapper(*args, **kwargs):\n",
        "        inicio = time.time()\n",
        "        resultado = func(*args, **kwargs)\n",
        "        fin = time.time()\n",
        "        print(f\"La función '{func.__name__}' tardó {fin - inicio:.4f} segundos en ejecutarse.\")\n",
        "        return resultado\n",
        "    return wrapper\n\n",
        "@temporizador\n",
        "def tarea_larga(n):\n",
        "    \"\"\"Simula una tarea que consume tiempo.\"\"\"\n",
        "    sum(i*i for i in range(n))\n\n",
        "tarea_larga(1000000)"
    ]
})

# --- 3. OOP Section ---
new_cells.append({
    "cell_type": "markdown",
    "metadata": {},
    "source": [
        "## 2. Programación Orientada a Objetos (POO)\n\n",
        "La POO es un paradigma de programación que utiliza **objetos** para representar entidades del mundo real (o abstracto). Cada objeto es una **instancia** de una **clase**.\n\n",
        "- **Clase:** Una plantilla o molde para crear objetos. Define un conjunto de atributos (datos) y métodos (funciones) que los objetos de esa clase tendrán.\n",
        "- **Objeto:** Una instancia de una clase. Contiene datos concretos en sus atributos y puede ejecutar los métodos definidos en su clase."
    ]
})

# --- 3.1 Class Definition ---
new_cells.append({
    "cell_type": "markdown",
    "metadata": {},
    "source": [
        "### 2.1. Definición de una Clase\n\n",
        "En Python 3, una clase se define con la palabra clave `class`. No es necesario heredar de `object` explícitamente, ya que es el comportamiento por defecto."
    ]
})
new_cells.append({
    "cell_type": "code",
    "execution_count": None,
    "metadata": {}, "outputs": [],
    "source": [
        "class Vehiculo:\n",
        "    # Atributo de clase: es compartido por todas las instancias de la clase\n",
        "    garantia_meses = 12\n\n",
        "    def __init__(self, marca, modelo, anio):\n",
        "        \"\"\"El constructor de la clase. Se llama al crear una nueva instancia.\"\"\"\n",
        "        # Atributos de instancia: son únicos para cada objeto\n",
        "        self.marca = marca\n",
        "        self.modelo = modelo\n",
        "        self.anio = anio\n",
        "        self._kilometraje = 0 # Un atributo 'privado' por convención\n\n",
        "    def describir(self):\n",
        "        \"\"\"Un método de instancia que opera sobre los datos del objeto.\"\"\"\n",
        "        return f{self.marca} {self.modelo} ({self.anio}) con {self._kilometraje} km.\"\n\n",
        "    def avanzar(self, km):\n",
        "        \"\"\"Modifica el estado interno del objeto.\"\"\"\n",
        "        if km > 0:\n",
        "            self._kilometraje += km\n\n",
        "# Creamos dos objetos (instancias) de la clase Vehiculo\n",
        "coche1 = Vehiculo(\"Toyota\", \"Corolla\", 2022)\n",
        "coche2 = Vehiculo(\"Ford\", \"Mustang\", 2023)\n\n",
        "coche1.avanzar(150)\n",
        "print(coche1.describir())\n",
        "print(coche2.describir())\n\n",
        "# El atributo de clase es el mismo para ambos\n",
        "print(f\"Garantía Coche 1: {coche1.garantia_meses} meses\")\n",
        "print(f\"Garantía Coche 2: {coche2.garantia_meses} meses\")"
    ]
})

# --- 3.2 Properties ---
new_cells.append({
    "cell_type": "markdown",
    "metadata": {},
    "source": [
        "### 2.2. Propiedades (`@property`)\n\n",
        "El decorador `@property` permite tratar un método de una clase como si fuera un atributo de solo lectura. Esto es útil para calcular valores derivados o para proteger el acceso directo a un atributo."
    ]
})
new_cells.append({
    "cell_type": "code",
    "execution_count": None,
    "metadata": {}, "outputs": [],
    "source": [
        "import datetime\n\n",
        "class Vehiculo:\n",
        "    def __init__(self, marca, modelo, anio):\n",
        "        self.marca = marca\n",
        "        self.modelo = modelo\n",
        "        self.anio = anio\n\n",
        "    @property\n",
        "    def antiguedad(self):\n",
        "        \"\"\"Calcula la antigüedad del vehículo como un atributo de solo lectura.\"\"\"\n",
        "        anio_actual = datetime.date.today().year\n",
        "        return anio_actual - self.anio\n\n",
        "coche = Vehiculo(\"Honda\", \"Civic\", 2018)\n\n",
        "# Accedemos a 'antiguedad' como si fuera un atributo, no un método\n",
        "print(f\"El coche es un {coche.marca} {coche.modelo}.\")\n",
        "print(f\"Tiene {coche.antiguedad} años de antigüedad.\")"
    ]
})

# --- Replace old content with new cells ---
notebook_content['cells'] = new_cells

# --- Write the modernized notebook back to the file ---
with open(notebook_path, 'w', encoding='utf-8') as f:
    json.dump(notebook_content, f, indent=4, ensure_ascii=False)

print(f"Notebook '{notebook_path}' has been completely restructured and modernized.")
