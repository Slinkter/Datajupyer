# Nivel Avanzado - Python Zero to Hero

## Objetivo
Dominio de arquitectura, bajo nivel, concurrencia, metaprogramación e internals de CPython.

## Notebooks creados (7)

| # | Archivo | Tema | Estado |
|---|---------|------|--------|
| 1 | `A01_concurrencia_fundamentos.ipynb` | GIL, I/O vs CPU bound, benchmarking | [x] Completado ✅ |
| 2 | `A02_asincronismo_asyncio.ipynb` | async/await, gather, semáforos, async for | [x] Completado ✅ |
| 3 | `A03_multiprocessing_multithreading.ipynb` | concurrent.futures, Pool, Lock, shared_memory | [x] Completado ✅ |
| 4 | `A04_metaprogramacion_descriptores.ipynb` | Metaclasses, descriptors, ABC, type() | [x] Completado ✅ |
| 5 | `A05_internals_memoria.ipynb` | gc, __slots__, dis, profiling, refcount | [x] Completado ✅ |
| 6 | `A06_patrones_diseno.ipynb` | Factory, Singleton, Strategy, Observer, etc. | [x] Completado ✅ |
| 7 | `A07_proyecto_motor_async.ipynb` | Micro-framework async resiliente | [x] Completado ✅ |

## Referencias
- Architecture Patterns with Python (Percival & Gregory)
- CPython Internals (Anthony Shaw)
- PEPs 8/484/557/712

## Reglas
- Nunca usar `from module import *`
- Siempre documentar la complejidad temporal de los ejemplos
- Código debe ser ejecutable sin dependencias externas salvo stdlib
- Metaprogramación explicada con diagramas de resolución de atributos
