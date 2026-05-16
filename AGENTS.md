# AGENTS.md - Datajupyer

## Project Type
Educational data science content repository with Jupyter notebooks (Spanish). NOT a typical software project - no build/test/lint systems.

## Structure
- `Version01/` - Older course materials (session 0-6)
- `Version02/` - Newer course materials (12 modules: Python → Pandas → ML)
- `Estudio/` - Personal study notebooks

## Critical Workflow
**Editing Jupyter notebooks has ~70% chance of breaking JSON** (encoding issues). Always recreate with Write tool instead of editing.

Safe workflow:
1. Read existing notebook with Read tool
2. Modify content as needed
3. Write entire file fresh using Write tool
4. Validate: `python -c "import json; json.load(open('notebook.ipynb'))"`
5. If broken: `git restore <archivo>`

## Before Starting Any Notebook Task
Read these files first:
- `PROMTS_NOTEBOOKS.md` - Contains prompts and methodology for recreating notebooks
- `TAREAS_MEJORAS.md` - Documents the audit process and standards applied

## Standards
- Methodology: Objetivos → Analogías → Diagramas ASCII → Tablas → Ejercicios → Resumen
- Python 3.12+ compatible (f-strings, type hints, pathlib)
- All notebooks must pass JSON validation before commit

## Commands
```bash
# Validate a notebook
python -c "import json; json.load(open('notebook.ipynb'))"

# Restore broken notebook
git restore path/to/notebook.ipynb
```