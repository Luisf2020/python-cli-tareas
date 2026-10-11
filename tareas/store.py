"""Persistencia simple en JSON con validacion de entradas."""
from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path


@dataclass
class Tarea:
    id: int
    titulo: str
    hecha: bool = False


class Store:
    def __init__(self, ruta: Path) -> None:
        self.ruta = Path(ruta)
        self._tareas: list[Tarea] = []
        self._cargar()

    def _cargar(self) -> None:
        if not self.ruta.exists():
            return
        datos = json.loads(self.ruta.read_text(encoding="utf-8") or "[]")
        self._tareas = [Tarea(**d) for d in datos]

    def _guardar(self) -> None:
        self.ruta.write_text(
            json.dumps([asdict(t) for t in self._tareas], ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

    def agregar(self, titulo: str) -> Tarea:
        titulo = titulo.strip()
        if not titulo:
            raise ValueError("el titulo no puede estar vacio")
        nuevo = Tarea(id=self._siguiente_id(), titulo=titulo)
        self._tareas.append(nuevo)
        self._guardar()
        return nuevo

    def alternar(self, tarea_id: int) -> Tarea:
        for t in self._tareas:
            if t.id == tarea_id:
                t.hecha = not t.hecha
                self._guardar()
                return t
        raise KeyError(f"tarea {tarea_id} no existe")

    def listar(self) -> list[Tarea]:
        return list(self._tareas)

    def _siguiente_id(self) -> int:
        return max((t.id for t in self._tareas), default=0) + 1
