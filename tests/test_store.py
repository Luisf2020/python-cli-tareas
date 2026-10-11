import json
from pathlib import Path

import pytest

from tareas.store import Store


def test_agregar_y_listar(tmp_path: Path) -> None:
    store = Store(tmp_path / "t.json")
    t1 = store.agregar("primera")
    t2 = store.agregar("segunda")
    assert [t.id for t in store.listar()] == [1, 2]
    assert t1.titulo == "primera" and t2.titulo == "segunda"


def test_titulo_vacio_falla(tmp_path: Path) -> None:
    store = Store(tmp_path / "t.json")
    with pytest.raises(ValueError):
        store.agregar("   ")


def test_alternar_persiste(tmp_path: Path) -> None:
    ruta = tmp_path / "t.json"
    store = Store(ruta)
    t = store.agregar("una")
    store.alternar(t.id)
    recargado = Store(ruta)
    assert recargado.listar()[0].hecha is True
    assert json.loads(ruta.read_text(encoding="utf-8"))[0]["hecha"] is True
