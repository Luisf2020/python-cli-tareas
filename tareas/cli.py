"""Punto de entrada: python -m tareas.cli [listar|agregar|alternar]."""
from __future__ import annotations

import argparse
from pathlib import Path

from .store import Store

ARCHIVO = Path("tareas.json")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="tareas", description="Gestor de tareas en Python.")
    sub = parser.add_subparsers(dest="cmd", required=True)

    sub.add_parser("listar", help="Muestra todas las tareas")
    p_add = sub.add_parser("agregar", help="Agrega una tarea")
    p_add.add_argument("titulo")
    p_toggle = sub.add_parser("alternar", help="Marca/desmarca una tarea")
    p_toggle.add_argument("id", type=int)

    args = parser.parse_args(argv)
    store = Store(ARCHIVO)

    if args.cmd == "agregar":
        t = store.agregar(args.titulo)
        print(f"creada #{t.id}: {t.titulo}")
    elif args.cmd == "alternar":
        t = store.alternar(args.id)
        print(f"#{t.id} {'hecha' if t.hecha else 'pendiente'}")
    else:
        for t in store.listar():
            print(f"[{'x' if t.hecha else ' '}] #{t.id} {t.titulo}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
