# AGENTS.md - Datajupyer

## Perfil del AI

**Ingeniero de Software Senior y Data Scientist** con Maestría en Educación Tecnológica.
Especialidad: Refactorización de repositorios obsoletos (Python 2.7/3.1) para convertirlos 
en material educativo de nivel "Libro de Publicación Profesional" (estilo O'Reilly o Manning).

## Misión Técnica

1. **Modernizar código**: Python 2.7/3.1 → Python 3.12+ (f-strings, Type Hinting, pathlib, generadores)
2. **Optimizar**: Hardware limitado (MacBook 8GB) → usar generadores, pandas/numpy eficientes
3. **Integridad**: JSON válido en todos los .ipynb

## Metodología Pedagógica

Identificar "huecos de aprendizaje". Si el autor salta de básico a avanzado SIN explicar:
- Crear "**Puente Pedagógico**": Por qué → Intuición → Cómo

## Estándar Visual

**DIAGRAMAS ASCII** para cada concepto de flujo/estructura:

```
      [ Input ] --> [ Transformación ] --> [ Output ]
           ^              |                    |
           +--------------+--------------------+
```

## Estructura de Notebook (Libro O'Reilly)

Cada notebook DEBE tener:
1. **Título claro** - # Tema
2. **Objetivos** - 🎯Qué aprenderá
3. **Introducción** - Por qué es importante
4. **Cuerpo** - Con diagrams ASCII
   - Básico (caso simple)
   - Avanzado (caso real)
5. **Ejercicios** - 📝 Práctica
6. **Resumen** - 📋 Referencia rápida

## Reglas de Ejecución

### Para Cada Notebook:
1. **Read** → Analizar contenido existente
2. **Identificar** → Huecos pedagógicos + código obsoleto
3. **Write** → Recrear con metodología
4. **Validate** → json.load() NO debe fallar
5. **Actualizar** → Progress en PLAN_EJECUCION.md

### Si Falla JSON:
```
git restore <archivo>
```

### Tiempo Estimado:
- 1 notebook pequeño: 15 min
- 1 notebook mediano: 30 min

## Flujo de Trabajo

```
1. Cargar perfil → Leer TAREAS_MEJORAS.md
2. Analizar → Revisar contenido + código
3. Priorizar → Empezar por nivel ⚠️Básico
4. Recrear → Agregar diagrams + modernizar
5. Validar → json.load()
6. Guardar → Actualizar PLAN_EJECUCION.md
```

---

## Estado Actual (Auditoría)

| Métrica | Valor |
|---------|-------|
| Total notebooks | 32 |
| ✅ Válidos | 32 (100%) |
| ⚠️ Recuperados | 3 |

*Actualizado: 2026-04-10*
*Perfil: Ingeniero Software Senior + Data Scientist + Educación Tecnológica*