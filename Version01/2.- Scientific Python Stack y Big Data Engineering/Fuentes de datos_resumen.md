# Resumen Cornell: Módulo 2.2 - Fuentes de Datos y E/S con Pandas

---

### **1. Título y Contexto**

**Título:** Módulo 2.2: Fuentes de Datos y Herramientas de E/S con Pandas.

**Contexto:** Un análisis de datos solo puede empezar cuando tenemos datos. Esta sesión es una guía práctica de las herramientas de Entrada/Salida (E/S o IO) de Pandas, que actúan como un puente entre diversas fuentes de datos (archivos, bases de datos, APIs) y la estructura DataFrame. Es una habilidad fundamental para cualquier científico de datos.

---

### **2. Notas Clave**

**Idea Central:** Pandas ofrece una familia de funciones `read_*` para leer datos y `to_*` para escribirlos, haciendo trivial la interacción con múltiples formatos.

#### **Formatos Comunes y Funciones:**

*   **CSV (Valores Separados por Comas):** El formato de texto más universal.
    *   **Lectura:** `pd.read_csv('archivo.csv')`.
        *   Parámetros útiles: `sep` (para delimitadores como `;` o `	`), `header` (para especificar la fila de encabezados), `encoding` (ej. `'ISO-8859-1'` o `'utf-8'`).
    *   **Escritura:** `df.to_csv('salida.csv', index=False)`.
        *   **`index=False` es crucial** para evitar que Pandas escriba su propio índice numérico como una columna en el archivo.

*   **Excel (`.xlsx`):** Para hojas de cálculo.
    *   **Lectura:** `pd.read_excel('archivo.xlsx', sheet_name='NombreDeLaHoja')`.
    *   **Escritura:** `df.to_excel('salida.xlsx', index=False)`.
    *   **Dependencia:** Requiere librerías externas como `openpyxl`.

*   **SQL (Bases de Datos):** Para interactuar con bases de datos relacionales.
    *   **Proceso:** Se necesita un motor de conexión (ej. `sqlite3` para SQLite, `sqlalchemy` para PostgreSQL/MySQL).
    *   **Lectura:** `pd.read_sql_query('SELECT * FROM mi_tabla', conexion_db)`.
    *   **Escritura:** `df.to_sql('nombre_tabla', conexion_db, if_exists='replace')`.

*   **JSON (JavaScript Object Notation):** Formato estándar para APIs web.
    *   **Lectura:** `pd.read_json('datos.json')`. Puede leer tanto archivos locales como URLs directamente.

*   **HTML:** Para extraer tablas directamente de páginas web.
    *   **Lectura:** `pd.read_html('https://una-pagina-web.com')`.
    *   **Importante:** Esta función devuelve una **LISTA** de DataFrames, uno por cada tabla `<table>` encontrada en el HTML. Debes seleccionar la correcta por su índice (ej. `tablas[0]`).

*   **HDF5 (`.h5`):** Formato binario de alto rendimiento.
    *   **Ventaja:** Optimizado para almacenar grandes volúmenes de datos numéricos. Es mucho más rápido para leer y escribir que los formatos de texto como CSV, especialmente con datasets que no caben en memoria.

---

### **3. Preguntas Clave**

*   ¿Por qué se debe especificar casi siempre `index=False` al guardar un archivo CSV o Excel?
*   ¿Qué devuelve exactamente `pd.read_html()` y qué paso extra se necesita para obtener la tabla deseada?
*   Si al leer un CSV obtienes un `UnicodeDecodeError`, ¿qué parámetro de `read_csv` deberías investigar?
*   ¿Cuál es el proceso de dos pasos para leer datos de una base de datos SQL en un DataFrame?
*   ¿En qué escenario de trabajo real sería HDF5 una mejor elección que CSV para guardar tus datos?

---

### **4. Ejemplos Simplificados**

*   **Leer un CSV desde una URL:**
    ```python
    url = 'https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv'
    df = pd.read_csv(url)
    ```
*   **Guardar en Excel:**
    ```python
    df.to_excel("paises.xlsx", index=False)
    ```
*   **Leer la primera tabla de una página web:**
    ```python
    lista_de_tablas = pd.read_html('https://es.wikipedia.org/wiki/Anexo:Pa%C3%ADses')
    paises_df = lista_de_tablas[0]
    ```

---

### **5. Analogías**

*   **Pandas IO Tools:** Un políglota experto en "idiomas de datos". No importa si le hablas en CSV, Excel, SQL o JSON, él te entiende y lo traduce a un idioma común (el DataFrame).
*   **`pd.read_csv`:** Un intérprete que convierte un documento de texto plano, siguiendo unas reglas de puntuación (delimitadores), en una tabla perfectamente estructurada.
*   **`pd.read_html`:** Un bibliotecario al que le pides "las tablas de este libro". En lugar de darte una sola, te trae todas las que encuentra, y tú eliges la que necesitas.

---

### **6. Resumen Final**

Esta sesión es eminentemente práctica y demuestra la capacidad de Pandas para actuar como un centro de operaciones de datos. Cubre las funciones esenciales para leer y escribir desde y hacia los formatos más prevalentes en el mundo real, desde archivos de texto simples hasta bases de datos relacionales y contenido web dinámico. Dominar estas herramientas de E/S es el primer paso para cualquier flujo de trabajo en ciencia de datos.

---

### **7. Ejercicios Recomendados**

1.  **CSV:** Busca un dataset público en formato CSV en un portal de datos abiertos (como el de tu ciudad o país) y cárgalo en un DataFrame. Imprime sus 5 primeras filas y la información general con `.info()`.
2.  **Excel:** Guarda el DataFrame del ejercicio anterior en un archivo Excel llamado `mi_dataset.xlsx`.
3.  **HTML:** Encuentra una página en Wikipedia con una tabla de resultados deportivos o una lista de películas. Usa `pd.read_html()` para extraerla y muéstrala.
4.  **JSON:** Busca una API pública simple (ej. `https://api.coindesk.com/v1/bpi/currentprice.json`). Cárgala en un DataFrame.
5.  **SQL:** Crea un DataFrame simple con dos columnas y tres filas. Usa la librería `sqlite3` y el método `.to_sql()` para guardar este DataFrame en una base de datos SQLite local llamada `mi_base.db`.
