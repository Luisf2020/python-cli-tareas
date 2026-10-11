# python-cli-tareas

CLI de tareas en Python con paquete modular, persistencia JSON y pruebas con pytest.

> Proyecto de portafolio de Luis Felipe Zuniga Leon. Desarrollado con asistencia de IA
> (generacion de codigo, revision y documentacion); el codigo fue revisado y probado manualmente.
> No declara clientes, metricas ni resultados no verificables.

## Stack

- Python 3.10+
- dataclasses
- pytest

## Como ejecutar

```bash
python -m tareas.cli agregar "estudiar"
python -m tareas.cli listar
python -m pytest -q
```

## Estructura

```
tareas/store.py      # persistencia y validacion
tareas/cli.py        # interfaz de linea de comandos
tests/test_store.py  # pruebas unitarias
```

## Estado

Muestra tecnica de portafolio. Sin datos de produccion.
