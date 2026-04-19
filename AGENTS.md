# AGENTS.md - Datajupyer

## Repositorio

Colección de notebooks educativos Python/Data Science en dos versiones:
- `Estudio/` - Versión original
- `Version02/` - Segunda versión (pandas, machine learning)

## Reglas Críticas

### JSON en notebooks
- **NUNCA** editar notebooks directamente (70% de probabilidad de romper JSON)
- Siempre usar **Write tool** para recrear desde cero
- Validar después: `python3 -c "import json; json.load(open('archivo.ipynb'))"`

### Si falla JSON
```bash
git restore <archivo>
```

## Workflow

```
1. Read notebook existente
2. Identificar huecos pedagógicos + código obsoleto
3. Recrear con metodología (Write tool)
4. Validar JSON
5. Actualizar PLAN_EJECUCION.md
```

## Estándar

Cada notebook debe incluir:
- **Título claro** + **Objetivos** (🎯)
- **Introducción** (por qué es importante)
- **Puente Pedagógico**: Por qué → Intuición → Cómo
- **Diagramas ASCII** para flujos
- **Básico** → **Avanzado** (caso simple → caso real)
- **Ejercicios** (📝)
- **Resumen** (📋)

## Código Moderno

- Python 3.12+ (f-strings, type hints, pathlib)
- Pandas/NumPy eficientes
- Generadores para hardware limitado (MacBook 8GB)

## Referencias

- `TAREAS_MEJORAS.md` - Hallazgos y estándares aplicados
- `PLAN_EJECUCION.md` - Progreso y estado de notebooks
- `Version02/README.md` - Overview de Version02

---

*Actualizado: 2026-04-18*