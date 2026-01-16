| Característica         | `pandas.pivot()`                                       | `pandas.pivot_table()`                                    |
| :--------------------- | :----------------------------------------------------- | :-------------------------------------------------------- |
| **Propósito Principal**  | Reestructurar un DataFrame de formato "largo" a "ancho". | Reestructurar y resumir (agregar) un DataFrame.           |
| **Manejo de Duplicados** | No permite entradas duplicadas para el `index` y `columns` combinados. Si existen, arrojará un error. | Puede manejar entradas duplicadas, ya que las agrupa y aplica una función de agregación. |
| **Agregación**           | No realiza ninguna agregación; simplemente reorganiza los datos. | Realiza agregación de datos automáticamente (por defecto, la media) o según la función especificada (`aggfunc`). |
| **Flexibilidad**         | Menos flexible; requiere que la combinación de `index` y `columns` sea única. | Más flexible; permite múltiples funciones de agregación y puede lidiar con jerarquías en el índice y las columnas. |
| **Parámetros Clave**     | `index`, `columns`, `values`                           | `index`, `columns`, `values`, `aggfunc`, `fill_value`, `margins`, `dropna` |
| **Cuándo usar**          | Cuando la combinación de `index` y `columns` es única y solo se necesita reorganizar los datos sin agregación. | Cuando hay o podría haber entradas duplicadas que necesitan ser agregadas, o cuando se desea un resumen de los datos. |
