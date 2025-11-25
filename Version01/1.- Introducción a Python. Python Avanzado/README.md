# Módulo 1: Introducción a Python Avanzado

---

## 1. Introducción del Módulo

Este módulo es el pilar fundamental del curso. Su objetivo es trascender la sintaxis básica de Python para forjar una comprensión profunda y idiomática del lenguaje, una competencia indispensable para cualquier profesional en el campo de los datos.

A lo largo de tres sesiones, se deconstruyen los elementos esenciales del lenguaje, desde sus tipos de datos y estructuras de control hasta paradigmas avanzados como la Programación Orientada a Objetos y la metaprogramación. Se pone un énfasis especial no solo en el "cómo" se escribe el código, sino en el "porqué" de las decisiones de diseño, la eficiencia computacional (complejidad algorítmica) y las mejores prácticas de la ingeniería de software que garantizan un código mantenible, escalable y robusto.

Este módulo ha sido diseñado para que los estudiantes no solo usen Python, sino que piensen en Python.

---

## 2. Objetivos Pedagógicos

Al finalizar este módulo, el estudiante será capaz de:

-   **Escribir Código "Pythonic":** Aplicar las filosofías del "Zen de Python" (PEP 20) para escribir código limpio, legible y eficiente.
-   **Dominar las Estructuras de Datos:** Comprender el funcionamiento interno, la complejidad computacional (Big O) y los casos de uso prácticos de listas, tuplas, diccionarios y sets.
-   **Aplicar Paradigmas de Programación Avanzados:** Utilizar la Programación Orientada a Objetos (POO), funciones de orden superior, decoradores y generadores para escribir código modular y eficiente en memoria.
-   **Gestionar Errores y Excepciones:** Implementar estrategias robustas para el manejo de errores, adoptando el principio EAFP (Easier to Ask for Forgiveness than Permission).
-   **Estructurar y Distribuir Código:** Organizar un proyecto de software en módulos y paquetes, y entender el proceso moderno de distribución de paquetes en Python.

---

## 3. Temas Tratados

### Sesión 1: Fundamentos y Tipos de Datos
Esta sesión establece el entorno de trabajo y repasa los fundamentos del lenguaje desde una perspectiva avanzada.

-   **Entorno de Desarrollo:**
    -   Uso de `conda` para la gestión de entornos virtuales, garantizando la reproducibilidad de los proyectos.
    -   **Jupyter Notebooks:** El laboratorio interactivo para la exploración y el análisis de datos.
-   **El Zen de Python (PEP 20):** Los principios que guían el diseño del lenguaje.
-   **Tipos de Datos y Estructuras:**
    -   **Numéricos:** `int`, `float`, `complex`.
    -   **Secuencias:**
        -   `list`: Mutables, ordenadas. Análisis de complejidad de operaciones (`append`, `pop`, `insert`).
        -   `tuple`: Inmutables, ordenadas. Casos de uso (e.g., claves de diccionario, datos que no deben cambiar).
        -   `range`: Secuencias numéricas eficientes en memoria.
    -   **Mappings:**
        -   `dict`: Pares clave-valor. Análisis de complejidad de búsqueda, inserción y eliminación.
    -   **Sets:** Colecciones no ordenadas de elementos únicos. Operaciones de conjuntos (`union`, `intersection`).
-   **Variables y Referencias:**
    -   El modelo de objetos de Python: toda variable es una referencia a un objeto.
    -   Diferencia crítica entre `==` (igualdad de valor) y `is` (identidad de objeto).
-   **Control de Flujo:** `if`, `for`, `while`, y el uso de `enumerate` y `zip` para iteraciones eficientes.

### Sesión 2: Funciones y Programación Orientada a Objetos (POO)
Esta sesión introduce los dos pilares para la estructuración de código en Python.

-   **Funciones como Objetos de Primera Clase:**
    -   Definición, argumentos posicionales y de palabra clave (`keyword`).
    -   Argumentos variables: `*args` y `**kwargs`.
    -   **Tipado Estático (Type Hinting - PEP 484):** Anotaciones de tipo para un código más claro y robusto.
    -   **Funciones Lambda:** Funciones anónimas para operaciones sencillas.
-   **Decoradores:**
    -   Metaprogramación para extender la funcionalidad de las funciones sin modificar su código.
    -   Ejemplo práctico: `timer` para medir el rendimiento.
-   **Programación Orientada a Objetos (POO):**
    -   **Clases e Instancias:** Moldes y objetos.
    -   Constructor `__init__` y el puntero `self`.
    -   **Atributos de Clase vs. Atributos de Instancia.**
    -   **Encapsulamiento:** Atributos públicos, protegidos (`_`) y privados (`__`).
    -   **Métodos de Instancia, Métodos de Clase (`@classmethod`) y Métodos Estáticos (`@staticmethod`).**
    -   **Propiedades (`@property`):** Getters y setters de una forma "Pythonic".
    -   **Herencia y Polimorfismo:** Reutilización de código y diseño de interfaces comunes.
    -   **Métodos Mágicos (Dunder Methods):** `__str__`, `__repr__`, `__len__`, etc., para que los objetos se comporten como tipos nativos.

### Sesión 3: Python Avanzado y Estructura de Proyectos
La sesión final consolida el conocimiento con herramientas para escribir código eficiente y bien organizado.

-   **Manejo de Excepciones:**
    -   Bloques `try...except...else...finally`.
    -   El estilo "Pythonic" EAFP (Easier to Ask for Forgiveness than Permission) vs. LBYL.
-   **Iteradores y Generadores:**
    -   El protocolo de iteración (`__iter__` y `__next__`).
    -   **Generator Functions (`yield`):** Creación de secuencias "perezosas" para un consumo de memoria óptimo.
    -   **Generator Expressions:** Sintaxis similar a las comprehensions pero con evaluación perezosa.
-   **Comprehensions:**
    -   Sintaxis concisa y eficiente para crear `list`, `dict` y `set`.
-   **Estructura de Proyectos:**
    -   Diferencia entre scripts, **módulos** y **paquetes**.
    -   Importaciones absolutas vs. relativas.
    -   El rol de `__init__.py`.
    -   Ejemplo práctico analizando los directorios `mipaquete` y `nssample`.
-   **Distribución de Paquetes:**
    -   Introducción a los estándares modernos con `pyproject.toml` y herramientas como `setuptools`.

---

## 4. Ejemplos y Notas del Profesor

### Nota sobre `is` vs. `==`
Un error común es usar `is` cuando se quiere comparar el valor de dos objetos.
-   `a == b` compara si los **valores** de `a` y `b` son iguales. Llama internamente a `a.__eq__(b)`.
-   `a is b` compara si `a` y `b` apuntan a la **misma dirección de memoria**, es decir, si son el mismo objeto.

En ciencia de datos, casi siempre querrás usar `==` (por ejemplo, con arrays de NumPy o DataFrames de Pandas). El uso canónico de `is` es para comparar con singletons como `None`, `True` o `False` (e.g., `if mi_variable is None:`).

### Ejemplo Avanzado: Decorador con Argumentos

```python
import time
from functools import wraps

def timer(unit="s"):
    """
    Un decorador que mide el tiempo de ejecución y permite especificar la unidad.
    Usa functools.wraps para preservar los metadatos de la función original.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.perf_counter()
            result = func(*args, **kwargs)
            end_time = time.perf_counter()
            duration = end_time - start_time
            
            if unit == "ms":
                duration *= 1000
                print(f"Tiempo de ejecución de '{func.__name__}': {duration:.4f} ms")
            else:
                print(f"Tiempo de ejecución de '{func.__name__}': {duration:.4f} s")
            
            return result
        return wrapper
    return decorator

# Uso del decorador con argumento
@timer(unit="ms")
def proceso_intensivo(n):
    """Simula un cálculo que consume tiempo."""
    return sum(i**2 for i in range(n))

proceso_intensivo(1000000)
print(proceso_intensivo.__name__) # Imprime 'proceso_intensivo' gracias a @wraps
```

### Nota sobre Generadores vs. List Comprehensions
Para conjuntos de datos masivos, la diferencia entre una list comprehension y un generador es crítica.

-   **List Comprehension:** Crea la lista **completa en memoria**.
    `mi_lista = [i * 2 for i in range(10**7)]` # ¡Consume mucha RAM!
-   **Generator Expression:** Crea un objeto generador que produce los valores **uno por uno bajo demanda**.
    `mi_generador = (i * 2 for i in range(10**7))` # Consumo de RAM casi nulo.

En pipelines de datos, siempre se debe preferir el uso de generadores para procesar los datos en streaming, evitando así cargar todo en memoria.

---

## 5. Fuentes y Referencias

-   **PEP 8 -- Style Guide for Python Code:** [https://www.python.org/dev/peps/pep-0008/](https://www.python.org/dev/peps/pep-0008/)
-   **PEP 20 -- The Zen of Python:** [https://www.python.org/dev/peps/pep-0020/](https://www.python.org/dev/peps/pep-0020/)
-   **PEP 484 -- Type Hints:** [https://www.python.org/dev/peps/pep-0484/](https://www.python.org/dev/peps/pep-0484/)
-   **Documentación oficial de Python 3:** [https://docs.python.org/3/](https://docs.python.org/3/)
-   **Libro "Fluent Python" de Luciano Ramalho:** Una referencia indispensable para programación avanzada en Python.

---