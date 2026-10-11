# python-cli-tareas

![stack: Python 3.10+](https://img.shields.io/badge/stack--Python%203.10+-0d9488?style=flat-square) ![stack: dataclasses](https://img.shields.io/badge/stack--dataclasses-0d9488?style=flat-square) ![stack: pytest](https://img.shields.io/badge/stack--pytest-0d9488?style=flat-square)
![IA: asistido](https://img.shields.io/badge/IA--asistido-6366f1?style=flat-square)

CLI de tareas en Python con paquete modular, persistencia JSON y pruebas con pytest.

> **Transparencia sobre IA:** este proyecto se desarrollo con asistencia de inteligencia artificial (generacion de codigo, revision y documentacion). El codigo fue leido, ejecutado y probado manualmente antes de publicarse. No declara clientes, metricas ni resultados que no puedan verificarse.

## Problema que resuelve

Organizar tareas desde la terminal con datos que sobrevivan al cierre del programa, sin base de datos.

## Solucion implementada

CLI con subcomandos (agregar/listar/completar/borrar) y almacen en JSON con escritura atomica; logica aislada en un modulo con pruebas.

### Funcionalidades principales

- Subcomandos de linea de comandos
- Persistencia JSON con escritura atomica
- Modelo de datos tipado con dataclasses
- Pruebas unitarias con pytest

## Stack

- Python 3.10+
- dataclasses
- pytest

## Estructura

```
tareas/store.py      # persistencia y validacion
tareas/cli.py        # interfaz de linea de comandos
tests/test_store.py  # pruebas unitarias
```

## Puesta en marcha

```bash
python -m tareas.cli agregar "estudiar"
python -m tareas.cli listar
python -m pytest -q
```

## Complejidad del proyecto

**Nivel: Principiante** — Alcance acotado y arquitectura simple (dos modulos), con pruebas automatizadas.

El nivel describe la complejidad tecnica del proyecto, no el grado de dominio de quien lo escribio.

## Despliegue

Herramienta de terminal; no tiene interfaz web.  
El codigo fuente si esta disponible en este repositorio.

## Autor

**Luis Felipe Zuniga Leon** — Desarrollador de software asistido por IA

- GitHub: <https://github.com/Luisf2020>

---

_Proyecto de portafolio. El desarrollo se apoyo en herramientas de IA bajo revision tecnica humana._
